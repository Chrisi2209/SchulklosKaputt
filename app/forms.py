from flask_wtf import FlaskForm 
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import NumberRange, InputRequired
 
class NeuesKloForm(FlaskForm): 
    building = IntegerField("Gebäudenummer", validators=[NumberRange(0, 33, "Muss von 0 bis 33 sein"), InputRequired("Gib eine Zahl ein")])
    floor = IntegerField("Stocknummer", validators=[NumberRange(0, 5, "Muss von 0 bis 5 sein"), InputRequired("Gib eine Zahl ein")])
    room = IntegerField("Zimmernummer", validators=[NumberRange(0, 99, "Muss von 0 bis 99 sein"), InputRequired("Gib eine Zahl ein")])
    pissoir = BooleanField('Pissoir')
    toilet = IntegerField("Klonummer", validators=[NumberRange(0, 99, "Muss von 0 bis 99 sein"), InputRequired("Gib eine Zahl ein")])
    submit = SubmitField('Klo hinzufügen')

class KloLöschenForm(FlaskForm):
    submit = SubmitField("Löschen")