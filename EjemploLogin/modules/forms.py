# 2)Este tipo de formularios permite validar el ingreso de datos,
# el formato de email, tamaño de contraseña y confirmación de contraseña
from flask_wtf import FlaskForm # pip install flask-wtf
from wtforms import StringField, PasswordField, SubmitField # https://wtforms.readthedocs.io/en/2.3.x/
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(label='Repeat Password', validators=[DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField(label='Log In')