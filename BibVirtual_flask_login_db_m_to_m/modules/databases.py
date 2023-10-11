from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import relationship
from flask_login import UserMixin

asociacion_usuarios_libros = db.Table('usuarios_libros',
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

##CREATE TABLE IN DB
class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    puntaje = Column(Float())
    user_id = Column(Integer(), ForeignKey('users.id'))



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
    libros_seguidos = relationship("Book", secondary=asociacion_usuarios_libros, backref="usuarios")
    
