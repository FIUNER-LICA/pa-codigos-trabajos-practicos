##############################################################################
#versión usando estructura en capas persistencia-dominio-servicios
#usando POO y base de datos SQLAlchemy
# Servicios: GestorDeLibros
# Dominio: Libro
# Persistencia: SQLAlchemyRepository
##############################################################################
from flask import render_template, request, redirect, url_for, flash, session
from modules.config import app
from modules.factoria import crear_repositorio
from modules.servicio_gestor_libros import GestorDeLibros

repo = crear_repositorio()
gestor_libros = GestorDeLibros(repo)

@app.route("/")
def inicio():     
    session['counter'] = gestor_libros.numero_libros
    return render_template("inicio.html", num_libros=session['counter'])

@app.route("/listar", methods=['GET', 'POST'])
def funcion_listar(): 
    if request.args.get('del'):
        id = request.args.get('id')
        gestor_libros.eliminar_libro_seleccionado(id)

    if session['counter'] == 0:
        return render_template("listar.html", vacio=True)    
    
    lista_libros = gestor_libros.listar_libros_existentes()
    return render_template("listar.html", mi_lista=lista_libros, vacio=False)

@app.route("/agregar", methods=['GET', 'POST'])
def funcion_agregar():
    if request.method == 'POST':
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = float(request.form["input_calif"])
        try:
            gestor_libros.agregar_nuevo_libro(nombre, autor, calificacion)
        except ValueError as e:
            flash(str(e))
        else:
            flash("Libro agregado con éxito")
    return render_template("agregar.html")

@app.route("/edit", methods=['GET', 'POST'])
def funcion_editar():
    if request.method == 'POST':
        try:
            gestor_libros.editar_libro(int(request.form['id']), 
                                       request.form['input_nombre'], 
                                       request.form['input_autor'], 
                                       float(request.form['input_calif']))
        except ValueError as e:
            flash(str(e))
        return redirect(url_for('funcion_listar')) 
    libro_a_editar = gestor_libros.devolver_libro_a_editar(request.args.get('id'))
    print(libro_a_editar)
    return render_template("editar.html", libro=libro_a_editar)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')