import urllib

from functools import wraps
from flask import flash,request,redirect,url_for
from flask_login import current_user

from wtforms import SelectMultipleField, widgets

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
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


'''
Ref: http://wtforms.simplecodes.com/docs/0.6/specific_problems.html#specialty-field-tricks
'''
class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

'''
Ref: https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
Ref: https://www.e-learn.cn/content/wangluowenzhang/388351
'''
def is_valid_url(url, qualifying=None):
    qualifying = ('scheme', 'netloc') if qualifying is None else qualifying
    token = urllib.parse.urlparse(url)
    return all([getattr(token, qualifying_attr)
        for qualifying_attr in qualifying])