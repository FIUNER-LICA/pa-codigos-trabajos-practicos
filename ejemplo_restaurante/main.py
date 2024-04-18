from modules.chef import Chef
from modules.restaurante import Restaurante

chef_1 = Chef('Raoul')
chef_2 = Chef('Abigail')
chef_3 = Chef('Fabricio')

restaurante_1 = Restaurante('La Mer est Calme')
restaurante_2 = Restaurante('Ratatouille')

# 
print(f"Restaurantes de trabajo del chef {chef_1.nombre}:")
chef_1.listar_restaurantes_trabajo()

restaurante_1.contratar_chef(chef_1)
restaurante_2.contratar_chef(chef_1)

print("Después de ser contratado....")
print(f"Restaurantes de trabajo del chef {chef_1.nombre}:")
chef_1.listar_restaurantes_trabajo()

print(f"\nListo los chefs contratados en el restaurante {restaurante_1.nombre}:")
restaurante_1.listar_chefs()
