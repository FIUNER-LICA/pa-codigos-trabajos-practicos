import unittest
from modules.servicio import GestorDeLibros
from modules.repositorio_abstracto import RepositorioAbstracto

class FakeRepository(RepositorioAbstracto):
    def __init__(self):
        self.__libros = []

    def guardar_libro(self, libro):
        self.__libros.append(libro)

    def obtener_libros(self):
        return self.__libros


class TestServicio(unittest.TestCase):

    def test_agregar_nuevo_libro(self):
        # Arrange
        repo = FakeRepository()
        gestor = GestorDeLibros(repo)
        # Act
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5)
        # Assert
        self.assertIsNotNone(gestor.listar_libros_existentes())
        self.assertEqual(gestor.numero_libros, 1)

    def test_agregar_multiples_libros(self):
        repo = FakeRepository()
        gestor = GestorDeLibros(repo)
        self.assertEqual(gestor.numero_libros, 0)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5)
        self.assertEqual(gestor.numero_libros, 1)
        gestor.agregar_nuevo_libro("Momo", "Michael Ende", 9.0)
        self.assertEqual(gestor.numero_libros, 2)

    def test_listar_libros_existentes_vacio(self):
        repo = FakeRepository()
        gestor = GestorDeLibros(repo)
        self.assertEqual(gestor.listar_libros_existentes(), [])

    def test_listar_libros_existentes(self):
        repo = FakeRepository()
        gestor = GestorDeLibros(repo)
        gestor.agregar_nuevo_libro("El principito", "Antoine de Saint-Exupéry", 9.5)
        gestor.agregar_nuevo_libro("Momo", "Michael Ende", 9.0)
        lista_resultado = [{'nombre': 'El principito', 'autor': 'Antoine de Saint-Exupéry', 'calificacion': 9.5},
                           {'nombre': 'Momo', 'autor': 'Michael Ende', 'calificacion': 9.0}]
        self.assertEqual(gestor.listar_libros_existentes(), lista_resultado)

    


    

    
if __name__ == "__main__":
    unittest.main()
