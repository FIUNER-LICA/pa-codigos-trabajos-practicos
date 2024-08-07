
def crear_libro(nombre, autor, calificacion):
    """Crea un diccionario con la información de un libro.
    pre: nombre y autor son cadenas de texto no vacías, calificación es un número entre 0 y 10.
    pos: devuelve un diccionario con la información del libro.
    """
    if not isinstance(nombre,str) or not isinstance(autor,str):
        raise ValueError("El nombre y autor del libro deben ser cadenas de texto")
    if nombre.strip() == "" or autor.strip() == "": # if not nombre.strip() or not autor.strip():
        raise ValueError("El nombre y autor del libro no pueden estar vacíos")
    if not isinstance(calificacion, (int,float)):
        raise ValueError("La calificación del libro debe ser un número")
    if calificacion < 0 or calificacion > 10: # if not (0 <= calificacion <= 10):
        raise ValueError("La calificación del libro debe ser un número en el rango de 0 a 10")
    libro = {
        "nombre": nombre,
        "autor": autor,
        "calificacion": calificacion
    }
    return libro

if __name__=="__main__":
    libro = crear_libro("1984","George Orwell", 10)
    print(libro)    