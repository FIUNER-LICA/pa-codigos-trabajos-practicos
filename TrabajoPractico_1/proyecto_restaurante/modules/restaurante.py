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


class Cocina:
    def __init__(self):
        self.__lista_chefs = list()

    def agregar_chef(self, p_chef: Chef):
        if isinstance(p_chef, Chef):
            self.__lista_chefs.append(p_chef)
        else:
            # Esto no: print("El chef debe ser un objeto de tipo Chef")
            raise TypeError("El chef debe ser un objeto de tipo Chef")


class Restaurante:
    def __init__(self, p_nombre_local):
        self.__nombre = p_nombre_local
        self.__chefs_contratados = []
        self.__cocina = Cocina()

    def contratar_chef(self, p_chef):
        if isinstance(p_chef, Chef):
            self.__chefs_contratados.append(p_chef)
        else:
            raise TypeError("El chef debe ser un objeto de tipo Chef")
        
    def listar_chefs(self):
        res = []
        for chef in self.__chefs_contratados:
            res.append(chef.get_nombre())
        return res