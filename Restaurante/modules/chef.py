class Chef:
    def __init__(self, p_nombre): # Qué sucede si ingreso un nombre vacío?
        self.__nombre = p_nombre
        self.__restaurantes_trabajo = []

    def anotarse_restaurante(self, p_restaurante):# Qué sucede si verifico si es una instancia de Restaurante?
        self.__restaurantes_trabajo.append(p_restaurante)

    @property
    def nombre(self):
        return self.__nombre       
    
    # @property 
    # def restaurantes_trabajo(self): # Esto sería correcto?
    #     return self.__restaurantes_trabajo

    def listar_restaurantes_trabajo(self):
        restaurantes = ""
        for res in self.__restaurantes_trabajo:
            restaurantes += f"{res.nombre}\n"  
        return restaurantes          
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Restaurantes de trabajo: {[res.nombre for res in self.__restaurantes_trabajo]}"   
    
    # def __repr__(self):
    #     return f"Nombre: {self.__nombre}"
        

if __name__ == '__main__':
    
    chef_1 = Chef('Raoul')
    print(chef_1.nombre)
    chef_2 = Chef('Abigail')
    print(chef_2)
    chef_3 = Chef('Fabricio')
    print(chef_3)
    lista_chefs = [chef_1, chef_2, chef_3]
    print(lista_chefs)

