from modules.chef import Chef
from modules.restaurante import Restaurante

restaurante_1 = Restaurante('La Mer est Calme')
restaurante_2 = Restaurante('Ratatouille')

chef_1 = Chef('Raoul')
chef_2 = Chef('Abigail')
chef_3 = Chef('Fabricio')
print(f"Restaurantes de trabajo del chef {chef_1.nombre}:")
print(chef_1.listar_restaurantes_trabajo())

restaurante_1.contratar_chef(chef_1)
restaurante_1.contratar_chef(chef_2)

print("Después de ser contratado....")
print(f"Restaurantes de trabajo del chef {chef_1.nombre}:")
print(chef_1.listar_restaurantes_trabajo())

print(f"\nListo los chefs contratados en el restaurante {restaurante_1.nombre}:")
print(restaurante_1.listar_chefs())
