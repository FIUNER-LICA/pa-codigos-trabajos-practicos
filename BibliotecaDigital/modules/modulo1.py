print("__name__:", __name__)

def raiz(a):
    return a**0.5

if __name__ == "__main__":
    num = input("Ingrese un número para calcular su raiz: ")
    print(raiz(int(num)))