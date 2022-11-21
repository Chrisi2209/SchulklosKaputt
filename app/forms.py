from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
 
class NeuesKloForm(FlaskForm): 
    gebäudenummer = IntegerField("Gebäudenummer", validators=[NumberRange(0, 33), DataRequired()])
    stocknummer = IntegerField("Stocknummer", validators=[NumberRange(0, 5), DataRequired()])
    zimmernummer = IntegerField("Zimmernummer", validators=[NumberRange(0, 99), DataRequired()])
    pissoir = BooleanField('Pissoir')
    klonummer = IntegerField("Klonummer", validators=[NumberRange(0, 99), DataRequired()])
    submit = SubmitField('Klo hinzufügen')

class KloLöschenForm(FlaskForm):
    submit = SubmitField("Löschen")