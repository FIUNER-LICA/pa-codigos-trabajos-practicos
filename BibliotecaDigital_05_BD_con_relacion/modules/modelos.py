from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

asociacion_usuarios_libros = Table('usuarios_libros', Base.metadata,
    Column('user_id', Integer, ForeignKey('usuarios.id')),
    Column('book_id', Integer, ForeignKey('libros.id'))
)

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

    libros_seguidos = relationship('ModeloLibro', secondary=asociacion_usuarios_libros, backref= 'usuarios_seguidores')