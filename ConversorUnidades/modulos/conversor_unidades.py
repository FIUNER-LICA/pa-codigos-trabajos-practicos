# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:20:29 2021

@author: je_su
"""

# Se quiere implementar pruebas unitarias para un conversor de unidades de temperatura que convierte valores(float)
# entre las unidades Fahrenheit, Celsius y Kelvin (identificadas con los caracteres 'F', 'C' y 'K' en mayúsculas)
# el conversor maneja los casos en que la temperatura no es físicamente realizable (< 0 K)
# y también el caso en que se ingresen otras opciones diferentes a 'F', 'C' y 'K' como parámetros.

# El conversor opera de la siguiente manera:
# - Para convertir una temperatura de una unidad a otra, primero se convierte el valor a grados Kelvin 
# y después a las unidades requeridas. 
# - Si la unidad de temperatura original es la misma a la que se quiere convertir, 
# se devuelve el mismo valor sin modificar.

#FÓRMULAS:
#   T_K = T_C + 273.15
#   T_K = (T_F + 459.67)*5/9

# El Conversor tiene implementado los siguientes métodos:
# convertir_a_kelvin((float)temperatura, (str)desde_unidad)
# convertir_desde_kelvin((float)temperatura_K, (str)a_unidad)  
# ValueError: excepción que se lanza cuando el valor de temperatura a convertir es < a 0 ºK
# KeyError: excepción lanzada al ingresar una unidad no reconocida
# convertir_temperatura((float)temperatura, (str)desde_unidad, (str)a_unidad)



class ConversorUnidadesTemperatura:
   
        
    def convertir_a_kelvin(self, temperatura, desde_unidad):
        """Función para convertir una temperatura en en unidades C o F a Kelvin
        Args:
            temperatura (float): temperatura a convertir a Kelvin
            desde_unidad (str): unidad en la que se encuentra el parámetro temperatura, 
                                toma valores 'K', 'C' o 'F' según la unidad
        Raises:
            ValueError: excepción que se lanza cuando el valor de temperatura a convertir es < a 0 ºK
            KeyError: excepción lanzada al ingresar una unidad no reconocida
        Returns:
            float: temperatura en kelvin
        """   
        if desde_unidad not in ['K', 'C', 'F']:
            raise KeyError(f'Unidad de temperatura no reconocida: {desde_unidad}') 
        elif desde_unidad == 'K':
            temperatura_kelvin = temperatura       
        elif desde_unidad == 'C':
            temperatura_kelvin = temperatura + 273.15
        elif desde_unidad == 'F':
            temperatura_kelvin = (temperatura + 459.67)*5/9     
            
        if temperatura_kelvin < 0:
            raise ValueError(f'Temperatura no válida: {temperatura} {desde_unidad} menor que 0 K')
            
        return temperatura_kelvin
    
    def convertir_desde_kelvin(self, temperatura, a_unidad):
        """Función para convertir una temperatura en Kelvin a las unidades C o F
        Args:
            temperatura (float): temperatura en Kelvin a convertir
            a_unidad (str): unidad a la que se convierte el parámetro temperatura, 
                            toma valores tipo string 'K', 'C' o 'F'       
        Raises:
            ValueError: excepción que se lanza cuando el valor de temperatura a convertir es < a 0 ºK
            KeyError: excepción lanzada al ingresar una unidad no reconocida
        Returns:
            float: temperatura en K C o F
        """
        if temperatura < 0:
            raise ValueError(f'Temperatura no válida: {temperatura} K menor que 0 K')
        if a_unidad not in ['K', 'C', 'F']:
            raise KeyError(f'Unidad de temperatura no reconocida: {a_unidad}') 
        elif a_unidad == 'K':
            return temperatura       
        elif a_unidad == 'C':
            return temperatura - 273.15
        elif a_unidad == 'F':
            return temperatura*9/5 - 459.67 
    
    def convertir_unidades_temperatura(self, temperatura, desde_unidad, a_unidad):
        """Función para convertir una temperatura desde una unidad "desde_unidad" a otra "a_unidad"
        Args:
            temperatura (float): temperatura a convertir
            desde_unidad (str): unidad en la que se encuentra el parámetro temperatura, toma valores tipo string 'K', 'C' o 'F'
            a_unidad (str): unidad a la que se convierte el parámetro temperatura, toma valores tipo string 'K', 'C' o 'F'
        Raises:
            KeyError: excepción lanzada al ingresar una unidad no reconocida
        """
        if desde_unidad not in ['K', 'C', 'F'] or a_unidad not in ['K', 'C', 'F']:
            raise KeyError(f'Unidad de temperatura no reconocida: {desde_unidad}')
        elif desde_unidad == a_unidad:
            #no necesito conversión
            return temperatura
        else:
            #Primero convierto temperatura desde "desde_unidad" a Kelvin
            temperatura_kelvin = self.convertir_a_kelvin(temperatura, desde_unidad)
            #Ahora convierto desde Kelvin a "a_unidad"
            return self.convertir_desde_kelvin(temperatura_kelvin, a_unidad)
            
    
    
    
    
    
    
    
    
    
    
    