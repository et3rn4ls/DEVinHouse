from Pessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__convenio = convenio
        self.__data_de_nascimento = data_de_nascimento
    
    def __cadastrar_paciente(self):
        pass

    def __exibir_paciente(self):
        pass

    def salvar_paciente(self):
        pass
