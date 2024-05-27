from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Tabla de asociación
autores_libros = db.Table( 'autores_libros',
    Column('autores_id', Integer, ForeignKey('autor.id')),
    Column('libros_id', Integer, ForeignKey('libro.id'))
)        
class Autor(db.Model):
    __tablename__ = 'autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    libros_seguidos = relationship("Libro", secondary=autores_libros, backref="autores")

class Libro(db.Model):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), unique=True)


with app.app_context():
    db.create_all()

    libro1 = Libro(titulo='Libro 1')

    libro2 = Libro(titulo='Libro 2')

    autor1 = Autor(nombre='Autor 1')

    autor2 = Autor(nombre='Autor 2')
   
    db.session.add_all([autor1, autor2, libro1, libro2])
    db.session.commit()

    autor1.libros_seguidos.append(libro1)
    autor2.libros_seguidos.append(libro1)

    autor1.libros_seguidos.append(libro2)
    db.session.commit()

    print(autor1.libros_seguidos)
    print(libro1.autores)
    db.session.delete(libro2)
    db.session.commit()
    print(autor1.libros_seguidos)
    

