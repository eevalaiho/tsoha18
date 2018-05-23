from application import app
from application.library import admin_required

from flask import render_template
from flask_login import login_required

@app.route("/")
def index():
    return render_template("/auth/login.html")

@app.route("/edit")
@login_required
def edit():
    return render_template("/edit/home.html")

@app.route("/admin")
@login_required
@admin_required
def admin():
    return render_template("/admin/home.html")

