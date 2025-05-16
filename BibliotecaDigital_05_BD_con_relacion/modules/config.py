from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import datetime

app = Flask("server")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

URL_BD = 'sqlite:///data/base_datos.db'

def crear_engine():
    engine = create_engine(URL_BD)
    Session = sessionmaker(bind=engine)
    return Session

app.config.from_object(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=5)
Session(app)

# Flask Login
login_manager = LoginManager()
login_manager.init_app(app)
# Bootstrap
Bootstrap(app)