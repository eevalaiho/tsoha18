from application import db
from application.models import Base
from application.admin.models import Company

class Role(Base):
    __tablename__ = 'role'

    name = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name
        self.done = False


class User(Base):
    __tablename__ = "account"

    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    companyid = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    def __init__(self):
        return

    def __init__(self, username, firstname, lastname, password, companyid):
        self.username = username # email address
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.companyid = companyid

    def get_roles(self):
        roles = {1:0, 2:0, 3:0} # 1=Administrator, 2=Editor, 3=Customer
        for role in UserRole.query.filter(UserRole.accountid.__eq__(self.id)).all():
            roles[role.id] = 1
        return roles

    def get_company(self):
        comp2 = Company.query.filter_by(id=self.companyid).first()
        #comp = Company.get(self.id)
        return comp2

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_admin(self):
        return bool(self.get_roles().get(1))


class UserRole(Base):
    __tablename__ = 'accountrole'

    roleid = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    accountid = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, roleid, accountid):
        self.roleid = roleid
        self.accountid = accountid
        self.done = False


