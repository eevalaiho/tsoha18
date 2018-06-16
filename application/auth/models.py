import jsonpickle
from application import db
from application.models import Base
from application.models import Company

class Role(Base):
    __tablename__ = 'role'

    name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name
        self.done = False


class User(Base):
    __tablename__ = "account"

    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    companyid = db.Column(db.Integer, db.ForeignKey('company.id'))
    active = db.Column(db.Boolean, default=False)

    def __init__(self):
        return

    def __init__(self, username, firstname, lastname, password, companyid, active):
        self.username = username # email address
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.companyid = companyid
        self.active = active

    def toJSON(self):
        return jsonpickle.encode(self)

    def roles(self):
        roles = {1:0, 2:0, 3:0} # 1=Administrator, 2=Editor, 3=Customer
        for role in UserRole.query.filter(UserRole.accountid.__eq__(self.id)).all():
            roles[role.id] = 1
        return roles

    def rolesstring(self):
        roles = db.session.query(Role)\
            .from_statement("SELECT role.* FROM role" +
                " INNER JOIN accountrole ON role.id = accountrole.roleid"
                " WHERE accountrole.accountid = :userid"
            ).params(userid=self.id).all()
        if not roles is None and len(roles) > 0:
            val = map(lambda x: x.name, roles)  # Output: ['python', 'java']
            return ", ".join(val)
        return ""

    def company(self):
        return Company.query.filter_by(id=self.companyid).first()

    def is_anonymous(self):
        return False

    def is_active(self):
        return bool(self.active)

    def is_authenticated(self):
        return True

    def is_admin(self):
        return bool(self.roles().get(1))


class UserRole(Base):
    __tablename__ = 'accountrole'

    roleid = db.Column(db.Integer, db.ForeignKey('role.id',ondelete='CASCADE'), nullable=False)
    accountid = db.Column(db.Integer, db.ForeignKey('account.id',ondelete='CASCADE'), nullable=False)

    def __init__(self, roleid, accountid):
        self.roleid = roleid
        self.accountid = accountid
        self.done = False


