from flask import render_template, session, redirect, url_for, request
from flask_login import login_required

from application import app, db
from application.library import admin_required
from application.auth.models import User, UserRole

@app.route('/admin/user', methods=["GET"])
@login_required
@admin_required
def userlist():
    return render_template("/admin/userlist.html", users=User.query.all())

@app.route('/admin/user/<id>', methods=["GET"])
@login_required
@admin_required
def user(id):

    user = User.query.get(id)
    if user is None:
        return redirect(url_for('user'))

    userroles = {1: 0, 2: 0, 3: 0}  # 1=Administrator, 2=Editor, 3=Customer
    for row in UserRole.query.filter(UserRole.accountid.__eq__(user.id)).all():
        userroles[row.roleid] = 1

    return render_template("/admin/user.html", user=user, userroles=userroles)

@app.route("/admin/user", methods=["POST"])
@login_required
@admin_required
def user_save():

    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('userlist'))

    id = request.form.get("id")
    if id is None:
        user = User()
    else:
        user = User.query.get(id)
    user.firstname = request.form.get("firstname")
    user.lastname = request.form.get("lastname")
    user.date_modified = db.func.current_timestamp()

    db.session().commit()

    return redirect(url_for('user'))

@app.route("/admin/user/add", methods=["GET"])
@login_required
@admin_required
def user_add():
    userroles = {1: 0, 2: 0, 3: 0}  # 1=Administrator, 2=Editor, 3=Customer
    user = User
    return render_template("/admin/user_add.html", user=user, userroles=userroles)

@app.route('/admin/user/<id>/delete', methods=["GET"])
@login_required
@admin_required
def user_delete(id):
    user = User.query.get(id)
    db.session().delete(user)
    db.session().commit()
    return redirect(url_for('userlist'))
