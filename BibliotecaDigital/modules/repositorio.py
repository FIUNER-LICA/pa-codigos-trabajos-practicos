from modules.dominio import crear_libro

def guardar_libro(nombre_archivo, libro):   
    with open(nombre_archivo, "a") as archi:
        archi.write(f"{libro['nombre']},{libro['autor']},{libro['calificacion']}\n")


def obtener_libros(nombre_archivo):
    """Función que lee la información de los libros desde un archivo
    y retorna una lista de libros con formato de diccionario.
    """
    lista_libros = []
    # Si el archivo no existe, se crea uno vacío 
    try: 
        with open(nombre_archivo, "r") as archi:
            for linea in archi:
                nombre, autor, calificacion = linea.rstrip().split(',')
                libro = crear_libro(nombre, autor, float(calificacion))
                lista_libros.append(libro)
    except FileNotFoundError:
        with open(nombre_archivo, "w") as archi:
            pass

    return lista_libros
