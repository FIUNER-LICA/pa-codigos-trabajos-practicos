from modules.chef import Chef

class Cocina:
    def __init__(self):
        self.__lista_chefs = []

    def agregar_chef(self, p_chef):
        if isinstance(p_chef, Chef):
            self.__lista_chefs.append(p_chef)
        else:
            raise TypeError("Ingrese un chef")


class Restaurante:
    def __init__(self, p_nombre):
        self.__nombre = p_nombre  
        self.__cocina = Cocina()    
        self.__chefs_contratados = []  

    def contratar_chef(self, p_chef):
        if p_chef not in self.__chefs_contratados: 
            if isinstance(p_chef, Chef):
                self.__chefs_contratados.append(p_chef)    
                self.__cocina.agregar_chef(p_chef)          
                p_chef.anotarse_restaurante(self) 
        else:
            raise ValueError(f"El chef {p_chef.nombre} ya trabaja en el restaurante {self.__nombre}") 
        
    def listar_chefs(self):
        for chef in self.__chefs_contratados:
            print(chef)

    @property
    def nombre(self):
        return self.__nombre
    
    # def __str__(self):
    #     return f"{self.__nombre}"
    
    def __repr__(self):
        return f"{self.__nombre}"