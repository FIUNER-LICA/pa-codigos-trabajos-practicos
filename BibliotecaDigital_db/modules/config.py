from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask("server")

#1) Escribimos las configuraciones necesarias para crear nuestra base de datos SQLite
#variable de configuración en Flask-SQLAlchemy que se utiliza para indicar la ubicación y 
#las credenciales de la base de datos que se utilizará en la aplicación.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_datos.db'

#rastrea todas las modificaciones que se realizan en los modelos de la aplicación, 
#incluyendo la creación, actualización y eliminación de objetos de la base de datos
#el seguimiento de las modificaciones puede tener un costo en el rendimiento de la aplicación
#por eso lo seteamos en False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#crea una instancia de la clase SQLAlchemy en la aplicación flask, permite
#que la aplicación interactúe con la base de datos
db = SQLAlchemy(app)

#La clave secreta se utiliza para evitar que terceros malintencionados accedan a los datos
#confidenciales de la aplicación, como las credenciales de usuario y las sesiones de usuario. 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
Session(app)