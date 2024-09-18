from modules.repositorios_concretos import RepositorioTXT
from modules.repositorios_concretos import RepositorioCSV

RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"

#Esta función es llamada por la aplicación de Flask para instanciar el repositorio
def crear_repositorio():
    return RepositorioTXT(ARCHIVO)
    # return RepositorioCSV(ARCHIVO)