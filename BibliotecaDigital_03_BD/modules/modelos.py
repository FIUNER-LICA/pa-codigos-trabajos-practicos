# from modules.config import db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#2) Creamos la tabla/s que van a estar en nuestra base de datos base_datos.db
class ModeloLibro(Base):
    __tablename__ = 'libros'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    calificacion = Column(Float(), default=0.0)


#__tablename__ corresponde al nombre de la tabla SQL dentro de la base de datos

#primary_key es un campo o conjunto de campos que identifica de manera única cada
#registro en una tabla. suele ser un campo numérico autoincremental que no permite 
#valores duplicados y que se utiliza como índice para acceder a los registros 
#de la tabla de forma rápida y eficiente