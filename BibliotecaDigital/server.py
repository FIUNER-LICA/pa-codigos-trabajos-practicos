# Aplicación principal
from flask import render_template, request, redirect, url_for, session
from modules.config import app
from modules.funciones import cargar_lista_desde_archivo, guardar_libro_en_archivo, agregar_libro_a_lista


RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"
lista_libros = [] #lista auxiliar

try:
    cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass

@app.route("/")
def inicio():    
    session['contador'] = len(lista_libros)
    return render_template("inicio.html")

@app.route("/listar")
def funcion_listar():
    
    if len(lista_libros) == 0:
        return render_template("listar.html", vacio=True )
    return render_template("listar.html", mi_lista = lista_libros, vacio=False, num_libros=session['contador'])

@app.route("/agregar", methods=["GET", "POST"])
def funcion_agregar():   
    if request.method == "POST":
        # Procesamos los datos del formulario
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = request.form["input_calif"]
        # Guardamos los datos en el archivo
        guardar_libro_en_archivo(ARCHIVO, nombre, autor, calificacion)
        # Agregamos el libro a la lista
        agregar_libro_a_lista(lista_libros, nombre, autor, calificacion)
        #Opcional si queremos redirigimos a la página de inicio
        #return redirect(url_for("inicio")) 
    
    return render_template("agregar.html", num_libros=session['contador'])

if __name__ == "__main__":
    app.run(debug=True)