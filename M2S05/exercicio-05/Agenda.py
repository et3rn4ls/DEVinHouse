from Medico import Medico
from Paciente import Paciente


class Agenda:

    def __init__(self, crm_medico: int, cpf_paciente: str, dia: int, mes: int, ano: int, hora: str, observacao: str):
        self.crm_medico = crm_medico
        self.cpf_paciente = cpf_paciente
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hora = hora
        self.observacao = observacao
    
    @staticmethod
    def cadastrar_agenda():
        pass

    @staticmethod
    def exibir_agenda():
        pass

    def __salvar_agenda(self):
        pass

