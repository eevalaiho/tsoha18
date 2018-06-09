from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.library import admin_required
from application.auth.models import User, UserRole
from application.models import Company
from application.user.forms import UserForm, NewUserForm


@app.route('/users', methods=["GET"])
@login_required
@admin_required
def userlist():
    return render_template("/user/index.html", users=User.query.all())


@app.route('/user', methods=["GET","POST"])
@app.route('/user/<id>', methods=["GET","POST"])
@login_required
@admin_required
def user(id=None):

    if not id is None:
        user = User.query.get(id)
        if user is None:
            return redirect(url_for('userlist'))
    else:
        user = None

    companies = [("", "---")]+[(str(c.id), c.name) for c in Company.query.all()]

    # GET
    if request.method == "GET":
        if user is None:
            form = NewUserForm()
        else:
            userroles = []
            for userrole in UserRole.query.filter(UserRole.accountid.__eq__(user.id)).all():
                userroles.append(userrole.roleid)
            form = UserForm(obj=user,userroles=userroles)
        form.companyid.choices = companies
        return render_template("/user/edit.html", user=user, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('userlist'))

    if user is None:
        form = NewUserForm(request.form, companies=companies)
    else:
        form = UserForm(request.form,obj=user,companies=companies)
    form.companyid.choices = companies

    if not form.validate():
        return render_template("/user/edit.html", user=user, form=form)

    if user is None:
        user = User(form.username.data, form.firstname.data, form.lastname.data, form.password.data, form.companyid.data, form.active.data)
        db.session.add(user)
    else:
        user.companyid = form.companyid.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.active = form.active.data

    try:
        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
        form.errors["general"] = ["Käyttäjän tallentaminen ei onnistunut."]
        return render_template("/user/edit.html",user = user,form=form)

    # SAVE roles
    try:
        # First delete all existing roles
        if not id is None:
            sql = text('delete from accountrole where accountid=' + str(user.id))
            db.engine.execute(sql)

        # Then add new roles
        for role_id in form.userroles.data:
            userrole = UserRole(int(role_id),user.id)
            db.session.add(userrole)

        db.session().commit()
    except (DBAPIError, SQLAlchemyError, IntegrityError) as ex2:
        form.errors["general"] = ["Käyttäjäryhmien tallentaminen ei onnistunut."]
        return render_template("/user/edit.html", user=user, form=form)

    flash('Käyttäjän tallentaminen onnistui','user')
    return redirect(url_for('user', id=user.id))



@app.route('/user/<id>/delete', methods=["GET"])
@login_required
@admin_required
def user_delete(id):
    user = User.query.get(id)
    db.session().delete(user)
    db.session().commit()
    flash('Käyttäjän poistaminen onnistui','user')
    return redirect(url_for('userlist'))
