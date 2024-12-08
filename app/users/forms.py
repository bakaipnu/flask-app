from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp

from app.users.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[
                               DataRequired(),
                               Length(min=3, max=20),
                               Regexp("^[A-Za-z0-9_]+$",
                                      message="Username must contain only letters, numbers, and underscores.")
                           ])

    email = StringField("Email",
                        validators=[
                            DataRequired(),
                            Email()
                        ])

    password = PasswordField("Password",
                             validators=[
                                 DataRequired(),
                                 Length(min=8, max=128, message="Password must be between 8 and 128 characters.")
                             ])

    confirm_password = PasswordField("Confirm Password",
                                     validators=[
                                         DataRequired(),
                                         EqualTo("password", message="Passwords must match.")
                                     ])

    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError("This email is already registered.")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already taken.")
