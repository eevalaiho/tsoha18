from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required

from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db
from application.library import admin_required
from application.auth.models import User, UserRole
from application.admin.forms import UserForm, NewUserForm


@app.route('/admin/users', methods=["GET"])
@login_required
@admin_required
def userlist():
    return render_template("/admin/userlist.html", users=User.query.all())


@app.route('/admin/user', methods=["GET","POST"])
@login_required
@admin_required
def newuser():

    # GET
    if request.method == "GET":
        return render_template("/admin/user.html", user=None, form = NewUserForm()) # 1=Administrator, 2=Editor, 3=Customer

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('userlist'))

    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("/admin/user.html", user=None, form = form)

    password = form.password.data
    username = form.username.data
    firstname = form.firstname.data
    lastname = form.lastname.data
    active = form.active.data

    user = User(username,firstname,lastname,password,None,active)
    db.session.add(user)

    try:
        db.session().commit()
    except (IntegrityError) as ex1:
        form.username.errors = ["Sähköposti on varattu"]
        return render_template("/admin/user.html", user=None, form=form)
    except (DBAPIError, SQLAlchemyError) as ex2:
        form.errors["general"] = ["Käyttäjän tallentaminen ei onnistunut."]
        return render_template("/admin/user.html", user=None, form=form)

    # GET userid
    user = User.query.filter_by(username=username).first()

    # SAVE roles
    for role_id in form.userroles.data:
        userrole = UserRole(role_id,user.id)
        db.session.add(userrole)

    try:
        db.session().commit()
    except (DBAPIError, SQLAlchemyError) as ex2:
        form.errors["general"] = ["Käyttäjäryhmien tallentaminen ei onnistunut."]
        return render_template("/admin/user.html", user=user, form=form)

    flash('Käyttäjän lisääminen onnistui')
    return redirect(url_for('user', id=user.id))




@app.route('/admin/user/<id>', methods=["GET","POST"])
@login_required
@admin_required
def user(id):
    user = User.query.get(id)
    if user is None:
        return redirect(url_for('userlist'))

    # GET
    if request.method == "GET":
        userroles = []
        for userrole in UserRole.query.filter(UserRole.accountid.__eq__(user.id)).all():
            userroles.append(userrole.id)
        form = UserForm(obj=user,userroles=userroles)
        return render_template("/admin/user.html", user = user, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('userlist'))

    form = UserForm(request.form, obj=user)

    if not form.validate():
        return render_template("/admin/user.html", user = user, form = form)

    user.firstname = form.firstname.data
    user.lastname = form.lastname.data
    user.active = form.active.data

    try:
        db.session().commit()
    except (DBAPIError, SQLAlchemyError) as ex2:
        form.errors["general"] = ["Käyttäjän tallentaminen ei onnistunut."]
        return render_template("/admin/user.html", user = user, form=form)

    flash('Käyttäjän tallentaminen onnistui')
    return render_template("/admin/user.html", user = user, form=form)



@app.route('/admin/user/<id>/delete', methods=["GET"])
@login_required
@admin_required
def user_delete(id):
    user = User.query.get(id)
    db.session().delete(user)
    db.session().commit()
    flash('Käyttäjän poistaminen onnistui')
    return redirect(url_for('userlist'))
