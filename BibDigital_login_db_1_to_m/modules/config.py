from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from datetime import timedelta

app = Flask("server")

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-WTF
app.config["WTF_CSRF_ENABLED"] = False
# Flask Session
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
app.config.from_object(__name__)
Session(app)
# Bootstrap
Bootstrap(app)
# SqlAlchemy
db = SQLAlchemy(app)
# Flask Login
login_manager = LoginManager()
login_manager.init_app(app)