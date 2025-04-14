from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask("server")

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Configuración de la sesión que me permite interactuar con la base de datos

URL_BD = 'sqlite:///data/base_datos.db'

def crear_engine():
    engine = create_engine(URL_BD)
    Session = sessionmaker(bind=engine)
    return Session


SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
Session(app)