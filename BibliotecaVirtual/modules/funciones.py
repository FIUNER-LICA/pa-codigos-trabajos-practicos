

def agregar_libro_a_lista(lista_libros:list, nombre:str, autor:str, puntaje:float):
    """Función que guarda la información de un libro a una lista
    de libros en forma de diccionario.
    """
    libro = {
            "nombre": nombre,
            "autor": autor,
            "puntaje": puntaje,
        }
    lista_libros.append(libro) 

def cargar_lista_desde_archivo(nombre_archivo, lista_libros):
    """Función que lee la información de los libros desde un archivo
    y lo carga a una lista.
    """
    with open(nombre_archivo, "r") as archi:
        for linea in archi:
            libro = linea.rstrip().split(',')
            agregar_libro_a_lista(lista_libros, libro[0], libro[1], libro[2]) 

def guardar_lista_en_archivo(nombre_archivo, lista_libros):  
    """Función que guarda en un archivo la información de los libros 
    almacenados en la lista.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archi:                
        for libro in lista_libros:
            archi.write(f"{libro['nombre']},{libro['autor']},{libro['puntaje']}\n")