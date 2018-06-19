import jsonpickle, os
from datetime import datetime
from application import db
from application.models import Base
from application.analysis.models import Analysis
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'role'
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name
        self.done = False

class Company(Base):
    __tablename__ = "company"
    name = db.Column(db.String(50), nullable=False)
    users = relationship("User", back_populates="company")
    analyses = relationship("Analysis")

    def __init__(self, name):
        self.name = name

    def get_finished_analyses(self):
        # Filtering SQLAlchemy queries by a boolean value seems to behave differently
        # with SQLite as compared to Postgres so it's safer to use raw SQL here
        analyses = db.session.query(Analysis)\
            .from_statement("SELECT Analysis.* " +
                " FROM Analysis" +
                " INNER JOIN Ttarget ON Analysis.id = Ttarget.analysis_id"
                " WHERE Analysis.company_id = :company_id AND Analysis.locked AND NOT Analysis.date_crawled IS NULL"
                " ORDER BY Analysis.date_crawled DESC"
            ).params(company_id=self.id).all()
        # SQLite returns datetime fileds as string when raw SQL is used, ref: https://stackoverflow.com/questions/44781320/dates-as-strings-when-submitting-raw-sql-with-sqlalchemy
        if not analyses is None:
            if not os.environ.get("HEROKU"):
                for analysis in analyses:
                    analysis.date_crawled = datetime.strptime(analysis.date_crawled, '%Y-%m-%d %H:%M:%S.%f') #2018-06-17 16:27:56.980978
            return analyses
        return None

    def get_latest_analysis(self):
        result = self.get_finished_analyses()
        if not result is None and len(result) > 0:
            return result[0].get_report_data()
        return None


class User(Base):
    __tablename__ = "account"

    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = relationship("Company", back_populates="users")
    active = db.Column(db.Boolean, default=False)

    def __init__(self):
        return

    def __init__(self, username, firstname, lastname, password, company_id, active):
        self.username = username # email address
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.company_id = company_id
        self.active = active

    def is_anonymous(self):
        return False

    def is_active(self):
        return bool(self.active)

    def is_authenticated(self):
        return True

    def is_admin(self):
        return bool(self.roles().get(1))

    def toJSON(self):
        return jsonpickle.encode(self)

    def roles(self):
        roles = {1:0, 2:0, 3:0} # 1=Administrator, 2=Editor, 3=Customer
        for role in UserRole.query.filter(UserRole.account_id.__eq__(self.id)).all():
            roles[role.id] = 1
        return roles

    def rolesstring(self):
        roles = db.session.query(Role)\
            .from_statement("SELECT role.* FROM role" +
                " INNER JOIN accountrole ON role.id = accountrole.role_id"
                " WHERE accountrole.account_id = :userid"
            ).params(userid=self.id).all()
        if not roles is None and len(roles) > 0:
            val = map(lambda x: x.name, roles)  # Output: ['python', 'java']
            return ", ".join(val)
        return ""

    def get_latest_analysis(self):
        return self.company.get_latest_analysis()


class UserRole(Base):
    __tablename__ = 'accountrole'

    role_id = db.Column(db.Integer, db.ForeignKey('role.id',ondelete='CASCADE'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id',ondelete='CASCADE'), nullable=False)

    def __init__(self, role_id, account_id):
        self.role_id = role_id
        self.account_id = account_id
        self.done = False


