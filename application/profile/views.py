from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.profile.forms import ProfileForm, ChangePasswordForm


@app.route("/profile", methods=["GET","POST"])
@login_required
def profile():

    user = User.query.get(current_user.id)
    form = ProfileForm(obj=user)
    cpform = ChangePasswordForm()

    if request.method == "GET":
        return render_template("/profile/profile.html", user=user, form = form, cpform = cpform)

    if not request.form.get("cancel") is None: # user clicked cancel
        return redirect(url_for('edit'))


    if request.form.get("changepwd"): # change password form was submitted
        cpform = ChangePasswordForm(request.form)
        if not cpform.validate():
            form.firstname.data = user.firstname
            form.lastname.data = user.lastname
            return render_template("/profile/profile.html", user=user, form = form, cpform = cpform)
        user.password = cpform.password.data
    else:
        form = ProfileForm(request.form)
        if not form.validate():
            return render_template("/profile/profile.html", user=user, form = form, cpform = cpform)
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data

    user.date_modified = db.func.current_timestamp()
    db.session().commit()

    if request.form.get("changepwd"):  # change password form was submitted
        flash("Salasanan muutos onnistui","profile_password")
    else:
        flash("Profiilin tietojen tallennus onnistui","profile_profile")
    return render_template("/profile/profile.html", user=user, form = ProfileForm(obj=user), cpform = cpform)
