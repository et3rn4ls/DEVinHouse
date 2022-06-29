from Medico import Medico
from Paciente import Paciente

class Agenda:

    def __init__(self, crm_medico: int, cpf_paciente: str, dia: int, mes: int, ano: int, hora: str, observacao: str):
        self.__crm_medico = crm_medico
        self.__cpf_paciente = cpf_paciente
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__hora = hora
        self.__observacao = observacao
    
    def __cadastrar_agenda(self):
        pass

    def __exibir_agenda(self):
        pass

    def salvar_agenda(self):
        pass

