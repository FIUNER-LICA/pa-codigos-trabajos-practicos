from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from modules.config import app, db, login_manager
from modules.models import TablaLibro, TablaUsuario
from modules.forms import LoginForm, RegisterForm, BooksForm


with app.app_context():
    db.create_all()

@login_manager.user_loader
def user_loader(user_id):
    return db.session.get(TablaUsuario, user_id)

@app.route("/", methods=['GET', 'POST'])
def home():    
    if 'username' in session and current_user.is_authenticated:
        username = session['username']
        return redirect(url_for('my_books', username=username))
    else:
        username = 'Invitado' 

    lista_libros = TablaLibro.query.all()
    if len(lista_libros) == 0:
        return render_template("home.html", user=username, esta_vacia=True)
    else:
        return render_template("home.html", user=username, esta_vacia=False, lista_libros=lista_libros )
    
@app.route("/my_books/<username>", methods=['GET', 'POST'])
@login_required
def my_books(username):   

    libros_usuario = current_user.libros_seguidos
    print("libros: ", libros_usuario)
    todos_los_libros = TablaLibro.query.all() 

    if request.args.get('del'):
        id = request.args.get('id')
        libro_a_eliminar = db.session.get(TablaLibro,id)
        db.session.delete(libro_a_eliminar)
        db.session.commit()    
        libros_usuario = current_user.libros_seguidos        
        todos_los_libros = TablaLibro.query.all()
        return render_template(
                                    "home.html", esta_vacia=False, lista_libros=todos_los_libros, libros_seguidos=libros_usuario,
                                    user=username, logged_in=current_user.is_authenticated, all=True 
                                )

    if request.args.get('all') == 'True': 
        todos_los_libros = TablaLibro.query.all() 
        libros_usuario = current_user.libros_seguidos
        return render_template(
                                    "home.html", esta_vacia=False, lista_libros=todos_los_libros, libros_seguidos=libros_usuario,
                                    user=username, logged_in=current_user.is_authenticated, all=True 
                              )
    
    if request.args.get('seguir') == 'True':
        id = request.args.get('id')
        libro_a_seguir = db.session.get(TablaLibro,id)

        # muestro los usuarios que siguen al libro antes de agregar el usuario actual
        print("usuarios: ", libro_a_seguir.usuarios_seguidores)

        current_user.libros_seguidos.append(libro_a_seguir)

        # muestro los usuarios que siguen al libro después de agregar el usuario actual
        print("usuarios: ", libro_a_seguir.usuarios_seguidores)
        db.session.commit()
        return redirect(url_for('my_books', username=current_user.name, all=True))
    # Agrego la opción de dejar de seguir un libro
    if request.args.get('seguir') == 'False':
        id = request.args.get('id')
        libro_seguido = db.session.get(TablaLibro,id)
        current_user.libros_seguidos.remove(libro_seguido)
        db.session.commit()
        return redirect(url_for('my_books', username=current_user.name, all=True))

    if len(libros_usuario) == 0:
        return render_template(
                                "home.html", esta_vacia=True, user=username, 
                                logged_in=current_user.is_authenticated  
                              )
    
    return render_template(
                                "home.html", esta_vacia=False, lista_libros=libros_usuario, libros_seguidos=libros_usuario,
                                user=username, logged_in=current_user.is_authenticated, all=False 
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
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
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
            current_user.libros_seguidos.append(libro)
            db.session.commit()
        else:
            flash("El libro ya está agregado a la biblioteca")
        return redirect(url_for('my_books', username=current_user.name))
    return render_template("agregar.html", form=add_form)


@app.route("/logout")
def logout():   
    print(current_user)  
    logout_user()      
    print(current_user)
    session['username'] = 'Invitado' 
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')