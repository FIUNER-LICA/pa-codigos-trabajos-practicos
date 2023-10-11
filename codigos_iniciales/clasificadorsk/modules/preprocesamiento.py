import nltk
# Instalar estos paquetes si no están instalados
# nltk.download("punkt")
# nltk.download("stopwords")
import logging
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string
from collections import Counter
from sklearn.base import BaseEstimator, TransformerMixin
import json


class TextVectorizer(BaseEstimator, TransformerMixin):
  """Clase que representa un transformador de texto a vector
  Hereda de BaseEstimator y TransformerMixin para poder 
  ser usado en un pipeline de sklearn
  """
  def __init__(self):
    self.__word2idx = {}
    self.stop_words = set(stopwords.words('spanish'))
    self.spanish_stemmer = SnowballStemmer('spanish')

  # Text to Vector
  def __text_to_vector(self, texto):
    """Función que utiliza el diccionario word2idx para transformar
    un texto en un vector de frecuencias de palabras
    """
    word_vector = np.zeros(len(self.vocabulario_))
    for word in texto.split(" "):
        if self.__word2idx.get(word) is None:
            continue
        else:
            word_vector[self.__word2idx.get(word)] += 1
    return np.array(word_vector)

  def fit(self, X, y=None):
    """función que entrena el vectorizador de texto
    para obtener el vocabulario y el diccionario word2idx
    """
    X_procesado = []
    
    for reclamo in X:
        texto = reclamo.lower()
        tokens = word_tokenize(texto)    
        X_procesado.append( [self.spanish_stemmer.stem(palabra) for palabra in tokens \
                            if palabra not in self.stop_words and \
                              palabra not in string.punctuation] )

    X_procesado = [str.join(' ', reclamo_procesado) for reclamo_procesado in X_procesado]
    
    # logging.info(f"X_procesado: {X_procesado}")
    
    total_counts = Counter()
    for reclamo_procesado in X_procesado:
        for word in reclamo_procesado.split(" "):
            total_counts[word] += 1
    # total_counts registra cuantas veces aparece cada palabra en el texto
    logging.info(f"total_counts: {total_counts}")

    self.vocabulario_ = [elem[0] for elem in total_counts.most_common()]
    # vocabulario es una lista de las palabras que aparecen en el texto 
    # ordenadas de mayor a menor frecuencia
    logging.info(f"vocabulario: {self.vocabulario_}") 
    
    for i, word in enumerate(self.vocabulario_):
          self.__word2idx[word] = i 
    # word2idx es un diccionario que asocia cada palabra con un indice
    return self
    
  def transform(self, X):    
    word_vectors = np.zeros((len(X), len(self.vocabulario_)), dtype=np.int_)
    for i, texto in enumerate(X):
        word_vectors[i] = self.__text_to_vector(texto)
    return word_vectors


class ProcesadorArchivo():
  """Clase que representa un procesador de archivos json"""

  def __init__(self, direccion,):
    
    with open(direccion,'r', encoding='utf-8') as f:
      datos_entrenamiento = json.load(f)

    textos_entrenamiento = []
    etiquetas_entrenamiento = []
    
    for dato in datos_entrenamiento:
      textos_entrenamiento.append(dato['reclamo'])
      etiquetas_entrenamiento.append(dato['etiqueta'])
    
    mapeo_etiquetas = {'secretaría técnica': 0, 'soporte informático': 1, 'maestranza': 2}

    etiquetas_entrenamiento = [mapeo_etiquetas[etiqueta] for etiqueta in etiquetas_entrenamiento]
      
    #se unen todos los reclamos en un solo arreglo de nunpy
    self.x = np.array(textos_entrenamiento , dtype = object)
    #se crea un arreglo con las etiquetas (areas) correspondientes a cada reclamo
    self.y = np.array(etiquetas_entrenamiento)

  @property
  def datosEntrenamiento(self):
    return self.x, self.y


if __name__== "__main__":
   
  # logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
  vectorizer = TextVectorizer()
  procesador = ProcesadorArchivo("frases.json")
  X, y = procesador.datosEntrenamiento

  vectorizer.fit(X)
  print(type(vectorizer.transform(X)))
  