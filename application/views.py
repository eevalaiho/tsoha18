from application import app
from application.library import admin_required

from flask import render_template, redirect, url_for
from flask_login import login_required

@app.route("/")
def index():
    return redirect(url_for("auth_login"))

@app.route("/home")
@login_required
def home():
    return render_template("/home.html")


