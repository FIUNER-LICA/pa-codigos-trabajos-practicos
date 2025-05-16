from modules.dominio import Libro
from modules.repositorio_abstracto import RepositorioAbstracto

class GestorDeLibros:

    def __init__(self, repo: RepositorioAbstracto):
        self.__repo = repo    
        self.__numero_libros = len(self.__repo.obtener_todos_los_registros())    

    @property
    def numero_libros(self):
        return self.__numero_libros

    def listar_libros_existentes(self):
        registros = self.__repo.obtener_todos_los_registros()
        if not registros:
            return []
        return [libro.to_dict() for libro in registros]

    def agregar_nuevo_libro(self, nombre, autor, calificacion, id_usuario):
        if self.__repo.obtener_registro_por_filtro("nombre", nombre):
            raise ValueError("El libro ya está agregado a la biblioteca")
        libro = Libro(None, nombre, autor, calificacion, id_usuario)
        self.__repo.guardar_registro(libro)
        self.__numero_libros += 1

    def devolver_libro(self, id_libro):
        return self.__repo.obtener_registro_por_filtro("id", id_libro).to_dict() 

    def editar_libro(self, id_libro, nombre, autor, calificacion):
        if self.__repo.obtener_registro_por_filtro("id", id_libro) is None:
            raise ValueError("El libro no existe en la base de datos")
        libro = Libro(id_libro, nombre, autor, calificacion, None)
        self.__repo.modificar_registro(libro)

    def eliminar_libro_seleccionado(self, id_libro):
        if self.__repo.obtener_registro_por_filtro("id", id_libro) is None:
            raise ValueError("El libro no existe en la base de datos")
        self.__repo.eliminar_registro(id_libro)
        self.__numero_libros -= 1 

    def devolver_libros_segun_usuario(self, id_usuario):
        registros = self.__repo.obtener_registros_segun_filtro("id_usuario", id_usuario)
        if registros is None:
            registros = []
        return [libro.to_dict() for libro in registros]
    
    def obtener_libros_seguidos_por_usuario(self, id_usuario):
        return [libro.to_dict() for libro in self.__repo.obtener_registros_seguidos_por_usuario(id_usuario)]