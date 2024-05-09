# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:21:01 2021

@author: je_su
"""
import unittest
from modulos.conversor_unidades import ConversorUnidadesTemperatura

class TestConversorUnidadesTemperatura(unittest.TestCase):
    
    def setUp(self):
        # print("\nIniciando pruebas...")
        self.miConversor = ConversorUnidadesTemperatura() 

    def test_convertir_a_kelvin_valores_extremos(self):
        """ prueba valores de temperatura en los extremos para convertir a unidades Kelvin"""
        self.assertEqual( self.miConversor.convertir_a_kelvin(0, 'C'), 273.15)
        self.assertEqual( self.miConversor.convertir_a_kelvin(-273.15, 'C'), 0)
        #self.assertEqual( self.miConversor.convertir_a_kelvin(0, 'F'), 255.37)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(0, 'F'), 255.37, places=2)
        self.assertEqual( self.miConversor.convertir_a_kelvin(-459.67, 'F'), 0) 

    def test_convertir_a_kelvin_valores_intermedios(self):
        """ prueba valores de temperatura intermedios para convertir a unidades Kelvin"""
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(100, 'C'), 373.15, places=2 )
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-10.5, 'C'), 262.65, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(450, 'F'), 505.37, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-40, 'F'), 233.15, places=2)
        # convertir a kelvin desde kelvin
        self.assertEqual( self.miConversor.convertir_a_kelvin(20, 'K'), 20)

    def test_convertir_a_kelvin_excepciones(self):
        """ prueba que se lanzan las excepciones de la función""" 
        self.assertRaises(KeyError, self.miConversor.convertir_a_kelvin, 100, 'X')
        self.assertRaises(ValueError, self.miConversor.convertir_a_kelvin, -274, 'C')
        self.assertRaises(ValueError, self.miConversor.convertir_a_kelvin, -460, 'F')

    def test_convertir_desde_kelvin_valores_extremos(self):
        self.assertEqual( self.miConversor.convertir_desde_kelvin(273.15, 'C'), 0)
        self.assertEqual( self.miConversor.convertir_desde_kelvin(0, 'C'), -273.15)
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(255.37, 'F'), 0, places=2)         
        self.assertEqual( self.miConversor.convertir_desde_kelvin(0, 'F'), -459.67) 

    def test_convertir_desde_kelvin_valores_intermedios(self):
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(373.15, 'C'), 100, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(3.5, 'C'), -269.65, places=2)        
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(303.5, 'F'), 86.63, places=2)         
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(10.5, 'F'), -440.77, places=2) 
        # convertir desde kelvin a kelvin
        self.assertEqual( self.miConversor.convertir_desde_kelvin(35, 'K'), 35)

    def test_convertir_desde_kelvin_excepciones(self):
        self.assertRaises(KeyError, self.miConversor.convertir_desde_kelvin, 20, 'X')
        self.assertRaises(ValueError, self.miConversor.convertir_desde_kelvin, -10, 'C')
        self.assertRaises(ValueError, self.miConversor.convertir_desde_kelvin, -100, 'F')
    
    def test_convertir_unidades(self):
        """pruebo conversiones de temperatura desde una unidad a otra"""
        # Pruebo valores de temperatura de conversión válidos
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(0, 'C', 'F'), 32, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(100, 'C', 'F'), 212, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(-40, 'C', 'F'), -40, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(0, 'F', 'C'), -17.78, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(100, 'F', 'C'), 37.78, places=2)
        
        self.assertEqual(self.miConversor.convertir_unidades_temperatura(25, 'C', 'C'), 25)
        self.assertEqual(self.miConversor.convertir_unidades_temperatura(25, 'F', 'F'), 25) 
    
    def test_convertir_unidades_excepciones(self):
        self.assertRaises( ValueError, self.miConversor.convertir_unidades_temperatura, -274, 'C', 'F')
        self.assertRaises( ValueError, self.miConversor.convertir_unidades_temperatura, -460, 'F', 'C')   
        self.assertRaises( KeyError, self.miConversor.convertir_unidades_temperatura, 0, 'A', 'F')
        self.assertRaises( KeyError, self.miConversor.convertir_unidades_temperatura, 0, 'F', 'T')
    
    
if __name__ == '__main__':
    
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    