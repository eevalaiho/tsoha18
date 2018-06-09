import sys, jsonpickle, datetime

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
    if not current_user.companyid is None:
        latestreport = Analysis.get_latest_analysis_bycompany(current_user.companyid)
        sys.stdout.write("\r\n\r\n" + str(datetime.datetime.now()) + " INFO " + jsonpickle.encode(latestreport)+ "\r\n\r\n\r\n")
        sys.stdout.flush()
    return render_template("/home.html", latestreport=latestreport)


