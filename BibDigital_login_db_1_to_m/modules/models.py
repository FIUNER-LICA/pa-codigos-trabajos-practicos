from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from flask_login import UserMixin


##CREATE TABLE IN DB
class TablaLibro(db.Model):
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float())
    id_usuario = Column(Integer(), ForeignKey('usuarios.id')) 
    # Esta clave foranea es para relacionar la tabla libros con la tabla usuarios


class TablaUsuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))