from application import db
from application.models import Base
from sqlalchemy.sql import text


class Company(Base):
    __tablename__ = "company"

    name = db.Column(db.String(255), nullable=False)
    agreementlevel = db.Column(db.Integer, nullable=False, default=2) # 1 = Pro, 2 = Basic

    def __init__(self, name, agreement):
        self.name = name
        self.agreement = agreement

    def get_users(self):
        sql = text("select * from users where companyid = :compid")\
            .params(compid = self.id)
        res = db.engine.execute(sql)

        return res