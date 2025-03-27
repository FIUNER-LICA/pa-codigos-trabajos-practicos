class Chef:
    def __init__(self, p_nombre, p_antiguedad = 0):
        self.__nombre = p_nombre   # no está terminado!!!
        # self.__primer_nombre = p_nombre
        # self.__segundo_nombre = ''

        self.__antiguedad = p_antiguedad

    def get_nombre(self):
        return self.__nombre
    
    def set_antiguedad(self, p_antiguedad):
        self.__antiguedad = p_antiguedad

    def get_antiguedad(self):
        return self.__antiguedad
    
    def __str__(self):
        # return self.__nombre
        # return self.get_nombre()
        return self.get_nombre() + ', Antigüedad:' + str(self.get_antiguedad())

    
    # No hagas esto!
    # def otro_metodo(self):
    #     self.__nuevo_atributo = 5

class Restaurante:
    def __init__(self, p_nombre_local):
        self.__nombre = p_nombre_local