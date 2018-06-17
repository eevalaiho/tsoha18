import urllib, re, datetime, sys

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.library import admin_required
from application.analysis.models import Analysis
from application.ttarget.models import Ttarget
from application.auth.models import Company
from application.analysis.forms import AnalysisForm, ReportAnalysisForm

from bs4 import BeautifulSoup

import json

@app.route('/analyses', methods=["GET"])
@login_required
@admin_required
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
@admin_required
def analysis(id=None):

    analysis = Analysis(-1,"","", False, None) if id is None else Analysis.query.get(id)

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
        form.company_id.choices=companies
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('analysislist'))

    form = AnalysisForm(request.form, analysis=analysis)
    form.company_id.choices = companies

    if not form.validate():
        return render_template("/analysis/edit.html", analysis=analysis, form=form)

    analysis.company_id = form.company_id.data
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
            sql = text('delete from ttarget where analysis_id = :analysis_id')
            db.engine.execute(sql, analysis_id=analysis.id)
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

    analysis = Analysis.query.get(id)
    db.session().delete(analysis)

    try:
        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
        db.session().rollback()
        flash('Analyysin poistamisessa tapahtui virhe', 'analysis')
        return redirect(url_for('listanalysis'))

    flash('Analyysin poistaminen onnistui','analysis')
    return redirect(url_for('listanalysis'))


@app.route('/analysis/report/<int:id>', methods=["GET", "POST"])
@login_required
@admin_required
def reportanalysis(id):
    analysis = Analysis.query.get(id)

    if analysis is None:
        return redirect(url_for('analysislist'))

    form = ReportAnalysisForm(obj=analysis)

    # GET
    if request.method == "GET":
        return render_template("/analysis/report.html", analysis=analysis, form=form, json=json)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('analysislist'))

    # LOCK analysis and set crawl date
    analysis.date_crawled = db.func.current_timestamp()
    analysis.locked = True

    try:
        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex:
        db.session().rollback()
        sys.stdout.write(ex)
        flash('Raportin tekeminen ei onnistunut', 'analysis')
        return render_template("/analysis/report.html", analysis=analysis, form=form, json=json)

    # Process targets
    try:
        for ttarget in analysis.ttargets():

            # Process root target with NLTK
            ttarget.processWebContent(analysis.keywords)

            # GET 1st level children of the the target url
            res = urllib.request.urlopen(ttarget .url)
            soup = BeautifulSoup(res)
            counter = 0
            for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
                if counter > 3:
                    break;
                subtarget = Ttarget(ttarget.analysis_id, link['href'])
                subtarget.ttarget_id = ttarget.id
                db.session.add(subtarget)
                counter += 1
            db.session().commit()

            # PROCESS subtargets with NLTK
            for subtarget in db.session.query(Ttarget).filter(Ttarget.ttarget_id.__eq__(ttarget.id)):
                subtarget.processWebContent(analysis.keywords)
                db.session.add(subtarget)

            # UPDATE root ttarget
            db.session.add(ttarget)

        analysis.locked = True
        analysis.date_crawled = datetime.datetime.now()
        db.session.add(analysis)

        db.session().commit()

    except (Exception) as ex:
        db.session().rollback()
        sys.stdout.write(ex)
        flash('Raportin tekeminen ei onnistunut', 'analysis')
        return render_template("/analysis/report.html", analysis=analysis, form=form, json=json)

    flash('Raportti valmistui', 'analysis')
    return redirect(url_for('reportanalysis', id=analysis.id))




