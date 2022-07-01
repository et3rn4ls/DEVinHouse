from Pessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.convenio = convenio
        self.data_de_nascimento = data_de_nascimento
    
    @staticmethod
    def cadastrar_paciente():
        pass

    @staticmethod
    def exibir_paciente():
        pass

    def __salvar_paciente(self):
        pass
