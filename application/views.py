from application import app
from application.library import admin_required

from flask import render_template, redirect, url_for
from flask_login import login_required

@app.route("/")
def index():
    return redirect(url_for("auth_login"))

@app.route("/edit")
@login_required
def edit():
    return render_template("/edit/home.html")


