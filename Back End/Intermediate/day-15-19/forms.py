from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, BooleanField, DateTimeField
from wtforms.validators import ValidationError, DataRequired
from wtforms.widgets import TextArea, TextInput
import json

class AddToDo(FlaskForm):
    title = StringField('What do you want to add', validators=[DataRequired()])
    description = StringField('Details on what you want to add', widget=TextArea())
    date = DateTimeField()
    add = SubmitField()

def load_db():
    with open('forms.json') as f:
        return json.load(f)

# data = load_db()

def save_db(data):
    with open('forms.json', 'w') as f:
        json.dump(data, f)