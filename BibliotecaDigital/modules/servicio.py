"""La capa de servicio maneja los casos de uso (las acciones que el usuario puede realizar) de la aplicación.
Coordina la interacción entre la capa de dominio y la de persistencia. 
La aplicación implementada con cualquier interfaz de usuario (web o consola) debe comunicarse solo con 
la capa de servicio es decir, solo hacer llamadas a funciones de esta capa.
"""

from modules.persistencia import guardar_libro, obtener_libros
from modules.dominio import crear_libro


def obtener_numero_libros_existentes(ruta_archivo):
    lista_libros = obtener_libros(ruta_archivo)
    return len(lista_libros)

def listar_libros_existentes(ruta_archivo):
    return obtener_libros(ruta_archivo)

def agregar_nuevo_libro(ruta_archivo, nombre, autor, calificacion):
    libro = crear_libro(nombre, autor, calificacion)
    guardar_libro(ruta_archivo, libro)
    
