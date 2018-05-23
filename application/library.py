from functools import wraps
from flask import flash,request,redirect,url_for
from flask_login import current_user

"""
Custom decorator for controller methods that checks wheather a user is an admin
Ref: http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
Ref: https://github.com/paulchakravarti/flask-skeleton/blob/master/admin.py
"""
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None or not current_user.is_authenticated():
            return redirect(url_for('login', next=request.url))
        if not current_user.is_admin():
            flash("Admin login required for this page", "error")
            return redirect(url_for('edit'))
        return f(*args, **kwargs)
    return decorated_function