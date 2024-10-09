import unittest
from modules.gestor_libros import GestorDeLibros
from modules.repositorio_abstracto import RepositorioAbstracto

class RepositorioFalsoLibros(RepositorioAbstracto):
    def __init__(self):
        self.__libros = []

    def guardar_registro(self, libro):
        libro.id = len(self.__libros) + 1
        self.__libros.append(libro)

    def obtener_todos_los_registros(self):
        return self.__libros

    def obtener_registro_por_filtro(self, filtro, valor):
        for libro in self.__libros:
            if getattr(libro, filtro) == valor:
                return libro
        return None
    
    def modificar_registro(self, libro_modificado):
        for libro in self.__libros:
            if libro.id == libro_modificado.id:
                libro.nombre = libro_modificado.nombre
                libro.autor = libro_modificado.autor
                libro.calificacion = libro_modificado.calificacion
                break

    def eliminar_registro(self, id):
        for libro in self.__libros:
            if libro.id == id:
                self.__libros.remove(libro)
                break



class TestGestorDeLibros(unittest.TestCase):

    def test_agregar_nuevo_libro(self):
        # Arrange
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        # Act
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        # Assert
        self.assertIsNotNone(repo.obtener_registro_por_filtro("nombre", "El principito"))

    def test_agregar_libro_existente_lanza_excepcion(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        with self.assertRaises(ValueError):
            gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)

    def test_numero_libros_agregar(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        self.assertEqual(gestor.numero_libros, 0)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        self.assertEqual(gestor.numero_libros, 1)
        gestor.agregar_nuevo_libro("Momo", "Michael Ende", 9.0, 1)
        self.assertEqual(gestor.numero_libros, 2)

    def test_numero_libros_eliminar(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        gestor.agregar_nuevo_libro("Momo", "Michael Ende", 9.0, 1)
        self.assertEqual(gestor.numero_libros, 2)
        gestor.eliminar_libro_seleccionado(1)
        self.assertEqual(gestor.numero_libros, 1)

    def test_devolver_libro_a_editar(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        libro = gestor.devolver_libro(1)
        self.assertEqual(libro["nombre"], "El principito")
        self.assertEqual(libro["autor"], "Antoine de Saint-Exupéry")
        self.assertEqual(libro["calificacion"], 9.5)

    def test_editar_libro(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 2)
        gestor.editar_libro(1, "El principito", "Antoine de Saint-Exupéry", 10)
        libro = gestor.devolver_libro(1)
        self.assertEqual(libro["calificacion"], 10)

    def test_editar_libro_inexistente_lanza_excepcion(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        with self.assertRaises(ValueError):
            gestor.editar_libro(1, "El principito", "Antoine de Saint-Exupéry", 10)

    def test_eliminar_libro_inexistente_lanza_excepcion(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        with self.assertRaises(ValueError):
            gestor.eliminar_libro_seleccionado(1)
    
    def test_eliminar_libro(self):
        repo = RepositorioFalsoLibros()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        gestor.eliminar_libro_seleccionado(1)
        self.assertIsNone(repo.obtener_registro_por_filtro("id", 1))

    
if __name__ == "__main__":
    unittest.main()
