# Claims Classifier

Clasificador para Sistema de Gestión de Reclamos en la facultad

El objetivo de este proyecto es proveer un clasificador de reclamos entrenado guardado en el archivo pickle "claims_clf.pkl".

### Dependencias necesarias

- [Scikit-learn](https://scikit-learn.org/stable/index.html): `pip install -U scikit-learn` 
- [nltk](https://pypi.python.org/pypi/nltk): `pip install nltk`  
- [Numpy](https://numpy.org/doc/stable/index.html):`pip install numpy`

### Pasos para usar el clasificador 

1- Clonar el repositorio.

2- Instalar las dependencias necesarias en el proyecto donde utilizarás el clasificador

2- Copiar los archivos `text_vectorizer.py` y `classifier.py` en la carpeta `modules`de tu proyecto y el archivo `claims_clf.pkl` en la carpeta `data`. 

4- Para cargar el clasificador desde el archivo y empezar a clasificar tus reclamos, seguir el siguiente ejemplo:

```
import pickle

with open('./data/claims_clf.pkl', 'rb') as archivo:
  clf  = pickle.load(archivo)
```
Al cargar el clasificador desde el archivo, el mismo queda guardado en la variable `clf`, para utilizarlo, simplemente llamar al método clasificar.

```
reclamos = [
    "La computadora 1 del laboratorio 3 no enciende", 
    "El proyector del aula 2 no proyecta la imagen"
]
clf.clasificar(reclamos)
```
Tener en cuenta que el método `clasificar()` recibe como parámetro una lista de reclamos (lista de strings).
Las etiquetas que devuelve este clasificador son: `soporte informático`, `secretaría técnica` y `maestranza`.

Ver el ejemplo `eval_claims_clf.py` en la carpeta `apps` para probar el uso del clasificador.
