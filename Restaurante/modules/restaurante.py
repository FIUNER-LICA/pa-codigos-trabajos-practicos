from modules.chef import Chef

class Cocina:
    def __init__(self):
        self.__lista_chefs = []

    def agregar_chef(self, p_chef): #Es necesario verificar si es una instancia de Chef?
        self.__lista_chefs.append(p_chef)
        

class Restaurante:
    def __init__(self, p_nombre): # Qué sucede si ingreso un nombre vacío durante la creación?
        self.nombre = p_nombre  
        self.__cocina = Cocina()    
        self.__chefs_contratados = []  

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, p_nombre):
        if not isinstance(p_nombre, str) or p_nombre == "":
            raise ValueError("El nombre debe ser un string y no puede estar vacío")
        self.__nombre = p_nombre 

    def contratar_chef(self, p_chef):
        if not isinstance(p_chef, Chef):
            raise ValueError("El parámetro ingresado no es un Chef")
        if p_chef not in self.__chefs_contratados: 
            self.__chefs_contratados.append(p_chef)    
            self.__cocina.agregar_chef(p_chef)          
            p_chef.anotarse_restaurante(self) 
        else:
            print(f"El nombre {p_chef.nombre} ya está en la lista de contratados") 
        
    def listar_chefs(self):
        contratados = ""
        for chef in self.__chefs_contratados:
            contratados += f"{chef.nombre}\n"
        return f"Chefs Contratados:\n{contratados}"
    
    def __str__(self):
        return f"{self.__nombre}"
    
    def __repr__(self):
        return f"{self.__nombre}"

if __name__ == '__main__':

    restaurante1 = Restaurante('')
    # print(restaurante1.nombre)
    # restaurante1.nombre = 'Ratatouille'
    # print(restaurante1.nombre)