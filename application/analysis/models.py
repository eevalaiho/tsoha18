import os
from sqlalchemy import text
from sqlalchemy.orm import relationship
from application import db
from application.models import Base
from application.ttarget.models import Ttarget
from dateutil.parser import parse

class Analysis(Base):
    __tablename__ = "analysis"

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = relationship("Company")
    name = db.Column(db.String(50), nullable=False)
    keywords = db.Column(db.String(150), nullable=False)
    locked = db.Column(db.Boolean, nullable=False, default=False)
    date_crawled = db.Column(db.DateTime)

    def __init__(self, company_id, name, keywords, locked, date_crawled):
        self.company_id = company_id
        self.name = name
        self.keywords = keywords
        self.locked = locked
        self.date_crawled = date_crawled

    def ttargets(self):
        return Ttarget.query.filter(Ttarget.analysis_id.__eq__(self.id))\
            .filter(Ttarget.ttarget_id.is_(None))\
            .order_by(Ttarget.id)\
            .all()

    def get_keywords(self):
        sql = text("select distinct key"
            " from ("
                    " select data.value as keywords"
                    " from ttarget, json_each(ttarget.nltk_analysis) as data"
                    " where key = 'key_words' and ttarget.analysis_id= :id"
                " ) as subq, json_each(subq.keywords)"
                " order by key").params(id=self.id)
        res = db.engine.execute(sql)
        return res

    def get_targets_by_keyword(self,keyword):
        if os.environ.get("HEROKU"):
            sql = text("select ttarget.*, COALESCE(data.kw_count, 0) as kw_count"
                        " from ttarget "
                        " inner join (select ttarget.id as ttarget_id, sum((key_words->>:keyword)::int) as kw_count"
                                    " from ttarget, json_extract_path(ttarget.nltk_analysis, 'key_words') as key_words"
                                    " group by ttarget.id"
                                    " having sum((key_words->>:keyword)::int) > 0) as data on data.ttarget_id = ttarget.id"
                        " where ttarget.analysis_id = :id"
                        " order by kw_count desc")\
                .params(id=self.id, keyword=keyword)
        else:
            sql = text("select ttarget.*, json_extract(ttarget.nltk_analysis, :path) as kw_count"
                       " from ttarget"
                       " where analysis_id= :id and json_extract(ttarget.nltk_analysis, :path) is not null"
                       " order by kw_count desc")\
                .params(id=self.id, path='$.key_words."' + keyword + '"')
        res = db.engine.execute(sql)
        return res

    def get_keyword_counts(self):
        sql = text("select key, sum(cast(cast(value as varchar) as integer)) as _count" 
            " from ("
                    " select data.value as keywords"
                    " from ttarget, json_each(ttarget.nltk_analysis) as data"
                    " where key = 'key_words' and ttarget.analysis_id= :id  and lang is not null" # if lang gets assigned a value then nltk_analysis is not null
                " ) as subq, json_each(subq.keywords)"
            " group by key"
            " order by key").params(id=self.id)
        res = db.engine.execute(sql)
        return res

    def get_report_data(self):
        sql = text("SELECT Analysis.id, Analysis.name, SUM(Ttarget.key_word_count), Analysis.date_crawled"
                    " FROM Analysis"
                    " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysis_id"
                    " GROUP BY Analysis.id, Analysis.name, Analysis.date_crawled "
                    " HAVING Analysis.id = :id"
                    " ORDER BY Analysis.date_crawled desc").params(id=self.id)
        res = db.engine.execute(sql)
        row = res.fetchone()
        if not row is None:
            if os.environ.get("HEROKU"):
                return {"id": row[0], "name": row[1], "count": row[2], "date_crawled": row[3]}
            else:
                # SQLite returns datetime fileds as string when raw SQL is used, ref: https://stackoverflow.com/questions/44781320/dates-as-strings-when-submitting-raw-sql-with-sqlalchemy
                return {"id": row[0], "name": row[1], "count": row[2], "date_crawled": parse(row[3]) if not row[3] is None else ""}
        else:
            return None
