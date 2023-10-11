from modules.preprocesamiento import TextVectorizer
from modules.preprocesamiento import ProcesadorArchivo
import pickle
import numpy as np
from modules.preprocesamiento import TextVectorizer
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class Clasificador():
    """Clase que representa un clasificador de reclamos
    """
    def __init__(self, X=np.array, y=np.array, escalado=True):       
        self.X= X 
        self.y= y
        self.escalado = escalado
        self.vectorizer = TextVectorizer()
        self.word_vectors = self.__get_word_vectors()
        self.__entrenar_clasificador()

    def __get_word_vectors(self):
        #se entrena el vectorizador 
        self.vectorizer.fit(self.X)
        #el metodo "transform se encarga de trasnformar las cadenas de texto a una matriz binaria"
        return self.vectorizer.transform(self.X)

    def __entrenar_clasificador(self):
   
        X_train, X_test, y_train, y_test = train_test_split(self.word_vectors, self.y, test_size=0.2, shuffle=True, stratify=y, random_state=0)
        
        if self.escalado:
            self.sc = StandardScaler()
            X_train = self.sc.fit_transform(X_train)
            X_test = self.sc.transform(X_test)
       
        grid = {
                    'C': [0.01, 0.1, 0.5, 1, 5, 10, 15, 100], 
                    'kernel': ['rbf', 'sigmoid', 'linear', 'poly'], 
                    'gamma': [0.001, 0.01, 0.05, 0.1, 0.5, 1],
                    'degree': [2,3]
                }

        svc = SVC(random_state=42)
        grid_search = GridSearchCV(estimator=svc, param_grid=grid, cv=3, scoring="accuracy")
        grid_search.fit(X_train, y_train)
        #se guarda el mejor modelo (el de mejor desempeño)
        #por defecto el mejor modelo entrenado queda 
        #en el objeto grid_search.best_estimator_
        self.clf_best = grid_search.best_estimator_  
        print(accuracy_score(self.clf_best.predict(X_test), y_test))
        print(self.clf_best)

    def clasificar(self, texto):
        """_clasificar_
        Args:
            texto (_array_): _array de strings que contenga el/los reclamos _
        Returns:
            _array_: _retorno un array con los nombres de departamentos correspondientes a los reclamos ingresados_
        """ 
        x = self.vectorizer.transform(texto)
        if self.escalado:
            x = self.sc.transform(x)
        prediccion = self.clf_best.predict(x)
        print(prediccion)
        salida=[0] * len(prediccion) #salida tiene el mismo tamaño que los reclamos

        #'secretaría técnica': 0, 'soporte informático': 1, 'maestranza': 2
        for i in range(len(prediccion)):        
            if prediccion[i] == 0:
                salida[i] = "secretaría técnica" #tecnica
            elif prediccion[i] == 1:
                salida[i] = "soporte informático" #alumnado
            elif prediccion[i] == 2:
                salida[i]= "maestranza"         #otro
        return salida
        

if __name__== "__main__":  
    procesador = ProcesadorArchivo("frases.json")

    X, y = procesador.datosEntrenamiento
    cls=  Clasificador(X,y,escalado=True)

    text= ["No puedo enviar mi trabajo por correo electrónico porque la red no funciona.","El piso del aula 5 está muy sucio."]
    print(cls.clasificar(text))  

    # with open('./data/clasificador_svm.pkl', 'wb') as archivo:
    #     pickle.dump(cls, archivo)
    # archivo.close()