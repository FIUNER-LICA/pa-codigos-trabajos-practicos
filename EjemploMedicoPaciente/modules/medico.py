from modules.persona import Persona

class Medico(Persona):
    def __init__(self, p_nombre, p_especialidad):
        super().__init__(p_nombre)
        self.__especialidad = p_especialidad
        self.__pacientes = []

    def agregar_paciente(self, p_paciente):
        from modules.paciente import Paciente
        if isinstance(p_paciente, Paciente):
            self.__pacientes.append(p_paciente)
        else:
            raise TypeError("p_paciente debe ser un objeto de tipo Paciente")
        
    def devolver_pacientes(self):
        return [paciente.nombre for paciente in self.__pacientes]
