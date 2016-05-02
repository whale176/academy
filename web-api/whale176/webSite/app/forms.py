from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from app.models import User


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default=False)


#
# class RegistrationForm(Form):
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class RegistrationForm(Form):
    username = StringField("User name", validators=[DataRequired("Please enter your user name.")])
    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):

        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        user_email = User.query.filter_by(email=self.email.data.lower()).first()
        user_name = User.query.filter_by(username=self.username.data).first()
        if not user_email:
            if not user_name:
                return True
            self.username.errors.append("This username is already taken")
        self.email.errors.append("This email is already taken")
        return False
