from wtforms import Form, TextField, PasswordField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from validate_email import validate_email
from werkzeug.urls import url_encode

class contactForm(Form):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email("Please enter your email address.")])
    message= StringField(label='Message')
    submit = SubmitField(label="Log In")


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    username = TextField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )

"""
class LoginForm2(FlaskForm):
    """Login form."""

    email = EmailField(
        "Email Address", validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired()]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(email=self.email.data).first()
        if not self.user:
            self.email.errors.append("Unknown email address!")
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append("Invalid password!")
            return False

        if not self.user.verified:
            self.email.errors.append("Please verify your email address!")
            return False
        return True

# -------

from wtforms.widgets import PasswordInput, CheckboxInput, TextInput
from wtforms.widgets.html5 import EmailInput


class BootstrapVerifyEmail(EmailInput):
    """Bootstrap Validator for email"""

    def __init__(self, error_class=u"is-invalid"):
        super(BootstrapVerifyEmail, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop("class", "") or kwargs.pop("class_", "")
            kwargs["class"] = u"%s %s" % (self.error_class, c)
        return super(BootstrapVerifyEmail, self).__call__(field, **kwargs)


class BootstrapVerifyPassword(PasswordInput):
    """Bootstrap Validator for password"""

    def __init__(self, error_class=u"is-invalid"):
        super(BootstrapVerifyPassword, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop("class", "") or kwargs.pop("class_", "")
            kwargs["class"] = u"%s %s" % (self.error_class, c)
        return super(BootstrapVerifyPassword, self).__call__(field, **kwargs)


class BootstrapVerifyBoolean(CheckboxInput):
    """Bootstrap Validator for boolean"""

    def __init__(self, error_class=u"is-invalid"):
        super(BootstrapVerifyBoolean, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop("class", "") or kwargs.pop("class_", "")
            kwargs["class"] = u"%s %s" % (self.error_class, c)
        return super(BootstrapVerifyBoolean, self).__call__(field, **kwargs)


class BootstrapVerifyText(TextInput):
    """Bootstrap Validator for text"""

    def __init__(self, error_class=u"is-invalid"):
        super(BootstrapVerifyText, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop("class", "") or kwargs.pop("class_", "")
            kwargs["class"] = u"%s %s" % (self.error_class, c)
        return super(BootstrapVerifyText, self).__call__(field, **kwargs)

html
{{ login_user_form.email.label(class_="form-control-label") }}
<div class="input-group input-group-merge">
    <div class="input-group-prepend">
        <span class="input-group-text" id="user"><i class="fas fa-user"></i></span>
    </div>
    {{ login_user_form.email(placeholder="name@example.com", class_="form-control", **{"aria-describedby": "inputGroupPrepend3", "required": ""}) }}
    {% for error in login_user_form.email.errors %}
        <div class="invalid-feedback">{{ error }}</div>
    {% endfor %}
</div>

# ---------------------------------

he usage gets really simple really fast:

from wtforms import validators

from wtforms.validators import Email
from wtforms_widgets.base_form import BaseForm
from wtforms_widgets.fields.core import StringField, PasswordField

class RegisterForm(BaseForm):
    email = StringField('Email Address', [Email(), validators.DataRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [validators.DataRequired(message='Must provide a password. ;-)')])

<form method="POST" action="{{ url_for('auth.register') }}" accept-charset="UTF-8" role="form">
    {% for field in form %}
        {{ field(render_mode='horizontal', autocomplete='off') }}
    {% endfor %}
    <input type="submit" value="submit">
</form>

But this doesn't include validation.

To add validation, I put this in Jinja:

<form method="POST" action="{{ url_for('auth.register') }}" accept-charset="UTF-8" role="form">
    {% for field in form %}
        {{ field() }}
        {% for error in field.errors %}
          <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    {% endfor %}
    <input type="submit" value="submit">
</form>


"""
