############################################################################
#primera versión usando estructura en capas persistencia-dominio-servicios
#usando lenguaje estructurado
##############################################################################
from modules.config import app
from flask import render_template, request, redirect, url_for, session
from modules.servicio import obtener_numero_libros_existentes, listar_libros_existentes, agregar_nuevo_libro

RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"

@app.route("/")
def inicio():
    session['counter'] = obtener_numero_libros_existentes(ARCHIVO)
    return render_template("inicio.html", num_libros=session['counter'])

@app.route("/listar")
def funcion_listar():    
    if session['counter'] == 0:
        return render_template("listar.html", vacio=True )
    
    lista_libros = listar_libros_existentes(ARCHIVO)
    return render_template("listar.html", mi_lista=lista_libros, vacio=False)

@app.route("/agregar", methods=["GET", "POST"])
def funcion_agregar():
    if request.method == "POST":
        # Procesamos los datos del formulario
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = float(request.form["input_calif"])
        agregar_nuevo_libro(ARCHIVO, nombre, autor, calificacion)
        # Redirigimos a la página de inicio
        return redirect(url_for("inicio"))  
    return render_template("agregar.html")


if __name__ == "__main__":
    app.run(debug=True)