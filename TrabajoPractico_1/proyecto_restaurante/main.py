from modules.restaurante import Chef, Cocina, Restaurante

chef1 = Chef('Raul')
chef2 = Chef('Jose')
chef3 = Chef('Sonia')

# Hay mejores alternativas. En clase se discutieron los motivos.
# print(chef1.nombre) # 'Raul'
# chef1.nombre = ''   
# print(chef1.nombre) # ''

print(chef1.get_nombre())
print(chef2.get_nombre())

chef2.set_antiguedad(4)
print(chef1.get_antiguedad())
print(chef2.get_antiguedad())

print(chef1)

# chef1.imprimir_nombre()  # No recomendado! Vincula la interfaz de usuario con el modelo de dominio (Chef)


cocina1 = Cocina()
cocina1.agregar_chef(chef1)
del cocina1

restaurante = Restaurante("Coscoino")
restaurante.contratar_chef(chef1)
restaurante.contratar_chef(chef2)
restaurante.contratar_chef(chef3)

lista_de_chefs = restaurante.listar_chefs()
print(lista_de_chefs)