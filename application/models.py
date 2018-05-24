from application import db
from sqlalchemy.sql import text


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def get_id(self):
        return self.id


class Company(Base):
    __tablename__ = "company"

    name = db.Column(db.String(255), nullable=False)
    agreementlevel = db.Column(db.Integer, nullable=False, default=2)  # 1 = Pro, 2 = Basic

    def __init__(self, name, agreementlevel):
        self.name = name
        self.agreementlevel = agreementlevel

    def get_users(self):
        sql = text("select * from users where companyid = :compid") \
            .params(compid=self.id)
        res = db.engine.execute(sql)

        return res

class Analysis(Base):
    __tablename__ = "analysis"

    companyid = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    keywords = db.Column(db.String(2000), nullable=False)

    def __init__(self, companyid, name, keywords):
        self.companyid = companyid
        self.name = name
        self.keywords = keywords


class Target(Base):
    __tablename__ = "target"

    analysisid = db.Column(db.Integer, db.ForeignKey('analysis.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    uri = db.Column(db.String(255), nullable=False)

    def __init__(self, subjectid, title, type, uri):
        self.subjectid = subjectid
        self.title = title
        self.type = type
        self.uri = uri






