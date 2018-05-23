from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User

'''
@app.route("/edit/unauthorized", methods=["GET"])
@login_required
def unauthorized():
    return render_template("/edit/unauthorized.html")
'''

@app.route("/edit/profile", methods=["GET"])
@login_required
def profile():
    return render_template("/edit/profile.html", user=current_user)

@app.route("/edit/profile", methods=["POST"])
@login_required
def profile_save():
    info = ""
    info2= ""
    user = User.query.get(current_user.id)
    cancel = request.form.get("cancel")
    if not cancel is None:
        return redirect(url_for('edit'))
    changepwd = request.form.get("changepwd")
    if changepwd is None:
        user.firstname = request.form.get("firstname")
        user.lastname = request.form.get("lastname")
        info = "Tiedot tallennettu"
    else:
        pwd1 = request.form.get("password1")
        pwd2 = request.form.get("password2")
        if not pwd1 == pwd2:
            return render_template("/edit/profile.html", user=current_user, error2="Salasanat eivät täsmää")
        user.password = request.form.get("password1")
        info2 = "Salasana vaihdettu"
    user.date_modified = db.func.current_timestamp()
    db.session().commit()
    return render_template("/edit/profile.html", user=current_user, info=info, info2=info2)
