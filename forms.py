from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, TextAreaField, PasswordField, SelectField, SelectMultipleField, IntegerField, validators

class MoanForm(Form):
    moan = TextAreaField('Your Moan', [validators.Required()])
    user = TextField('And your name', [validators.Required()])