from modules.dominio import Libro
from modules.repositorio_abstracto import RepositorioAbstracto
import csv

class RepositorioTXT(RepositorioAbstracto):
    def __init__(self, p_nombre_archivo):
        super().__init__(p_nombre_archivo)

    def guardar_libro(self, libro):  
        with open(self.nombre_archivo, "a") as archi:
            archi.write(f"{libro.nombre},{libro.autor},{libro.calificacion}\n")

    def obtener_libros(self):
        lista_libros = []
        try:
            with open(self.nombre_archivo, "r") as archi:
                for linea in archi:
                    nombre, autor, calificacion = linea.rstrip().split(',')
                    libro = Libro(nombre, autor, float(calificacion))
                    lista_libros.append(libro)
        except FileNotFoundError:
            with open(self.nombre_archivo, "w") as archi:
                pass
        # except ValueError:    # ejemplo de manejo erróneo de excepción pues apantalla la causa raíz del problema. Pruebe eliminar la conversión a float de la calificación y descomente esta línea. ¿A qué conclusión llega? ¿Es realmente correcto el mensaje de la excepción lanzada?
        #     raise ValueError(f"Error al leer el archivo {self.nombre_archivo}")        
        return lista_libros
    
    
class RepositorioCSV(RepositorioAbstracto):
    def __init__(self, p_nombre_archivo):
        super().__init__(p_nombre_archivo)

    def guardar_libro(self, libro):
        with open(self.nombre_archivo, "a", newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow([libro.nombre, libro.autor, libro.calificacion])

    def obtener_libros(self):
        lista_libros = []
        try:
            with open(self.nombre_archivo, "r", newline='', encoding='utf-8') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for fila in lector_csv:
                    # Cada fila es una lista de valores de la fila del CSV
                    nombre, autor, calificacion = fila
                    libro = Libro(nombre, autor, float(calificacion))
                    lista_libros.append(libro)
        except FileNotFoundError:
            with open(self.nombre_archivo, "w", newline='', encoding='utf-8') as archivo_csv:
                pass
        except ValueError:
            print(f"Error al leer el archivo {self.nombre_archivo}")
        return lista_libros