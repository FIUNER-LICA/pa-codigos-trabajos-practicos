# Ejemplo de aplicación principal en Flask
from flask import render_template
from modules.config import app
from modules.servicios import listar_nombres

# from modules import servicios
# servicios.listar_nombres()

# Página de inicio
@app.route('/')
def index():
    cantidad = 20
    return render_template('inicio.html', una_cantidad=cantidad)

@app.route('/saludo')
def pagina_saludar():
    return render_template('saludo.html')

@app.route('/listar_nombres')
def pagina_listar_nombres():
    lista_nombres = listar_nombres("./data/nombres.txt")
    return render_template('lista_nombres.html',
                            nombres=lista_nombres)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)