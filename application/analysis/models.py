from sqlalchemy import text
from application import db
from application.models import Base
from application.ttarget.models import Ttarget
from datetime import datetime
from dateutil.parser import parse

class Analysis(Base):
    __tablename__ = "analysis"

    companyid = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(2000), nullable=False)
    locked = db.Column(db.Boolean, nullable=False, default=False)
    date_crawled = db.Column(db.DateTime)

    def __init__(self, companyid, name, keywords, locked, date_crawled):
        self.companyid = companyid
        self.name = name
        self.keywords = keywords
        self.locked = locked
        self.date_crawled = date_crawled

    def get_ttargets(self):
        return Ttarget.query.filter(Ttarget.analysisid.__eq__(self.id)).all()

    @staticmethod
    def get_analyses_bycompany(companyid):
        return Analysis.query\
            .filter(Analysis.companyid.__eq__(companyid)) \
            .order_by(Analysis.locked.desc(),Analysis.name.desc())\
            .all()

    @staticmethod
    def get_finished_analyses_bycompany(companyid):
        return Analysis.query\
            .filter(Analysis.companyid.__eq__(companyid) and Analysis.locked == 1 and not Analysis.date_crawled is None) \
            .order_by(Analysis.date_crawled.desc())\
            .all()

    @staticmethod
    def get_latest_analysis_bycompany(companyid):
        result = Analysis.get_finished_analyses_bycompany(companyid)
        for analysis in result:
            return Analysis.get_keyword_mentions(analysis.id)
        return None

    @staticmethod
    def get_keyword_mentions(id):
        sql = text("SELECT Analysis.id, Analysis.name, count(Ttarget.keywordmentioncount), Analysis.date_crawled"
                    " FROM Analysis"
                    " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysisid"
                    " WHERE Analysis.id = " + str(id))
        res = db.engine.execute(sql)
        row = res.fetchone()
        # SQLite returns datetime fileds as string in when raw SQL is used, ref: https://stackoverflow.com/questions/44781320/dates-as-strings-when-submitting-raw-sql-with-sqlalchemy
        return {"id": row[0], "name": row[1], "count": row[2], "date_crawled": parse(row[3]) if not row[3] is None else ""}








