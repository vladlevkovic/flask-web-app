from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, validators


class RegisterForm(FlaskForm):
    email = EmailField('Email:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])
    submit = SubmitField('Register')
