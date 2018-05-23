from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods=["GET","POST"])
def auth_login():
    if request.method == "GET":
        return render_template("/auth/login.html", form=LoginForm())

    form = LoginForm(request.form)

    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("/auth/login.html", form=form, error="Antamasi tunnus ja salasana eivät täsmää\r\n\r\n")

    login_user(user)

    return redirect(url_for("edit"))

'''
    roles = user.get_roles()
    admin = roles[1]
    isadmin = bool(admin)
    user.admin = bool(user.get_roles()[1])
'''


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for('index'))

