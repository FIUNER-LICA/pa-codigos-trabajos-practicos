# Ejemplo de aplicación principal en Flask
from flask import render_template
from modules.config import app

# Página de inicio
@app.route('/')
def index():
    cantidad = 20
    return render_template('inicio.html', una_cantidad=cantidad)

@app.route('/saludo')
def funcion_saludar():
    return render_template('saludo.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)