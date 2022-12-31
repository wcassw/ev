from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length
from werkzeug.urls import url_encode   # pragma: no cover
import bcrypt

class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Length(max=140)])
