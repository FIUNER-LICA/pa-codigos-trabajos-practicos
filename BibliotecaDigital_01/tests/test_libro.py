from modules.libro import Libro
import unittest

class TestLibro(unittest.TestCase):

    def test_crear_libro(self):
        libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 9.5)
        self.assertEqual(libro1.nombre, "El principito")
        self.assertEqual(libro1.autor, "Antoine de Saint-Exupéry")
        self.assertEqual(libro1.calificacion, 9.5)

        libro2 = Libro("1984", "George Orwell", 10)
        self.assertEqual(libro2.nombre, "1984")
        self.assertEqual(libro2.autor, "George Orwell")
        self.assertEqual(libro2.calificacion, 10)

    def test_modificar_calificacion_libro(self):
        libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 9.5)
        libro1.calificacion = 8
        self.assertNotEqual(libro1.calificacion, 9.5)
        self.assertEqual(libro1.calificacion, 8)

    def test_crear_libro_nombre_vacio_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            Libro("", "Antoine de Saint-Exupéry", 9.5)

    def test_crear_libro_autor_vacio_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            Libro("El principito", "", 9.5)

    def test_crear_libro_calificacion_erronea_lanza_execpcion(self):
        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", -1)
        
        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", 11)

        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", 'a')

        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", '-1')

        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", '11')

        with self.assertRaises(ValueError):
            Libro("El principito", "Antoine de Saint-Exupéry", '')

if __name__=="__main__":
    unittest.main()

