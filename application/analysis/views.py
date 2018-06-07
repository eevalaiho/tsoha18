from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.library import admin_required
from application.analysis.models import Analysis
from application.target.models import Target
from application.models import Company
from application.analysis.forms import AnalysisForm


@app.route('/analyses', methods=["GET"])
@login_required
def listanalysis():
    return render_template("/analysis/index.html", analyses=Analysis.query.all())


@app.route('/analysis', methods=["GET","POST"])
@app.route('/analysis/<int:id>', methods=["GET","POST"])
@login_required
def analysis(id=None):

    analysis = Analysis(-1,"","") if id is None else Analysis.query.get(id) # __init__(self, companyid, name, keywords):

    if analysis is None:
        return redirect(url_for('analysislist'))

    companies = [("", "---")]+[(str(c.id), c.name) for c in Company.query.all()]

    # GET
    if request.method == "GET":
        targets = "\r\n".join([t.url for t in analysis.get_targets()])
        form = AnalysisForm(obj=analysis, targets=targets)
        form.companyid.choices=companies
        return render_template("/analysis/item.html", analysis=analysis, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('analysislist'))

    form = AnalysisForm(request.form, analysis=analysis)
    form.companyid.choices = companies

    if not form.validate():
        return render_template("/analysis/item.html", analysis=analysis, form=form)

    analysis.companyid = form.companyid.data
    analysis.name = form.name.data
    analysis.keywords = form.keywords.data
    analysis.locked = form.locked.data

    try:
        if (analysis.id is None):
            db.session.add(analysis)
        db.session().commit()
    except (DBAPIError, SQLAlchemyError) as ex2:
        db.session().rollback()
        form.errors["general"] = ["Analyysin tallentaminen ei onnistunut."]
        return render_template("/analysis/item.html", analysis=analysis, form=form)

    # SAVE targets
    try:
        # First delete all existing targets
        sql = text('delete from target where analysisid = :analysisid')
        db.engine.execute(sql, analysisid=analysis.id)
        db.session().flush()
        # Then add new targets
        for url in form.targets.data.split("\r\n"):
            target = Target(analysis.id, url)
            db.session.add(target)
        db.session().commit()
    except (DBAPIError, SQLAlchemyError) as ex2:
        db.session().rollback()
        form.errors["general"] = ["Kohteiden tallentaminen ei onnistunut."]
        return render_template("/analysis/item.html", analysis=analysis, form=form)

    flash('Analyysin tallentaminen onnistui','analysis')
    return render_template("/analysis/item.html", analysis=analysis, form=form)



@app.route('/analysis/<int:id>/delete', methods=["GET"])
@login_required
@admin_required
def deleteanalysis(id):
    obj = Analysis.query.get(id)
    db.session().delete(obj)
    db.session().commit()
    flash('Analyysin poistaminen onnistui','user')
    return redirect(url_for('listanalysis'))

