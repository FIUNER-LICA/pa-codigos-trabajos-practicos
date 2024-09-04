class Chef:
    def __init__(self, p_nombre): # Qué sucede si ingreso un nombre vacío?
        if not isinstance(p_nombre, str) or p_nombre == "":
            raise ValueError("El nombre debe ser un string y no puede estar vacío")
        self.__nombre = p_nombre
        self.__restaurantes_trabajo = []

    @property
    def nombre(self):
        return self.__nombre 
    
    # @property 
    # def restaurantes_trabajo(self): # Esto sería correcto? NO!!!!
    #     return self.__restaurantes_trabajo

    def anotarse_restaurante(self, p_restaurante):
        self.__restaurantes_trabajo.append(p_restaurante)

    def listar_restaurantes_trabajo(self):
        restaurantes = ""
        for res in self.__restaurantes_trabajo:
            restaurantes += f"{res.nombre}\n"  
        return restaurantes          
          
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Restaurantes de trabajo: {[res.nombre for res in self.__restaurantes_trabajo]}"   
    
    def __repr__(self):
        return str(self)
        



if __name__ == '__main__':

    chef_1 = Chef('Raoul')
    print(chef_1.nombre)
    chef_2 = Chef('Abigail')
    print(chef_2)
    chef_3 = Chef('Fabricio')
    print(chef_3)
    lista_chefs = [chef_1, chef_2, chef_3]
    print(lista_chefs)

