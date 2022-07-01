import json
import os
from os.path import exists

from Pessoa import Pessoa

class Medico(Pessoa):

    def __init__(self, crm: int, telefone_secundario: str):
        self.__crm = crm
        self.__telefone_secundario = telefone_secundario
    
    def __cadastrar_medico(self):
        pass

    def __exibir_medico(self):
        pass

    def salvar_medico(self):
        pass
