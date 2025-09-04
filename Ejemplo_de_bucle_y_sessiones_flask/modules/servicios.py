# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

def listar_nombres(nombre: str) -> list[str]:
    resultado = []
    # codificar lectura desde archivo
    resultado.append("Carlos")
    resultado.append("Mariela")
    resultado.append("Agustín")
    return resultado

if __name__ == '__main__':
    lista = listar_nombres("./data/archivo_de_prueba.txt")
    print(lista)