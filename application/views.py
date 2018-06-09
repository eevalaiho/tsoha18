import sys

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
    latestreport = None
    sys.stdout.write(current_user.toJSON())
    sys.stdout.flush()
    if not current_user.companyid is None:
        latestreport = Analysis.get_latest_analysis_bycompany(current_user.companyid)
    return render_template("/home.html", latestreport=latestreport)


