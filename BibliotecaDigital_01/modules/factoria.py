from modules.repositorios_concretos import RepositorioTXT

RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"

#Esta función es llamada por la aplicación de Flask para instanciar el repositorio
def crear_repositorio():
    return RepositorioTXT(ARCHIVO)