from modules.modulo1 import raiz

def potencia_2(x):
    return x**2

num = input("Ingrese un número para elevarlo al cuadrado: ")
print(potencia_2(int(num)))
print(raiz(int(num)))