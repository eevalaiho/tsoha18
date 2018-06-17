from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, EqualTo, Length

class ProfileForm(FlaskForm):
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä'),Length(max=50, message='Etunimi voi olla korkeintaan 50 merkkiä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä'),Length(max=50, message='Sukunimi voi olla korkeintaan 50 merkkiä')])
    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    password = PasswordField("Salasana", validators=[InputRequired('Salasana ei voi olla tyhjä'), Length(min=5, max=50, message='Salasanan tulee olla vähintään 5 merkkiä, mutta korkeintaan 50 merkkiä'),EqualTo('confirm',message='Salasana ja salasanan vahvistus tulee olla samat')])
    confirm = PasswordField("Salasanan vahvistus")
    class Meta:
        csrf = False