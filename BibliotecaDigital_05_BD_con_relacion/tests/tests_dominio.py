from modules.dominio import Libro
import unittest

class TestLibro(unittest.TestCase):

    def test_crear_libro(self):
        libro1 = Libro(1, "El principito", "Antoine de Saint-Exupéry", 9.5, 1)
        self.assertEqual(libro1.id, 1)
        self.assertEqual(libro1.nombre, "El principito")
        self.assertEqual(libro1.autor, "Antoine de Saint-Exupéry")
        self.assertEqual(libro1.calificacion, 9.5)
        self.assertEqual(libro1.id_usuario, 1)

        libro2 = Libro(2, "1984", "George Orwell", 10, 2)
        self.assertEqual(libro2.id, 2)
        self.assertEqual(libro2.nombre, "1984")
        self.assertEqual(libro2.autor, "George Orwell")
        self.assertEqual(libro2.calificacion, 10)
        self.assertEqual(libro2.id_usuario, 2)

    def test_crear_libro_id_no_numerico_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            Libro("a", "El principito", "Antoine de Saint-Exupéry", 9.5, 1)

    def test_crear_libro_nombre_vacio_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            Libro(1, "", "Antoine de Saint-Exupéry", 9.5, 1)

    def test_crear_libro_autor_vacio_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            Libro(1, "El principito", "", 9.5, 1)

    def test_crear_libro_calificacion_erronea_lanza_execpcion(self):
        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", -1, 1)
        
        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", 11, 1)

        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", 'a', 1)

        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", '-1', 1)

        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", '11', 1)

        with self.assertRaises(ValueError):
            Libro(1, "El principito", "Antoine de Saint-Exupéry", '', 1)

if __name__=="__main__":
    unittest.main()

