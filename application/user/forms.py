from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, HiddenField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, Length, NoneOf
from wtforms.fields.html5 import EmailField
from application.library import MultiCheckboxField

class UserForm(FlaskForm):
    id = HiddenField("Id")
    companyid = SelectField("Yritys", validators=[NoneOf([''],'Yritystä ei ole valittu')])
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä')])
    active = BooleanField("Hyväksytty")
    userroles = MultiCheckboxField("Käyttäjäryhmät", choices=[['0', 'Pääylläpitäjä'],['1', 'Ylläpitäjä'], ['2','Käyttäjä']])

    class Meta:
        csrf = False


class NewUserForm(FlaskForm):
    companyid = SelectField("Yritys", validators=[NoneOf([''], 'Yritystä ei ole valittu')])
    username = EmailField("Sähköposti", validators=[InputRequired("Sähköposti ei voi olla tyhjä"), Email("Tarkista sähköpostiosoite")])
    firstname= StringField("Etunimi", validators=[InputRequired('Etunimi ei voi olla tyhjä')])
    lastname = StringField("Sukunimi", validators=[InputRequired('Sukunimi ei voi olla tyhjä')])
    password = PasswordField("Salasana", validators=[InputRequired('Salasana ei voi olla tyhjä'), Length(min=5,message='Salasanan tulee olla vähintään 5 merkkiä'), EqualTo('confirm', message='Salasana ja salasanan vahvistus tulee olla samat')])
    confirm = PasswordField("Salasanan vahvistus")
    active = BooleanField("Hyväksytty")
    userroles = MultiCheckboxField("Käyttäjäryhmät", choices=[['0', 'Pääylläpitäjä'],['1', 'Ylläpitäjä'], ['2','Käyttäjä']])

    class Meta:
        csrf = False
