from flask import render_template, request, redirect, url_for, flash
from modules.config import app, db
from modules.models import TablaLibro
from flask import session

# operaciones sobre las tablas
# TablaLibro.query.all() 
# db.session.get(TablaLibro,id) -> filtrar por primary key
# TablaLibro.query.filter_by( nombre="...").first() -> filtrar usando una columna de la tabla
# TablaLibro.query.filter( TablaLibro.nombre == "..." and TablaLibro.autor == "...").first() -> filtrar usando expresión lógica
# TablaLibro.query.order_by(TablaLibro.nombre).all() -> ordenar por nombre del libro
# db.session.add(...)
# db.session.delete(...)
# db.session.commit()

#3) Se llama a db.create_all() dentro del contexto de la aplicación en Flask para 
#asegurar que se pueda acceder correctamente a la base de datos y para garantizar
#la integridad de las transacciones en la base de datos.
with app.app_context(): 
    db.create_all()

@app.route("/")
def inicio():        
    return render_template("inicio.html")

@app.route("/listar", methods=['GET', 'POST'])
def funcion_listar(): 
    #8) agregamos el código correspondiente al delete   
    if request.args.get('del'):
        id = request.args.get('id')
        libro_a_eliminar = db.session.get(TablaLibro,id)
        db.session.delete(libro_a_eliminar)
        db.session.commit()
        
    #5)Se consulta por todos los libros en la tabla de libros 
    print(TablaLibro.query.all()) 
    session['num_libros'] = len(TablaLibro.query.all())    
    if session['num_libros'] == 0:
        return render_template("listar.html", esta_vacia=True)
    
    return render_template("listar.html", esta_vacia=False,\
                           lista_libros = TablaLibro.query.all(),\
                              num_libros=session['num_libros'])

@app.route("/agregar", methods=['GET', 'POST'])
def funcion_agregar():
    if request.method == 'POST':
        #4)Creamos los primeros libros en nuestra base de datos
        # para evitar el error de sqlalchemy si ingresamos un libro con nombre existente
        # nos fijamos si ese nombre existe en la base de datos
        if TablaLibro.query.filter_by(nombre=request.form["input_nombre"]).first() == None:
            libro = TablaLibro(
                nombre = request.form["input_nombre"],
                autor = request.form["input_autor"],
                calificacion = float(request.form["input_calif"])
            )
            db.session.add(libro)
            db.session.commit()
            #db.session es una instancia de la sesión de la base de datos
            #se encarga de administrar la comunicación con la base de datos
            print(TablaLibro.query.all())
            session['num_libros'] = len(TablaLibro.query.all())  
        else:
            #agregar secret key https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/
            flash("El libro ya está agregado a la biblioteca")

    return render_template("agregar.html", num_libros=session['num_libros'])

# 7) agregamos la ruta para editar
@app.route("/edit", methods=['GET', 'POST'])
def funcion_editar():
    if request.method == 'POST':
        id = request.form['id']
        print(id)
        libro_a_editar = db.session.get(TablaLibro,id) 
        libro_a_editar.nombre = request.form["input_nombre"]
        libro_a_editar.autor = request.form["input_autor"]
        libro_a_editar.calificacion = float(request.form["input_calif"])
        db.session.commit()
        return redirect(url_for('funcion_listar'))   
    #acceder a los datos enviados desde html. La cadena de consulta es la parte
    #de la URL que sigue al signo de interrogación    
    id = request.args.get('id')
    libro_a_editar = db.session.get(TablaLibro,id)
    print(f"id: {id}") 
    return render_template("editar.html", libro=libro_a_editar)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')