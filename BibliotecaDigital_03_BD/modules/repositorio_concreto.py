from modules.dominio import Libro
from modules.repositorio_abstracto import RepositorioAbstracto
from modules.modelos import ModeloLibro, Base

  
class RepositorioSQLAlchemy(RepositorioAbstracto):
    def __init__(self, session):
        self.__session = session
        Base.metadata.create_all(self.__session.bind)

    def guardar_registro(self, libro: Libro):
        modelo_libro = self.__map_entidad_a_modelo(libro)
        self.__session.add(modelo_libro)
        self.__session.commit()

    def obtener_todos_los_registros(self):
        modelo_libros = self.__session.query(ModeloLibro).all()
        return [self.__map_modelo_a_entidad(libro) for libro in modelo_libros]      
    
    def modificar_registro(self, libro_modificado: Libro):
        register = self.__session.query(ModeloLibro).filter_by(id=libro_modificado.id).first()
        register.nombre = libro_modificado.nombre
        register.autor = libro_modificado.autor
        register.calificacion = libro_modificado.calificacion
        self.__session.commit()

    def obtener_registro_por_filtro(self, filtro, valor):
        modelo_libro = self.__session.query(ModeloLibro).filter_by(**{filtro:valor}).first()
        return self.__map_modelo_a_entidad(modelo_libro) if modelo_libro else None
    
    def eliminar_registro(self, id):
        register = self.__session.query(ModeloLibro).get(id)
        self.__session.delete(register)
        self.__session.commit()
    
    def __map_entidad_a_modelo(self, entidad: Libro):
        return ModeloLibro(
            nombre=entidad.nombre,
            autor=entidad.autor,
            calificacion=entidad.calificacion
        )
    
    def __map_modelo_a_entidad(self, model: ModeloLibro):
        return Libro(
            model.id,
            model.nombre,
            model.autor,
            model.calificacion
        )
    
