# Dependencias del proyecto

Carpeta para registrar los módulos que necesiten ser instalados para que nuestro proyecto sea reproducible.

# Uso de entornos virtuales

Un "Entorno" en Python es el contexto en el que se ejecuta un programa de Python que consta de un intérprete y una cantidad de paquetes instalados.

## Entorno global:
Por defecto, cualquier intérprete de Python instalado se ejecuta en su propio entorno global. Por ejemplo, si se ejecuta el comando python o python3 en alguna terminal (dependiendo de cómo se haya instalado Python), se estaría ejecutando en el entorno global de ese intérprete. Cualquier paquete que se instale o desinstale afecta el entorno global y por tanto todos los programas que se ejecutan en él.

En Python, es una buena práctica crear un entorno específico de un espacio de trabajo o entorno virtual local.

## Entorno virtual local:
Este tipo de entorno te permite instalar módulos de python sin afectar otros entornos aislando la instalación de los módulos del espacio de trabajo. 

## Creación de entorno virtual local en VSCode

- Abrir la paleta de comandos, __Command Palette__ (`Ctrl+Shift+P`). Buscar y seleccionar el comando **Python: Create Environment**

![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/fc049bfd-75ee-47fb-845f-fec47f9b245b)

- Una vez seleccionado el comando, se presenta una lista de tipos de entornos: **Venv** o **Conda**
 
![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/138d7966-d259-4d26-a69a-de6d4f2cbb5c)

- Seleccionar el tipo de entorno **Venv**, el comando presenta una lista de los intérpretes disponibles que pueden utilizarse como base para el nuevo entorno virtual

![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/4ea200f3-f2dd-4395-9112-3fa6c31a6e95)

- Luego de seleccionar el intérprete, se mostrará una notificación con el progreso de la creación de la carpeta del entorno

![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/b3671f70-d54e-4a38-85e3-7befe227c86b)

- Una vez creado nuestro entorno virtual, el mismo debe ser activado usando el siguiente comando en la terminal de VSCode:
  `& .venv\Scripts\Activate.ps1`

### ⚠️ 
En Windows al ejecutar el comando anterior nos puede aparecer el mensaje:
"File D:\ProgAvanzadaPython\Ejercicios\TrabajoPractico_1\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. 
For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170." 
En este caso es necesario ingresar el siguiente comando en la terminal: 

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

- Al ejecutar los comandos anteriores, aparece la etiqueta (.venv) en la entrada de comando indicando que se activó el entorno:
  
![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/5bc9e8c4-8b32-4ff1-9dcb-343e3472f1e7)

- Una vez activado nuestro entorno, podemos instalar los módulos necesarios para nuestro proyecto usando pip desde la terminal de VSCode.
  
- Para desactivar el entorno ejecutar `deactivate` en la terminal de VSCode

## Generación del archivo "requirements.txt"

"requirements.txt" es el archivo que guardará los nombres de los módulos instalados para nuestro proyecto, así como las versiones de los mismos.

Para generar este archivo en la carpeta `deps/` ejecutar en la terminal de VSCode: 

`pip freeze > deps/requirements.txt`. 

Un archivo con ese nombre se creará en la carpeta correspondiente de nuestro proyecto. Un ejemplo del mismo se puede ver a continuación:

![image](https://github.com/Grupo-de-Computacion-de-la-FI-UNER/pa-repositorio-practica-inicial/assets/69655502/82bbe65e-8329-4579-bd12-102e317b628f)

En el futuro se puede reproducir este entorno a partir del "requirements.txt", ejecutando el siguiente comando en un entorno virtual nuevo:

`pip install -r deps/requirements.txt`
