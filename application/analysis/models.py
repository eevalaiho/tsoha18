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
            .filter(Ttarget.ttarget_id.is_(None)).all()

    @staticmethod
    def get_analysis(id):
        sql = text("SELECT Analysis.id, Analysis.name, count(Ttarget.key_word_count), Analysis.date_crawled"
                    " FROM Analysis"
                    " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysis_id"
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








