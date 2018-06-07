from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired

class AnalysisForm(FlaskForm):
    id = HiddenField("Id")
    companyid = SelectField("Yritys")
    name = StringField("Nimi", validators=[InputRequired('Nimi ei voi olla tyhjä')])
    keywords = StringField("Avainsanat", validators=[InputRequired('Avainsanat ei voi olla tyhjä')])
    targets = TextAreaField("Kohteet")
    locked = BooleanField("Lukittu")

    class Meta:
        csrf = False
