# Ejemplo de aplicación principal en Flask
from flask import render_template, request, redirect, url_for, flash, session
from modules.config import app
from modules.servicios import listar_nombres


# from modules import servicios
# servicios.listar_nombres()


# Página de inicio
@app.route('/', methods=['GET', 'POST'])
def index():
    cantidad = 20
    if request.method == 'GET':
        return render_template('inicio.html', una_cantidad=cantidad)
    elif request.method == 'POST':
        if request.form['name_nro_iteraciones']: # se cargó el número de iteraciones
            session['nro_iteraciones'] = int(request.form['name_nro_iteraciones'])
            return redirect(url_for('pagina_bucle'))
        else:
            flash('No se ha cargado correctamente el número de iteraciones')
            return render_template('inicio.html', una_cantidad=cantidad)


@app.route('/bucle', methods=['GET', 'POST'])
def pagina_bucle():
    # se controlan iteraciones
    if request.method == 'GET': # se llega a esta página por 1ra vez desde inicio (iteracion 1)
        session['iteracion'] = 1
    elif request.method == 'POST':
        session['iteracion'] = session['iteracion'] + 1  # se incrementa el contador de iteraciones    
    
    # se renderiza html correspondiente o se redirije si se terminó de iterar
    if session['iteracion'] <= session['nro_iteraciones']:
        # Ejemplo de un texto leido de la propia página y reenviado a la misma página.
        texto = None
        if request.method == 'POST':
            if request.form['texto']:
                texto = request.form['texto']

        return render_template('bucle.html',
                        nro_iteraciones = session['nro_iteraciones'],
                        iteracion = session['iteracion'],
                        texto = texto)
    else:  # se ha iterado el número de veces requerido y se redirige el inicio
        return redirect(url_for('index'))


@app.route('/saludo')
def funcion_saludar():
    return render_template('saludo.html')


@app.route('/listar_nombres')
def pagina_listar_nombres():
    lista_nombres = listar_nombres("./data/nombres.txt")
    return render_template('lista_nombres.html',
                            nombres=lista_nombres)
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)