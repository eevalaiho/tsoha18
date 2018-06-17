from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.analysis.models import Analysis

@app.route('/report/<int:id>', methods=["GET"])
@login_required
def report(id):

    analysis = db.session.query(Analysis).filter(Analysis.company_id.__eq__(current_user.company_id)).filter(Analysis.id.__eq__(id)).first()

    if analysis is None:
        return redirect(url_for('home'))

    report = Analysis.get_analysis(analysis.id)

    return render_template("/report/view.html", analysis=analysis, report=report)

