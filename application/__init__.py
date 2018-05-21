from flask import Flask, session, request
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tsoha18.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application import views

from application import models

from application.customer import models

db.create_all()

from sqlalchemy import exists
from application.models import Role #def __init__(self, name):
db_populated = db.session.query(exists().where(Role.id==1)).scalar() # We want to create data only on the first run
if not db_populated:

    role1 = Role('Administrator')
    role2 = Role('Editor')
    role3 = Role('Customer')
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)

    from application.models import User #def __init__(self, username, firstname, lastname, email):
    user1 = User('paivio', 'Päiviö','Pääkäyttäjä','paivio@tsoha18','salainen')
    user2 = User('yngve', 'Yngve','Ylläpitäjä','yngve@tsoha18','salainen')
    user3 = User('aino', 'Aino','Asiakas','aino@tsoha18','salainen')
    user4 = User('reija', 'Reija','Rahakas','reija@tsoha18','salainen')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    from application.models import UserRole #def __init__(self, roleid, userid):
    userrole1 = UserRole(1, 1) # Administrator-paivio
    userrole2 = UserRole(2, 1) # Editor-paivio
    userrole3 = UserRole(2, 2) # Editor-yngve
    userrole4 = UserRole(3, 3) # Customer-aino
    userrole5 = UserRole(3, 4) # Customer-reija
    db.session.add(userrole1)
    db.session.add(userrole2)
    db.session.add(userrole3)
    db.session.add(userrole4)
    db.session.add(userrole5)

    db.session.commit()
