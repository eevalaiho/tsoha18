from flask import render_template, redirect, url_for, request, flash

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, SQLAlchemyError, IntegrityError

from application import app, db, login_required
from application.auth.models import User, UserRole, Company, Role, RolesEnum
from application.user.forms import UserForm, NewUserForm


@app.route('/users', methods=["GET"])
@login_required(role=RolesEnum.EDIT)
def userlist():
    return render_template("/user/index.html", users=User.query.order_by(User.id).all())


@app.route('/user/view/<id>', methods=["GET"])
@login_required(role=RolesEnum.EDIT)
def viewuser(id):
    user = User.query.get(id)
    if user is None:
        return redirect(url_for('userlist'))
    return render_template("/user/view.html", user=user)


@app.route('/user', methods=["GET","POST"])
@app.route('/user/<id>', methods=["GET","POST"])
@login_required(role=RolesEnum.EDIT)
def user(id=None):

    if not id is None:
        user = User.query.get(id)
        if user is None:
            return redirect(url_for('userlist'))
    else:
        user = None

    companies = [("", "---")]+[(str(c.id), c.name) for c in Company.query.all()]
    userroles = [(str(r.id), r.name) for r in Role.query.all()]

    # GET
    if request.method == "GET":
        if user is None:
            form = NewUserForm()
        else:
            selectedroles = [(str(r.role_id)) for r in UserRole.query.filter(UserRole.account_id.__eq__(user.id)).all()]
            form = UserForm(obj=user,userroles=selectedroles)
        form.company_id.choices = companies
        form.userroles.choices = userroles
        return render_template("/user/edit.html", user=user, form=form)

    # POST
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('userlist'))

    if user is None:
        form = NewUserForm(request.form, companies=companies)
    else:
        form = UserForm(request.form,obj=user,companies=companies)
    form.company_id.choices = companies
    form.userroles.choices = userroles

    if not form.validate():
        return render_template("/user/edit.html", user=user, form=form)

    if user is None:
        user = User(form.username.data, form.firstname.data, form.lastname.data, form.password.data, form.company_id.data, form.active.data)
        db.session.add(user)
    else:
        user.company_id = form.company_id.data
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
            sql = text('delete from accountrole where account_id=' + str(user.id))
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
@login_required(role=RolesEnum.ADMIN)
def user_delete(id):
    user = User.query.get(id)
    db.session().delete(user)
    db.session().commit()
    flash('Käyttäjän poistaminen onnistui','user')
    return redirect(url_for('userlist'))
