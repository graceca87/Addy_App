from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length


class AddressBook(FlaskForm):
    name = StringField('Name', validators= [InputRequired()])
    number = StringField('Phone Number', validators= [InputRequired(), Length(min=7, max=14)])
    address = StringField('Address', validators= [InputRequired()])
    email = email = StringField('Email', validators= [InputRequired()])
    submit = SubmitField('Submit', validators= [InputRequired()])


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField()





