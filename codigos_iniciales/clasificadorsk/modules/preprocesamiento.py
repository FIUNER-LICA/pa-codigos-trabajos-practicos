import nltk
nltk.download("punkt")
nltk.download("stopwords")
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string
from collections import Counter
from sklearn.base import BaseEstimator, TransformerMixin
import json


class TextVectorizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.__word2idx = {}
        self.stop_words = set(stopwords.words('spanish'))
        self.spanish_stemmer = SnowballStemmer('spanish')

    # Text to Vector
    def __text_to_vector(self, texto):
        word_vector = np.zeros(len(self.vocabulario_))
        for word in texto.split(" "):
            if self.__word2idx.get(word) is None:
                continue
            else:
                word_vector[self.__word2idx.get(word)] += 1
        return np.array(word_vector)

    def fit(self, X, y=None):
      X_procesado = []
      
      for reclamo in X:
          texto = reclamo.lower()
          tokens = word_tokenize(texto)    
          X_procesado.append([self.spanish_stemmer.stem(palabra) for palabra in tokens if palabra not in self.stop_words and palabra not in string.punctuation])

      X_procesado = [str.join(' ', reclamo) for reclamo in X_procesado]

      total_counts = Counter()
      for reclamo in X_procesado:
          for word in reclamo.split(" "):
              total_counts[word] += 1
      self.vocabulario_ = [elem[0] for elem in total_counts.most_common()]
      for i, word in enumerate(self.vocabulario_):
            self.__word2idx[word] = i 

      return self
    
    def transform(self, X):
      
      word_vectors = np.zeros((len(X), len(self.vocabulario_)), dtype=np.int_)
      for i, texto in enumerate(X):
          word_vectors[i] = self.__text_to_vector(texto)

      return word_vectors


class ProcesadorArchivo():
  
  def __init__(self, direccion,):
    
    with open(direccion,'r', encoding='utf-8') as f:
      datos_entrenamiento = json.load(f)

    textos_entrenamiento = []
    etiquetas_entrenamiento = []
    
    for dato in datos_entrenamiento:
      texto = dato['reclamo']
      etiqueta = dato['etiqueta']
      textos_entrenamiento.append(texto)
      etiquetas_entrenamiento.append(etiqueta)
    
    mapeo_etiquetas = {'secretaría técnica': 0, 'soporte informático': 1, 'maestranza': 2}

    etiquetas_entrenamiento = [mapeo_etiquetas[etiqueta] for etiqueta in etiquetas_entrenamiento]
      
    #se unen todos los reclamos en un solo arreglo de nunpy
    self.x = np.array(textos_entrenamiento , dtype = object)
    #se crea un arreglo con las etiquetas (areas) correspondientes a cada reclamo
    self.y = np.array(etiquetas_entrenamiento)

  @property
  def datosEntrenamiento(self):
    return self.x,self.y

