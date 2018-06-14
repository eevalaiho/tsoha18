from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NoneOf

class AnalysisForm(FlaskForm):
    id = HiddenField("Id")
    companyid = SelectField("Yritys", validators=[NoneOf([''],'Yritystä ei ole valittu')])
    name = StringField("Nimi", validators=[InputRequired('Nimi ei voi olla tyhjä')])
    keywords = StringField("Avainsanat", validators=[InputRequired('Avainsanat ei voi olla tyhjä')])
    ttargets = TextAreaField("Kohteet")
    locked = BooleanField("Lukittu")

    class Meta:
        csrf = False

class ReportAnalysisForm(FlaskForm):
    id = HiddenField("Id")
