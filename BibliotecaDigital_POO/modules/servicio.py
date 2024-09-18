from modules.dominio import Libro


class GestorDeLibros:
    def __init__(self, gestor_archivo):
        self.__gestor_archivo = gestor_archivo
            
    @property
    def numero_libros(self):
        return len(self.__gestor_archivo.obtener_libros())
   
    def listar_libros_existentes(self):
        lista_de_libros =  self.__gestor_archivo.obtener_libros()
        return [libro.to_dict() for libro in lista_de_libros]
           
    def agregar_nuevo_libro(self, nombre, autor, calificacion):
        libro = Libro(nombre, autor, calificacion)
        self.__gestor_archivo.guardar_libro(libro)


















# from modules.repositorio_abstracto import RepositorioAbstracto

# class GestorDeLibros:
#     def __init__(self, p_repositorio: RepositorioAbstracto):
#         self.__repositorio = p_repositorio
    
#     @property
#     def numero_libros(self):
#         return len(self.__repositorio.obtener_libros())
   
#     def listar_libros_existentes(self):
#         lista_de_libros =  self.__repositorio.obtener_libros()
#         return [libro.to_dict() for libro in lista_de_libros]
           
#     def agregar_nuevo_libro(self, p_nombre, p_autor, p_calificacion):
#         libro = Libro(p_nombre, p_autor, p_calificacion)
#         self.__repositorio.guardar_libro(libro)
    