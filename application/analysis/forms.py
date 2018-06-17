from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NoneOf, Length

class AnalysisForm(FlaskForm):
    id = HiddenField("Id")
    company_id = SelectField("Yritys", validators=[NoneOf([''],'Yritystä ei ole valittu')])
    name= StringField("Nimi", validators=[InputRequired('Nimi ei voi olla tyhjä'),Length(max=50, message='Nimi voi olla korkeintaan 50 merkkiä')])
    keywords = StringField("Avainsanat", validators=[InputRequired('Avainsanat ei voi olla tyhjä'),Length(max=150, message='Avainsanat voi olla korkeintaan 150 merkkiä')])
    ttargets = TextAreaField("Kohteet", validators=[Length(max=1024, message='Kohteet voi olla korkeintaan 1024 merkkiä')])
    locked = BooleanField("Lukittu")

    class Meta:
        csrf = False

class ReportAnalysisForm(FlaskForm):
    id = HiddenField("Id")
