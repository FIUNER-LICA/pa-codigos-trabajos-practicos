##############################################################################
#versión usando estructura en capas persistencia-dominio-servicios
#usando POO
##############################################################################
from modules.config import app
from flask import render_template, request, redirect, url_for, session

# from modules.persistencia import GestorArchivosTXT ##Estas importaciones ya no son necesarias
# from modules.persistencia import GestorArchivosCSV ##tampoco el módulo persistencia que se reemplazó
                                                     ##por los repositorios

from modules.servicio import GestorDeLibros
from modules.factoria import crear_repositorio


repositorio = crear_repositorio()
gestor_libros = GestorDeLibros(repositorio)

## Esto pasó a factoria.py
# RUTA = "./data/"
# ARCHIVO = RUTA + "libros_leidos.csv"

# ARCHIVO = RUTA + "libros_leidos.txt"
##Esto ya no es necesario porque se creó la factoría y
##se usa el método crear_repositorio() para instanciar el repositorio

# gestor_archivo_csv = GestorArchivosCSV(ARCHIVO)
# gestor_libros = GestorDeLibros(gestor_archivo_csv)
# gestor_archivo_txt = GestorArchivosTXT(ARCHIVO)
# gestor_libros = GestorDeLibros(gestor_archivo_txt)

@app.route("/")
def inicio():
    session['counter'] = gestor_libros.numero_libros
    return render_template("inicio.html", num_libros=session['counter'])

@app.route("/listar")
def funcion_listar():    
    if session['counter'] == 0:
        return render_template("listar.html", vacio=True )
    lista_dicc_libros = gestor_libros.listar_libros_existentes()
    return render_template("listar.html", mi_lista=lista_dicc_libros, vacio=False)

@app.route("/agregar", methods=["GET", "POST"])
def funcion_agregar():
    if request.method == "POST":
        # Procesamos los datos del formulario
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = float(request.form["input_calif"])
        gestor_libros.agregar_nuevo_libro(nombre, autor, calificacion)
        # Redirigimos a la página de inicio
        return redirect(url_for("inicio"))  
    return render_template("agregar.html")


if __name__ == "__main__":
    app.run(debug=True)











