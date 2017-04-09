from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.

class GraphForm(Form):
    temp = TextField('Temperature', [DataRequired()])
