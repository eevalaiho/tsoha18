from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.edit.forms import ProfileForm, ChangePasswordForm


@app.route("/edit/profile", methods=["GET","POST"])
@login_required
def profile():
    user = User.query.get(current_user.id)

    if request.method == "GET":
        return render_template("/edit/profile.html", user=current_user, form = ProfileForm(obj=user), cpform = ChangePasswordForm(obj=user))

    if not request.form.get("cancel") is None: # user clicked cancel
        return redirect(url_for('edit'))

    form = ProfileForm(obj=user)
    cpform = ChangePasswordForm(obj=user)

    if request.form.get("changepwd"): # change password form was submitted
        cpform = ChangePasswordForm(request.form)
        if not cpform.validate():
            return render_template("/edit/profile.html", form = form, cpform = cpform)
        user.password = cpform.password
    else:
        form = ProfileForm(request.form)
        if not form.validate():
            return render_template("/edit/profile.html", form = form, cpform = cpform)
        user.firstname = form.firstname
        user.lastname = form.lastname

    user.date_modified = db.func.current_timestamp()
    db.session().commit()
    return render_template("/edit/profile.html", user=current_user, form = form, cpform = cpform)


@app.route("/edit/report", methods=["GET"])
@login_required
def report():
    return render_template("/edit/report.html")