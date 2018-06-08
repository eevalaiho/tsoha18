from application import app
from application.analysis.models import Analysis

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

@app.route("/")
def index():
    return redirect(url_for("auth_login"))

@app.route("/home")
@login_required
def home():
    latestreport = Analysis.get_latest_analysis(current_user.companyid)
    return render_template("/home.html", latestreport=latestreport)


