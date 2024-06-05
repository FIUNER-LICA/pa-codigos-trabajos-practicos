import pickle

# Abrir el archivo con el clasificador y guardarlo en la variable clf
with open('./data/claims_clf.pkl', 'rb') as archivo:
  clf  = pickle.load(archivo)

# Ahora en clf tenemos el clasificador entrenado

reclamos = [
    "La computadora 1 del laboratorio 3 no enciende", 
    "El proyector del aula 2 no proyecta la imagen", 
    "El piso del aula 5 está muy sucio", 
    "No puedo enviar mi trabajo por correo electrónico porque la red no funciona",
    "El pizarrón del aula 4 está roto",
    "La impresora de la biblioteca no imprime",
    "El aire acondicionado del aula 1 no enfría",
    "El baño de la planta baja está inundado",
]

# Clasificar los reclamos
print(clf.clasificar(reclamos))

# Clasificar único reclamo
print(clf.clasificar(["El proyector del aula 2 no proyecta la imagen"]))