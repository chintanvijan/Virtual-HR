from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email
class RegisterForm(FlaskForm):
	fname = StringField('First Name',validators=[DataRequired(),Length(min=2,max=20)])
	lname = StringField('Last Name',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	sub = SubmitField('Register')