from flask import Flask
from flask_session import Session

app = Flask("server")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)

Session(app)