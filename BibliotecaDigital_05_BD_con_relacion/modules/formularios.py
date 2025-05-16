from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class FormRegistro(FlaskForm):
    nombre = StringField(label="Nombre", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4), EqualTo('confirmacion', message='Las contraseñas deben coincidir')])
    confirmacion = PasswordField(label='Repetir Password', validators=[DataRequired()])
    submit = SubmitField(label='Registrar')

class FormLogin(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label='Ingresar')

class BooksForm(FlaskForm):
    id = HiddenField(label='')   
    nombre = StringField(label='Nombre', validators=[DataRequired()])
    autor = StringField(label='Autor', validators=[DataRequired()])
    calificacion = StringField(label='Calificacion', validators=[DataRequired()])
    submit = SubmitField(label='Agregar libro')