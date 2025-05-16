from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def guardar_registro(self, entidad):
        raise NotImplementedError

    @abstractmethod
    def obtener_todos_los_registros(self) -> list:
        raise NotImplementedError
    
    @abstractmethod
    def modificar_registro(self, entidad_modificada):
        raise NotImplementedError   
    
    @abstractmethod
    def obtener_registro_por_filtro(self, filtro, valor):
        raise NotImplementedError
    
    @abstractmethod
    def eliminar_registro(self, id):
        raise NotImplementedError

