from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModeloLibro(Base):
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float(), default=0.0)
    id_usuario = Column(Integer(), ForeignKey('usuarios.id'))

class ModeloUsuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False)
    email = Column(String(1000), nullable=False, unique=True)
    password = Column(String(1000), nullable=False)