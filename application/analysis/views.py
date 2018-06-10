from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.library import admin_required
from application.analysis.models import Analysis
from application.ttarget.models import Ttarget
from application.models import Company
from application.analysis.forms import AnalysisForm


@app.route('/analyses', methods=["GET"])
@login_required
def listanalysis():
    return render_template("/analysis/index.html", analyses=Analysis.query.all())


@app.route('/analysis/view/<id>', methods=["GET"])
@login_required
@admin_required
def viewanalysis(id):
    analysis = Analysis.query.get(id)
    if analysis is None:
        return redirect(url_for('analysislist'))
    return render_template("/analysis/view.html", analysis=analysis)


@app.route('/analysis', methods=["GET","POST"])
@app.route('/analysis/<int:id>', methods=["GET","POST"])
@login_required
def analysis(id=None):

    #def __init__(self, companyid, name, keywords, locked, date_crawled):
    analysis = Analysis(-1,"","", False, None) if id is None else Analysis.query.get(id) # __init__(self, companyid, name, keywords):

    if analysis is None:
        return redirect(url_for('analysislist'))

    companies = [("", "---")]+[(str(c.id), c.name) for c in Company.query.all()]

    # GET
    if request.method == "GET":
        urls = []
        for ttarget in analysis.ttargets():
            urls.append(ttarget.url)
        form = AnalysisForm(obj=analysis)
        form.ttargets.data="\r\n".join(urls)
        form.companyid.choices=companies
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('analysislist'))

    form = AnalysisForm(request.form, analysis=analysis)
    form.companyid.choices = companies

    if not form.validate():
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    analysis.companyid = form.companyid.data
    analysis.name = form.name.data
    analysis.keywords = form.keywords.data
    analysis.locked = form.locked.data

    try:
        if (analysis.id is None):
            db.session.add(analysis)
        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
        db.session().rollback()
        form.errors["general"] = ["Analyysin tallentaminen ei onnistunut."]
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    # SAVE targets
    try:
        # First delete all existing targets
        if not id is None:
            sql = text('delete from ttarget where analysisid = :analysisid')
            db.engine.execute(sql, analysisid=analysis.id)
            db.session().flush()

        # Then add new targets
        for url in form.ttargets.data.split("\r\n"):
            ttarget = Ttarget(analysis.id, url)
            db.session.add(ttarget)

        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
        db.session().rollback()
        form.errors["general"] = ["Kohteiden tallentaminen ei onnistunut."]
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    flash('Analyysin tallentaminen onnistui','analysis')
    return redirect(url_for('analysis', id=analysis.id))


@app.route('/analysis/<int:id>/delete', methods=["GET"])
@login_required
@admin_required
def deleteanalysis(id):
    obj = Analysis.query.get(id)
    db.session().delete(obj)
    db.session().commit()
    flash('Analyysin poistaminen onnistui','analysis')
    return redirect(url_for('listanalysis'))

