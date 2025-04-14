class Persona:
    def __init__(self, p_nombre):
        self.__nombre = p_nombre

    @property
    def nombre(self):
        return self.__nombre

    # def get_nombre(self):
    #     return self.__nombre
    
    @nombre.setter
    def nombre(self, p_nombre):
        if p_nombre.strip() == "":
            raise ValueError("El nombre no puede ser una cadena vacia") 
        self.__nombre = p_nombre