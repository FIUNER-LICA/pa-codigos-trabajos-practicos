from flask import Flask
from flask_session import Session   # sessiones del lado del servidor

app = Flask("server")

app.config["SESSION_PERMANENT"] = False     # Las sesiones terminarán al cerrar el navegador
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)