from flask import render_template, session, redirect, url_for, request
from sqlalchemy import text
from application import app, db
from application.models import User, UserRole

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    if not 'currentuser.id' in session or session['currentuser.id'] == None:
        return redirect(url_for('index'))
    return render_template("home.html")

@app.route("/admin")
def admin():
    if session['currentuser.id'] == None:
        return redirect(url_for('index'))
    return render_template("admin.html")

# User
def user():
    return render_template("user.html")

@app.route('/user/<id>', methods=["GET"])
def user(id):
    user = User.query.get(id)
    if user is None:
        return redirect(url_for('users'))
    userroles = {1: 0, 2: 0, 3: 0}  # 1=Administrator, 2=Editor, 3=Customer
    for row in UserRole.query.filter(UserRole.userid.__eq__(user.id)).all():
        userroles[row.roleid] = 1
    return render_template("user.html", user=user, userroles=userroles)

@app.route("/user", methods=["POST"])
def user_save():
    user = User.query.get(request.query_string.get("id"))
    user.firstname = request.form.get("firstname")
    user.lastname = request.form.get("lastname")
    user.date_modified = db.func.current_timestamp()
    db.session().commit()
    return redirect(url_for('user'))

# Profile

@app.route("/profile", methods=["GET"])
def profile():
    if not 'currentuser.id' in session or session['currentuser.id'] == None:
        return redirect(url_for('index'))
    user = User.query.get(session['currentuser.id'])
    if user is None:
        return redirect(url_for('/'))
    return render_template("profile.html", user=user)

@app.route("/profile", methods=["POST"])
def profile_save():
    if not 'currentuser.id' in session or session['currentuser.id'] == None:
        return redirect(url_for('index'))
    user = User.query.get(session['currentuser.id'])
    changepwd = request.form.get("changepwd")
    if not changepwd is None:
        pwd1 = request.form.get("password1")
        pwd2 = request.form.get("password2")
        if not pwd1==pwd2:
            return render_template("profile.html", error="Salasanat eivät täsmää<br><br>")
        user.password = request.form.get("password1")
    else:
        user.firstname = request.form.get("firstname")
        user.lastname = request.form.get("lastname")
    user.date_modified = db.func.current_timestamp()
    db.session().commit()
    return redirect(url_for('profile'))

# Login, logout

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("login")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()
    if not user is None and user.password == password:
        session['currentuser.id'] = user.id # SQLAlchemy models aren't directly serializable to JSON so we'll add only the logged in user's id in session, not the entire user object
        userroles = {1: 0, 2: 0, 3: 0}  # 1=Administrator, 2=Editor, 3=Customer
        for row in UserRole.query.filter(UserRole.userid.__eq__(user.id)).all():
            userroles[row.roleid] = 1
        session['currentuser.roles'] = userroles
        return redirect(url_for('home'))
    return render_template("index.html", error="Antamasi sähköposti ja salasana eivät täsmää\r\n\r\n")

@app.route("/logout")
def logout():
    session.pop('currentuser.id', None)
    return redirect(url_for('index'))

