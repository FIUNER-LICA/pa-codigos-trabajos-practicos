##############################################################################
#versión usando estructura en capas persistencia-dominio-servicios
#usando POO y base de datos SQLAlchemy
# Servicios: GestorDeLibros, GestorDeUsuarios
# Dominio: Libro Usuario
# Persistencia: SQLAlchemyRepository
##############################################################################
from flask import render_template, request, redirect, url_for, flash, session
from modules.config import app, login_manager
from modules.gestor_libros import GestorDeLibros
from modules.gestor_usuarios import GestorDeUsuarios
from modules.formularios import FormRegistro, FormLogin
from modules.gestor_login import GestorDeLogin
from modules.factoria import crear_repositorio

admin_list = [1]
repo_libro, repo_usuario = crear_repositorio()
gestor_libros = GestorDeLibros(repo_libro)
gestor_usuarios = GestorDeUsuarios(repo_usuario)
gestor_login = GestorDeLogin(gestor_usuarios, login_manager, admin_list)


# Rutas
@app.route("/")
def inicio():
    if 'username' in session and gestor_login.usuario_autenticado:
        username = session['username']        
        return redirect(url_for('funcion_listar'))
    else:
        username = 'Invitado' 

    session['counter'] = gestor_libros.numero_libros
    libros_existentes = gestor_libros.listar_libros_existentes()
    return render_template("inicio.html", user=username, esta_vacia= (session['counter'] == 0), lista_libros=libros_existentes)

@app.route("/register", methods= ["GET", "POST"])
def register():
    form_registro = FormRegistro()
    if form_registro.validate_on_submit():
        try:
            gestor_usuarios.registrar_nuevo_usuario(form_registro.nombre.data, 
                                                    form_registro.email.data, 
                                                    form_registro.password.data)
        except ValueError as e:
            flash(str(e))    
        else:
            flash("Usuario registrado con éxito")
            return redirect(url_for("login"))               
    return render_template('register.html', form=form_registro)

@app.route("/login", methods= ["GET", "POST"])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        try:
            usuario = gestor_usuarios.autenticar_usuario(form_login.email.data, 
                                                         form_login.password.data)
        except ValueError as e:
            flash(str(e))
        else:
            gestor_login.login_usuario(usuario)
            session['username'] = gestor_login.nombre_usuario_actual
            return redirect(url_for('funcion_listar', username=session['username'])) 

    return render_template('login.html', form=form_login)

@app.route("/listar", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def funcion_listar(): 
    if request.args.get('del'):
        id = request.args.get('id')
        gestor_libros.eliminar_libro_seleccionado(id)  

    if gestor_login.es_admin():
        libros_existentes = gestor_libros.listar_libros_existentes()
    else:
        libros_existentes = gestor_libros.devolver_libros_segun_usuario(gestor_login.id_usuario_actual)
    
    return render_template("inicio.html", 
                           vacio= (len(libros_existentes) == 0), 
                           user=gestor_login.nombre_usuario_actual, 
                           lista_libros = libros_existentes, 
                           logged_in = gestor_login.usuario_autenticado)

@app.route("/agregar", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def funcion_agregar():
    if request.method == 'POST':
        nombre = request.form["input_nombre"]
        autor = request.form["input_autor"]
        calificacion = float(request.form["input_calif"])
        try:
            gestor_libros.agregar_nuevo_libro(nombre, autor, calificacion, gestor_login.id_usuario_actual)
        except ValueError as e:
            flash(str(e))
        else:
            flash("Libro agregado con éxito")
    return render_template("agregar.html")

@app.route("/edit", methods=['GET', 'POST'])
@gestor_login.se_requiere_login
def funcion_editar():
    if request.method == 'POST':
        try:
            gestor_libros.editar_libro(int(request.form['id']), 
                                       request.form['input_nombre'], 
                                       request.form['input_autor'], 
                                       float(request.form['input_calif']))
        except ValueError as e:
            flash(str(e))        
        else:
            flash("Libro editado con éxito")
            return redirect(url_for('funcion_listar')) 
    libro_a_editar = gestor_libros.devolver_libro(request.args.get('id'))
    return render_template("editar.html", libro=libro_a_editar)

@app.route("/logout")
def logout():    
    gestor_login.logout_usuario()      
    session['username'] = 'Invitado' 
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')