from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from flask_login import UserMixin


##CREATE TABLE IN DB
class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    puntaje = Column(Float())
    user_id = Column(Integer(), ForeignKey('users.id')) 
    # Esta clave foranea es para relacionar la tabla books con la tabla users


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))