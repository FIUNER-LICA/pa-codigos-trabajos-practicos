from flask import render_template, request, redirect, url_for, flash, abort, session
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps
from modules.config import app, db, login_manager
from modules.models import TablaLibro, TablaUsuario
from modules.forms import LoginForm, RegisterForm, BooksForm

admin_list = [1]

with app.app_context():
    db.create_all()

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id not in admin_list:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

def is_admin():
    if current_user.is_authenticated and current_user.id in admin_list:
        return True
    else:
        return False


@login_manager.user_loader
def user_loader(user_id):
    return db.session.get(TablaUsuario, user_id)


#Muestra todos los libros de todos los usuarios
@app.route("/", methods=['GET', 'POST'])
def home():
    if 'username' in session and current_user.is_authenticated:
        username = session['username']        
        return redirect(url_for('my_books', username=username))
    else:
        username = 'Invitado' 
        print("username:", username)

    lista_libros = TablaLibro.query.all()
    if len(lista_libros) == 0:
        return render_template("home.html", user=username, esta_vacia=True)
    
    return render_template("home.html", user=username, esta_vacia=False, lista_libros=lista_libros )
    
@app.route("/my_books/<username>", methods=['GET', 'POST'])
@login_required
def my_books(username):

    if request.args.get('del'):
        id = request.args.get('id')
        libro_a_eliminar = db.session.get(TablaLibro,id)
        db.session.delete(libro_a_eliminar)
        db.session.commit()

    if is_admin():
        lista_libros = TablaLibro.query.all()
    else:
        lista_libros = TablaLibro.query.filter_by(id_usuario=current_user.id).all()

    if len(lista_libros) == 0:
        return render_template(
                                "home.html", esta_vacia=True, user=username, 
                                logged_in=current_user.is_authenticated
                              )

    return render_template(
                                "home.html", esta_vacia=False, 
                                user=username, lista_libros=lista_libros,
                                logged_in=current_user.is_authenticated 
                            )
    

@app.route("/login", methods= ["GET", "POST"])
def login():
    login_form = LoginForm()
    # Acceso a la información ingresada en el formulario
    # cuando el usuario realiza el "submit".
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        #hacemos una consulta filtrando por email para
        #saber si hay un usuario registrado con ese email
        user = TablaUsuario.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again")
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
        else:
            login_user(user)
            print(current_user)
            session['username'] = user.name
            return redirect(url_for('my_books', username=user.name))        
    return render_template('login.html', form=login_form)

@app.route("/register", methods= ["GET", "POST"])
def register():
    register_form = RegisterForm()
    # Acceso a la información ingresada en el formulario
    # cuando el usuario realiza el "submit".
    if register_form.validate_on_submit():
        # Verifico que no exista usuario con igual email
        if TablaUsuario.query.filter_by(email=register_form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        # Si el registro es corecto, se crea un nuevo usuario en la db
        encripted_pass = generate_password_hash(
            password= register_form.password.data,
            method= 'pbkdf2:sha256',
            salt_length=8
        )
        new_user = TablaUsuario(
            email = register_form.email.data,
            password = encripted_pass,
            name = register_form.username.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=register_form)


@app.route("/agregar", methods=['GET', 'POST'])
@login_required
def agregar():
    add_form = BooksForm()
    if request.method == 'POST':
        if TablaLibro.query.filter_by(nombre= add_form.nombre.data).first() == None:
            libro = TablaLibro(
                nombre = add_form.nombre.data,
                autor = add_form.autor.data,
                calificacion = float(add_form.calificacion.data),
                id_usuario = current_user.id
            )
            db.session.add(libro)
            db.session.commit()
        else:
            flash("El libro ya está agregado a la biblioteca")
        return redirect(url_for('my_books', username=current_user.name))
    return render_template("agregar.html", form=add_form)

@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    edit_form = BooksForm()
    if edit_form.validate_on_submit():
        id = edit_form.id.data
        print("id:", id)
        libro_a_editar = db.session.get(TablaLibro,id)
        libro_a_editar.nombre = edit_form.nombre.data
        libro_a_editar.autor = edit_form.autor.data
        libro_a_editar.calificacion = float(edit_form.calificacion.data)
        db.session.commit()
        return redirect(url_for('my_books', username=current_user.name))       
    id = request.args.get('id')
    libro_a_editar = db.session.get(TablaLibro,id) 
    
    return render_template("edit.html", libro=libro_a_editar, e_form=edit_form)

@app.route("/logout")
def logout():   
    print(current_user)  
    logout_user()      
    print(current_user)
    session['username'] = 'Invitado' 
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')