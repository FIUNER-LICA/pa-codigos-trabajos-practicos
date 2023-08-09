import server


print(f"__name__ ejecutado en auxiliar.py: {__name__}")

if __name__=="__main__":
    print("Se ejecuta auxiliar.py directamente")
else:
    print("Se importó auxiliar desde otro módulo")