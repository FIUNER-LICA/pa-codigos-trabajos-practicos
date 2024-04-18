
class Chef:
    def __init__(self, p_nombre):
        self.__nombre = p_nombre
        self.__restaurantes_trabajo = []

    def anotarse_restaurante(self, p_restaurante):
        # if isinstance(p_restaurante, Restaurante):
        self.__restaurantes_trabajo.append(p_restaurante)

    @property
    def nombre(self):
        return self.__nombre

    def listar_restaurantes_trabajo(self):
        # print(self.__restaurantes_trabajo) # Necesita __repr__ en Restaurante
        for res in self.__restaurantes_trabajo:
            print(res)
    
    # def __str__(self):
    #     return f"Nombre: {self.__nombre}"   
    
    def __repr__(self):
        return f"Nombre: {self.__nombre}"
        