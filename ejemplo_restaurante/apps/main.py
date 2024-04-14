
from modules.agentes_de_cocina import Chef, AuxiliarCocina
from modules.espacios_restaurante import Restaurante

restaurante_1 = Restaurante('La Mer est Calme')
restaurante_2 = Restaurante('Ratatouille')

chef_1 = Chef('Raoul')
auxiliar_1 = AuxiliarCocina('Giussepe') 
chef_2 = Chef('Abigail')
auxiliar_2 = AuxiliarCocina('Joseph')

restaurante_1.contratar_personal(chef_1)
restaurante_1.contratar_personal(chef_2)
restaurante_1.contratar_personal(auxiliar_1)
restaurante_1.contratar_personal(auxiliar_2)

restaurante_2.contratar_personal(chef_1)
restaurante_2.asignar_chef_ejecutivo(chef_2)

# chef_1.anotarse_restaurante(restaurante_1)
# chef_2.anotarse_restaurante(restaurante_1)
# auxiliar_1.anotarse_restaurante(restaurante_1)
# auxiliar_2.anotarse_restaurante(restaurante_1)

print(f"Auxiliares del restaurante {restaurante_1.nombre}:")
restaurante_1.listar_auxiliares()
print(f"\nChefs del restaurante {restaurante_1.nombre}:")
restaurante_1.listar_chefs()