from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

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

from application.analysis import views
from application.analysis import models

from application.target import models


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
from application.analysis.models import Analysis
from application.target.models import Target
from sys import stdout

try:
    db.create_all()

    user = User.query.get(1)
    if user is None:

        #comp1 = Company("Tsoha18", 1)  # agreementlevel: 1 = Pro, 2 = Basic
        db.session.add(Company("Aukustin asianajotoimisto Ky",2)) # agreementlevel: 1 = Pro, 2 = Basic
        db.session.add(Company("Idan ideahautomo",1))
        db.session.commit()
        stdout.write("Companies inserted")

        #def __init__(self, username, firstname, lastname, password, companyid, active):
        db.session.add(User('paivio@tsoha18','Päiviö','Pääkäyttäjä','salainen',None,True))
        db.session.add(User('yngve@tsoha18','Yngve','Ylläpitäjä','salainen',None,True))
        db.session.add(User('aukusti@asianajotoimisto','Aukusti','Asiakas','salainen',1,True))
        db.session.add(User('akuliina@asianajotoimisto', 'Akuliina', 'Asiakas', 'salainen', 1,True))
        db.session.add(User('ida@ideahautomo','Ida','Asiakas','salainen',2,True))
        db.session.commit()
        stdout.write("Users inserted")

        db.session.add(Role('Administrator'))
        db.session.add(Role('Editor'))
        db.session.add(Role('Customer'))
        db.session.commit()
        stdout.write("Roles inserted")

        db.session.add(UserRole(1, 1)) # Administrator-paivio
        db.session.add(UserRole(2, 1)) # Editor-paivio
        db.session.add(UserRole(2, 2)) # Editor-yngve
        db.session.add(UserRole(3, 3)) # Customer-aukusti
        db.session.add(UserRole(3, 4)) # Customer-akuliina
        db.session.add(UserRole(3, 5)) # Customer-ida
        db.session.commit()
        stdout.write("Userroles inserted")


        #Analysis: def __init__(self, companyid, name, keywords):
        db.session.add(Analysis(2,'Tiedeuutiset','als,olkiluoto,cfc,lukutaito,sote',False))
        db.session.commit()
        stdout.write("Analyses inserted")

        #Target: def __init__(self, analysisid, title, uri):
        db.session.add(Target(1,'https://www.aka.fi/fi/tietysti/tiedeuutiset/tiedeuutisia-suomesta1/')) # Akatemia tiedeuutiset
        db.session.add(Target(1, 'https://yle.fi/uutiset/18-212923')) # Yle tiedeuutiset tuoreimmat
        db.session.commit()
        stdout.write("Targets inserted")


except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
    stdout.write(ex2)
    pass
except Exception as ex1:
    stdout.write(ex1)
    pass

