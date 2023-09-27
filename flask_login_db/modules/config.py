from flask import Flask
from flask_bootstrap import Bootstrap #1) https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# Flask
app = Flask("server")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Flask-WTF
app.config["WTF_CSRF_ENABLED"] = False
# Por defecto, Flask-WTF habilita la protección CSRF de forma automática. 
# Cuando esta protección está habilitada, cada formulario generado con Flask-WTF 
# incluirá un token CSRF único que se espera que el navegador incluya en cada solicitud POST. 
# Si el token CSRF no coincide con el servidor, la solicitud POST se considera potencialmente
# maliciosa y se rechaza.

# SqlAlchemy
db = SQLAlchemy(app)

# Flask Session
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# 1) Bootstrap
Bootstrap(app)

# 4) Flask Login
login_manager = LoginManager()
login_manager.init_app(app)