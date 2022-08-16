from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo



# class SignUpForm(FlaskForm):
#     email = StringField('Email', validators= [DataRequired()])
#     username = StringField('Username', validators= [DataRequired()])
#     password = PasswordField('Password', validators= [DataRequired()])
#     confirm_pass = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
#     submit = StringField('Submit', validators= [DataRequired()])

class AddressBook(FlaskForm):
    name = StringField('Name', validators= [DataRequired()])
    number = StringField('Phone Number', validators= [DataRequired()])
    address = StringField('Address', validators= [DataRequired()])
    email = email = StringField('Email', validators= [DataRequired()])
    submit = StringField('Submit', validators= [DataRequired()])