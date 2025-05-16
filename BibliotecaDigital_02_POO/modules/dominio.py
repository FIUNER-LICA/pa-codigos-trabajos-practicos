class Libro:
    def __init__(self, p_nombre, p_autor, p_calificacion):
        self.nombre = p_nombre
        self.autor = p_autor
        self.calificacion = p_calificacion

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def calificacion(self):
        return self.__calificacion
    
    @nombre.setter
    def nombre(self, p_nombre):
        if not isinstance(p_nombre, str) or p_nombre.strip() == "":
            raise ValueError("El nombre del libro debe ser un string y no debe estar vacío")
        self.__nombre = p_nombre.strip()
        
    @autor.setter
    def autor(self, p_autor):
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
            "nombre": self.nombre,
            "autor": self.autor,
            "calificacion": self.calificacion
        }

    def __str__(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Calificación: {self.calificacion}"


if __name__ == "__main__":
    libro1 = Libro("1984", "George Orwell", 10)