# Entidad Libro
class Libro:
    def __init__(self, id, nombre, autor, calificacion):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.calificacion = calificacion

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def calificacion(self):
        return self.__calificacion
    
    @id.setter
    def id(self, p_id):
        if p_id != None:
            if not isinstance(p_id, int):
                raise ValueError("El id del libro debe ser un número entero")
            self.__id = p_id
        else:
            self.__id = None
    
    @nombre.setter
    def nombre(self, p_nombre:str):
        if not isinstance(p_nombre, str) or p_nombre.strip() == "":
            raise ValueError("El nombre del libro debe ser un string y no debe estar vacío")
        self.__nombre = p_nombre.strip()
        
    @autor.setter
    def autor(self, p_autor:str):
        if not isinstance(p_autor, str) or p_autor.strip() == "":
            raise ValueError("El nombre del autor debe ser un string y no debe estar vacío")
        self.__autor = p_autor.strip()

    @calificacion.setter
    def calificacion(self, p_calificacion):
        if not isinstance(p_calificacion, (float, int)):
            raise ValueError("La calificación del libro debe ser un número entre 0 y 10")
        if p_calificacion < 0 or p_calificacion > 10:
            raise ValueError("La calificación del libro debe ser un número entre 0 y 10")
        self.__calificacion = p_calificacion


    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "autor": self.autor,
            "calificacion": self.calificacion
        }

    def __str__(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Calificación: {self.calificacion}"

if __name__ == "__main__":
    l1 = Libro(1, '', "Antoine de Saint-Exupéry", 9.5)
    print(l1)