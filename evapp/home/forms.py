from wtforms import Form, TextField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.urls import url_encode   # pragma: no cover

class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Length(max=140)])
