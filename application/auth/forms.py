from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Sähköposti", validators=[InputRequired("Sähköposti ei voi olla tyhjä")])
    password = PasswordField("Salasana", validators=[InputRequired("Salasana ei voi olla tyhjä")])
    remember = BooleanField("Muista minut")
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = EmailField("Sähköposti", validators=[InputRequired("Sähköposti ei voi olla tyhjä"), Email("Tarkista sähköpostiosoite")])
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä')])
    password = PasswordField("Salasana", validators=[InputRequired('Salasana ei voi olla tyhjä'), Length(min=5,message='Salasanan tulee olla vähintään 5 merkkiä'), EqualTo('confirm', message='Salasana ja salasanan vahvistus tulee olla samat')])
    confirm = PasswordField("Salasanan vahvistus")

    class Meta:
        csrf = False