from modules.medico import Medico
from modules.paciente import Paciente

pac1 = Paciente("Carla")
pac2 = Paciente("Manuel")

med1 = Medico("Marta", "Clinica")
med2 = Medico("Roberto", "Gastroenterología")

# asociación pac1-med1 y med2
pac1.agregar_medico(med1)
pac1.agregar_medico(med2)
med1.agregar_paciente(pac1)

# asociación pac2-med2
pac2.agregar_medico(med2)

print(f"Medicos del paciente 1: {pac1.devolver_medicos()}")
print(f"Medicos del paciente 2: {pac2.devolver_medicos()}")
print(f"Pacientes del medico 1: {med1.devolver_pacientes()}")
print(f"Pacientes del medico 2: {med2.devolver_pacientes()}")


# property
print("pac1.nombre:", pac1.nombre)  # getter
pac1.nombre = "Carla Antonela" # setter 
print("pac1.nombre:", pac1.nombre)  # getter
# pac1.nombre = "" # setter 
