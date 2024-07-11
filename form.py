#!/usr/bin/python3
""" forms for registration and login in """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    """ login form """
    username = StringField('Username', validators=[Length(min=4, max=20), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=5, max=16), DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    """ Signup form """
    name = StringField('Name', validators=[Length(min=3, max=50), DataRequired()])
    username = StringField('Username', validators=[Length(min=4, max=20), DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=5, max=16), DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField('Submit')

    def to_dict(self):
        """ presents the user data in a dictionary format """
        form_dict = {
            self.name.name: self.name.data,
            self.username.name: self.username.data,
            self.email.name: self.email.data,
            self.password.name: self.password.data
        }

        return form_dict