from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import relationship
from flask_login import UserMixin

asociacion_usuarios_libros = db.Table('usuarios_libros',
    Column('user_id', Integer, ForeignKey('usuarios.id')),
    Column('book_id', Integer, ForeignKey('libros.id'))
)

##CREATE TABLE IN DB
class TablaLibro(db.Model):
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float())
    id_usuario = Column(Integer(), ForeignKey('usuarios.id'))



class TablaUsuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
    libros_seguidos = relationship("TablaLibro", secondary=asociacion_usuarios_libros, backref="usuarios_seguidores")
    
