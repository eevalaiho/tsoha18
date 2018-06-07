from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user

from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm


@app.route("/auth/login", methods=["GET","POST"])
def auth_login():
    if request.method == "GET":
        return render_template("/auth/login.html", form=LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("/auth/login.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("/auth/login.html", form=form, error="Antamasi tunnus ja salasana eivät täsmää\r\n\r\n")

    remember = form.remember
    login_user(user, remember=remember)

    return redirect(url_for("home"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("/auth/register.html", form=RegisterForm())

    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("/auth/register.html", form = form)

    password = form.password.data
    email = form.username.data
    firstname = form.firstname.data
    lastname = form.lastname.data

    user = User(email,firstname,lastname,password,None,False)
    db.session.add(user)

    try:
        db.session().commit()
    except (IntegrityError) as ex1:
        form.username.errors = ["Sähköposti on varattu"]
        return render_template("/auth/register.html", form=form)
    except (DBAPIError, SQLAlchemyError) as ex2:
        form.errors["general"] = ["Lomakkeen lähettäminen ei onnistunut."]
        return render_template("/auth/register.html", form=form)

    flash("Kiitos rekisteröitymisestä! Saat sähköpostia asiakaspalvelustamme, kun tunnuksesi on aktiivinen ja voit kirjautua järjestelmään.")
    return render_template("/auth/register.html", form=form)
