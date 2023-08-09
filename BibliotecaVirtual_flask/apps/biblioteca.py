# -*- coding: utf-8 -*-
# Documentación de Flask
# https://flask.palletsprojects.com/en/2.3.x/
# Documentación de jinja
# https://palletsprojects.com/p/jinja/
# https://www.w3schools.com/html/html_forms.asp
# https://www.geeksforgeeks.org/__name__-a-special-variable-in-python/
"""
Created on Thu Mar 9 13:12:19 2023

@author: je_su
"""

from modules.funciones import agregar_libro_a_lista, cargar_lista_desde_archivo, guardar_lista_en_archivo


OPCIONES = """
Elige una opción:
1. Ingresar libro nuevo
2. Listar libros
3. Salir
"""
RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos.txt"


#print(__name__)

def main():
    lista_libros = []
    salir = False

    try:
        cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
    except FileNotFoundError:
        with open(ARCHIVO, "w") as archi:
            pass

      
    while not salir:
        opcion = input(OPCIONES)
        if opcion == "1":
            nombre_libro = input("ingresar nombre del libro: ")
            autor_libro = input("ingresar autor del libro: ")
            puntaje_libro = input("ingresar puntaje del libro: ")

            agregar_libro_a_lista(lista_libros, nombre_libro, autor_libro, puntaje_libro)
            
        elif opcion == "2":
            if len(lista_libros)== 0:
                print("La Biblioteca está vacía")
            else:
                for libro in lista_libros:
                    print(f"{libro['nombre']} - {libro['autor']} - {libro['puntaje']}/10")
        
        elif opcion == "3":
            guardar_lista_en_archivo(ARCHIVO, lista_libros)
            salir = True
        
        else:
            print("La opción ingresada no es correcta")
        


if __name__ == "__main__":
    print(type("Hola"))
    main()