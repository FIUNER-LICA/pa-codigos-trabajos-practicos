from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    def __init__(self, p_nombre_archivo):
        self.nombre_archivo = p_nombre_archivo

    @property
    def nombre_archivo(self):
        return self.__nombre_archivo
    
    @nombre_archivo.setter
    def nombre_archivo(self, p_nombre_archivo):
        self.__nombre_archivo = p_nombre_archivo

    @abstractmethod
    def guardar_libro(self, Libro):
        pass

    @abstractmethod
    def obtener_libros(self) -> list:
        pass