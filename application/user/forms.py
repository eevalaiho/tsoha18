from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, HiddenField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, Length, NoneOf
from wtforms.fields.html5 import EmailField
from application.library import MultiCheckboxField

class UserForm(FlaskForm):
    id = HiddenField("Id")
    company_id = SelectField("Yritys", validators=[NoneOf([''],'Yritystä ei ole valittu')])
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä'),Length(max=50, message='Etunimi voi olla korkeintaan 50 merkkiä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä'),Length(max=50, message='Sukunimi voi olla korkeintaan 50 merkkiä')])
    active = BooleanField("Hyväksytty")
    userroles = MultiCheckboxField("Käyttäjäryhmät")

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    company_id = SelectField("Yritys", validators=[NoneOf([''], 'Yritystä ei ole valittu')])
    username = EmailField("Sähköposti",validators=[InputRequired("Sähköposti ei voi olla tyhjä"), Email("Tarkista sähköpostiosoite"),Length(min=6, max=254,message='Sähköpostiosoite tulee olla vähintään 6, mutta korkeintaan 254 merkkiä')])
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä'),Length(max=50, message='Etunimi voi olla korkeintaan 50 merkkiä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä'),Length(max=50, message='Sukunimi voi olla korkeintaan 50 merkkiä')])
    password = PasswordField("Salasana", validators=[InputRequired('Salasana ei voi olla tyhjä'), Length(min=5, max=50,message='Salasanan tulee olla vähintään 5 merkkiä, mutta korkeintaan 50 merkkiä'),EqualTo('confirm',message='Salasana ja salasanan vahvistus tulee olla samat')])
    confirm = PasswordField("Salasanan vahvistus")
    active = BooleanField("Hyväksytty")
    userroles = MultiCheckboxField("Käyttäjäryhmät")

    class Meta:
        csrf = False
