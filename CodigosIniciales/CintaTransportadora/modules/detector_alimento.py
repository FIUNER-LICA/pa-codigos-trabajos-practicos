import numpy as np
import random
import matplotlib.pyplot as plt

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.__alimentos = ["kiwi", "manzana", "papa", "zanahoria", "undefined"]
        self.__peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2)
        self.__prob_pesos = np.round(self.__softmax(self.__peso_alimentos)[::-1], 2)

    def __softmax(self, x):
        """función softmax para crear vector de probabilidades 
        que sumen 1 en total
        """
        return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

    def detectar_alimento(self):
        """método que simula la detección del alimento y devuelve un diccionario
        con la información del tipo y el peso del alimento.
        """
        n_alimentos = len(self.__alimentos)
        alimento_detectado = self.__alimentos[random.randint(0, n_alimentos-1)]
        peso_detectado = random.choices(self.__peso_alimentos, self.__prob_pesos)[0]
        return {"alimento": alimento_detectado, "peso": peso_detectado}
    

if __name__ == "__main__":
    random.seed(1)
    sensor = DetectorAlimento()
    lista_pesos = []
    
    print("Salida de dos detecciones:")
    print(sensor.detectar_alimento())
    print(sensor.detectar_alimento())
    print()

    for _ in range(200):
        lista_pesos.append(sensor.detectar_alimento()["peso"])

    print("Primeros 10 pesos detectados:")
    print(lista_pesos[0:10])

    plt.hist(lista_pesos, bins=12)
    plt.show()