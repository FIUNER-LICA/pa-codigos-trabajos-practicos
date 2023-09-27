from modules.config import db
from flask_login import UserMixin

# 4)Flask login requiere un modelo de usuario con las siguientes propiedades implementadas 
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()
# Flask login provee la clase UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(1000))