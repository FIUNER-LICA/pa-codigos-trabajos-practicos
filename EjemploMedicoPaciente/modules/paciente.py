from modules.medico import Medico
from modules.persona import Persona

class Paciente(Persona):
    def __init__(self, p_nombre):
        super().__init__(p_nombre)
        self.__medicos = []

    def agregar_medico(self, p_medico):
        if not isinstance(p_medico, Medico):
            raise TypeError("p_médico debe ser un objeto de tipo Médico")
        
        self.__medicos.append(p_medico)

        # if isinstance(p_medico, Medico):
        #     self.__medicos.append(p_medico)
        # else:
        #     raise TypeError("p_médico debe ser un objeto de tipo Médico")

    def devolver_medicos(self):
        return [medico.nombre for medico in self.__medicos]
