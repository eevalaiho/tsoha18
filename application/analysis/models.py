import os
from sqlalchemy import text
from application import db
from application.models import Base
from application.ttarget.models import Ttarget
from application.models import Company
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

    def company(self):
        return Company.query.filter_by(id=self.companyid).first()

    def ttargets(self):
        return Ttarget.query.filter(Ttarget.analysisid.__eq__(self.id))\
            .filter(Ttarget.ttarget_id.is_(None)).all()

    @staticmethod
    def get_analyses_bycompany(companyid):
        return Analysis.query\
            .filter(Analysis.companyid.__eq__(companyid)) \
            .order_by(Analysis.locked.desc(),Analysis.name.desc())\
            .all()

    @staticmethod
    def get_finished_analyses_bycompany(companyid):
        # Filtering SQLAlchemy queries by a boolean value seems to behave differently
        # with SQLite as compared to Postgres so it's safer to use raw SQL here
        analyses = db.session.query(Analysis)\
            .from_statement("SELECT Analysis.* " +
                " FROM Analysis" +
                " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysisid"
                " WHERE Analysis.companyid = :companyid AND Analysis.locked AND NOT Analysis.date_crawled IS NULL"
            ).params(companyid=companyid).all()
        return analyses

    @staticmethod
    def get_latest_analysis_bycompany(companyid):
        result = Analysis.get_finished_analyses_bycompany(companyid)
        for analysis in result:
            return Analysis.get_analysis(analysis.id)
        return None

    @staticmethod
    def get_analysis(id):
        sql = text("SELECT Analysis.id, Analysis.name, count(Ttarget.key_word_count), Analysis.date_crawled"
                    " FROM Analysis"
                    " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysisid"
                    " GROUP BY Analysis.id, Analysis.name, Analysis.date_crawled "
                    " HAVING Analysis.id = :id").params(id=id)
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








