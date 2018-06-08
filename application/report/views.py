from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from application import app
from application.analysis.models import Analysis

@app.route('/report/<int:id>', methods=["GET"])
@login_required
def report(id=None):

    analysis = Analysis(-1,"","", False) if id is None else Analysis.query.get(id) # __init__(self, companyid, name, keywords):

    if analysis is None:
        return redirect(url_for('home'))

    keywordmentions = Analysis.get_keyword_mentions(analysis.id)

    return render_template("/report/view.html", analysis=analysis, keywordmentions=keywordmentions)

