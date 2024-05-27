from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(label='Repeat Password', validators=[DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Log In')

class BooksForm(FlaskForm):
    id = HiddenField(label='')   
    nombre = StringField(label='Nombre', validators=[DataRequired()])
    autor = StringField(label='Autor', validators=[DataRequired()])
    calificacion = StringField(label='Calificacion', validators=[DataRequired()])
    submit = SubmitField(label='Add Book')