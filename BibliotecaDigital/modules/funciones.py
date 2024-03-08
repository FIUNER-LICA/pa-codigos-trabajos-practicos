def agregar_libro_a_lista(lista_libros, nombre, autor, calificacion):
    """Función que guarda la información de un libro a una lista
    de libros en forma de diccionario.
    """
    libro = {
            "nombre": nombre,
            "autor": autor,
            "calificacion": calificacion,
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

def guardar_libro_en_archivo(nombre_archivo, nombre, autor, calificacion): 
    """Guarda la información de un libro en archivo
    """   
    with open(nombre_archivo, "a") as archi:
        archi.write(f"{nombre},{autor},{calificacion}\n")