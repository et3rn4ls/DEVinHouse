import json
import os
from os.path import exists

from Pessoa import Pessoa


filedb = os.path.join('./', 'data', 'medicodb.json')
medicos = []


class Medico(Pessoa):

    #def __init__(self, nome: str, celular: int, email: str, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        #super().__init__(nome=nome, celular=celular, email=email)
    def __init__(self, crm: int, telefone_secundario: str):
        self.crm = crm
        self.telefone_secundario = telefone_secundario
    
    @staticmethod
    def cadastrar_medico():
        crm = int(input('CRM: '))
        telefone_secundario = input('Telefone secundario: ')

        m = Medico(crm, telefone_secundario)
        m.__salvar_medico()

    @staticmethod
    def exibir_medico():
        with open(filedb) as medicodb:
            print(json.load(medicodb))

    def __salvar_medico(self):
        print('\nSalvando ...')
        keys = ["crm", "telefone_secundario"]
        values = [self.crm, self.telefone_secundario]
        medico = dict(zip(keys, values))
        medicos.append(medico)

        if exists(filedb):
            with open(filedb) as medicodb:
                listaMedicos = json.load(medicodb)
                listaMedicos.append(medico)
            with open(filedb, "w") as medicodbrw:
                json.dump(listaMedicos, medicodbrw)
        else:
            with open(filedb, "w") as medicodbrw:
                json.dump(medicos, medicodbrw)

        print('\nMedico salvo!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar medico
            [2] Exibir medicos
            [0] Sair
        """)

        op = int(input('Opção: '))

        if op == 0:
            print ('Saindo ...')
            break

        if op == 1:
            Medico.cadastrar_medico()
        elif op == 2:
            Medico.exibir_medico()
        else:
            print('Opção inválida!')
        