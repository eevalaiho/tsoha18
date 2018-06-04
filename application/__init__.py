from flask import Flask
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tsoha18.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application import views
from application import models

from application.auth import views
from application.auth import models

from application.profile import views
from application.user import views


from os import urandom
app.config["SECRET_KEY"] = urandom(32)


from application.auth.models import User
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminnallisuus edellyttää kirjautumista."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from application.auth.models import Role
from application.models import Company
from application.auth.models import UserRole
from sys import stdout

try:
    db.create_all()

    user = User.query.get(1)
    if user is None:

        #comp1 = Company("Tsoha18", 1)  # agreementlevel: 1 = Pro, 2 = Basic
        comp2 = Company("Aukustin asianajotoimisto Ky",2) # agreementlevel: 1 = Pro, 2 = Basic
        comp3 = Company("Idan ideahautomo",1)
        #db.session.add(comp1)
        db.session.add(comp2)
        db.session.add(comp3)
        db.session.commit()
        stdout.write("Companies inserted")

        #def __init__(self, username, firstname, lastname, password, companyid, active):
        user1 = User('paivio@tsoha18','Päiviö','Pääkäyttäjä','salainen',None,True)
        user2 = User('yngve@tsoha18','Yngve','Ylläpitäjä','salainen',None,True)
        user3 = User('aukusti@asianajotoimisto','Aukusti','Asiakas','salainen',1,True)
        user5 = User('akuliina@asianajotoimisto', 'Akuliina', 'Asiakas', 'salainen', 1,True)
        user4 = User('ida@ideahautomo','Ida','Asiakas','salainen',2,True)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.add(user5)
        db.session.commit()
        stdout.write("Users inserted")

        role1 = Role('Administrator')
        role2 = Role('Editor')
        role3 = Role('Customer')
        db.session.add(role1)
        db.session.add(role2)
        db.session.add(role3)
        db.session.commit()
        stdout.write("Roles inserted")

        userrole1 = UserRole(1, 1) # Administrator-paivio
        userrole2 = UserRole(2, 1) # Editor-paivio
        userrole3 = UserRole(2, 2) # Editor-yngve
        userrole4 = UserRole(3, 3) # Customer-aukusti
        userrole5 = UserRole(3, 4) # Customer-akuliina
        userrole6 = UserRole(3, 5) # Customer-ida
        db.session.add(userrole1)
        db.session.add(userrole2)
        db.session.add(userrole3)
        db.session.add(userrole4)
        db.session.add(userrole5)
        db.session.add(userrole5)
        db.session.commit()
        stdout.write("Userroles inserted")

except:
    pass

