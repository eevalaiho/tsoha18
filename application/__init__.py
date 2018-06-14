
# App config

from flask import Flask
app = Flask(__name__)


# SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tsoha18.db"
    app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


# Login functionality part 1

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminnallisuus edellyttää kirjautumista."


# Roles in login_required

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


# Template methods

from application.analysis.models import Analysis
import json

def get_analyses_byuser(user):
    return Analysis.get_analyses_bycompany(user.companyid)
app.jinja_env.globals.update(get_analyses_byuser=get_analyses_byuser)
app.jinja_env.globals.update(json_stringify=json.dumps) # json.dumps(mylist, separators=(',',':'))


# Application views and models

from application import views, models
from application.models import Company
from application.auth import views, models
from application.auth.models import User, Role, UserRole
from application.profile import views
from application.user import views
from application.analysis import views, models
from application.ttarget import models
from application.ttarget.models import Ttarget, NltkAnalysis
from application.report import views


# Login functionality part 2

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# App error handlers


from flask import render_template

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


# Create and populate DB

from sys import stdout
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

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

        import datetime
        #Analysis: def __init__(self, companyid, name, keywords, locked, date_crawled):
        db.session.add(Analysis(2, 'Idan tiedeuutiset', 'luontopaneeli,ilmastonmuutos,aranda,uv-säteily,ilmakehä',False,None))
        db.session.add(Analysis(2, 'Idan keskeneräinen analyysi', '', False, None))
        db.session.add(Analysis(1, 'Aukustin asianajotoimiston ilmastopoiminnat', 'revontulet,arktinen,meteorologi,itämeri',False,None))
        db.session.commit()
        stdout.write("Analyses inserted")

        #Target: def __init__(self, analysisid, url):
        db.session.add(Ttarget(1, 'https://www.aka.fi/fi/tietysti/tiedeuutiset/tiedeuutisia-suomesta1/')) # Akatemia tiedeuutiset
        db.session.add(Ttarget(1, 'https://ilmastotieto.wordpress.com/ilmastouutiset/'))  # Akatemia tiedeuutiset
        db.session.add(Ttarget(3, 'http://ilmatieteenlaitos.fi/tiedeuutisten-arkisto'))
        db.session.commit()
        stdout.write("Targets inserted")


except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
    stdout.write(ex2)
    pass
except Exception as ex1:
    stdout.write(ex1)
    pass

