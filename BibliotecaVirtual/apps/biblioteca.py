# -*- coding: utf-8 -*-
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
ARCHIVO = "libros_leidos.txt"


def main():
    lista_libros = []
    salir = False

    # cargar_lista_desde_archivo(RUTA + ARCHIVO, lista_libros) 
    try:
        cargar_lista_desde_archivo(RUTA + ARCHIVO, lista_libros)            
    except FileNotFoundError:
        with open(RUTA + ARCHIVO, "w") as archi:
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
            guardar_lista_en_archivo(RUTA + ARCHIVO, lista_libros)
            salir = True
        
        else:
            print("La opción ingresada no es correcta")
        


if __name__ == "__main__":
    main()