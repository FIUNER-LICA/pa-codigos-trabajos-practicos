# ClasificadorSk
Clasificador de reclamos de gestión de campus universitario utilizando ML con  sklearn en python

La idea esta proyecto es que utilicen el archivo tipo pickle "clasificador_svm.pkl" para extraer el objeto del tipo 
Clasifica y que utilicen el metodo "clasificar" el cual al pasarle una lista de reclamos (lista de string) te devuelve una lista
con las clasificaciones(tres posibles: maestranza, soporte informatico y secretaria tecnica ) de 
dichos reclamos


Aclaracion para la implementacion en windows: 
Si poseen problemas con la importacion de modulos utilizando VScode REESCRIBIR archivo sttings.json en la carpeta
oculta .vscode colocando:
{
    "python.analysis.extraPaths": ["${workspaceFolder}"],
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder};${env:PYTHONPATH}",
        "PATH": "${workspaceFolder};${env:PATH}"
    },
    "[python]": {
        "editor.defaultFormatter": "ms-python.python"
    },
    "python.formatting.provider": "none"
}


#Uso 

Si estas en windows  abre la consola de comandos, buscala como en “cmd” en el buscador y copia los siguientes comandos para instalar las librerías:

1- Instalar dependencias
 
scikit-learn:pip install -U scikit-learn  
Pickle:pip install pickle4  
nltk:https://pypi.python.org/pypi/nltk.  
Numpy(opcional):https://numpy.org/install/.  

2- Clonar repositorio.

3- En tu proyecto donde vas a utilizar el clasificador importa las bibliotecas del clasificador

4- Abre el objeto #clasificador_svm.pkl con pickle. Luego podrás utilizar el método “clasificar” el cual recibe como parámetro una lista de uno o más reclamos (cadena de caracteres)![Presentación sin título](https://github.com/SalinasSantiago/ClasificadorSk/assets/105006228/5185abd8-8450-48d3-8e80-3e5056537b1e)

