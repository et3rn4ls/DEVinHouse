import json
import os

from Util import DEVinException
from Pessoa import Pessoa


filedb = os.path.join('./', 'data', 'medicodb.json')
medicos = {"medicos": []}


class Medico(Pessoa):

    def __init__(self, crm: int, telefone_secundario: str):
        self.crm = crm
        self.telefone_secundario = telefone_secundario
    
    @staticmethod
    def cadastrar_medico():
        print('\n---- Cadastro de Pessoa ----')
        Pessoa.cadastrar_pessoa()

        print('\n---- Cadastro do Medico ----')
        crm = int(input('CRM: '))
        telefone_secundario = input('Telefone secundario: ')

        if len(telefone_secundario) == 0:
            raise DEVinException('\n[ERRO] - Todos os campos sao obrigatorios!')
        else:
            m = Medico(crm, telefone_secundario)
            m.__salvar_medico()

    @staticmethod
    def exibir_medico():
        try:
            with open(filedb) as medicodb:
                print(json.load(medicodb))
        except FileNotFoundError as exception:
            print('\nNenhum cadastrado de medico localizado.')


    def __salvar_medico(self):
        print('\nSalvando ...')
        keys = ["crm", "telefone_secundario"]
        values = [self.crm, self.telefone_secundario]
        medico = dict(zip(keys, values))
        medicos['medicos'].append(medico)

        try:
            with open(filedb, 'r+') as medicodb:
                listaMedicos = json.load(medicodb)
                listaMedicos['medicos'].append(medico)
                medicodb.seek(0)
                json.dump(listaMedicos, medicodb)
        except FileNotFoundError as exception:
            with open(filedb, 'w') as medicodb:
                json.dump(medicos, medicodb)
            self.__salvar_medico

        print('\nCadastro do medico salvo!')


def menuMedico():

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar medico
            [2] Exibir medicos
            [0] Voltar
        """)

        op = input('Opção: ')

        if op == '0':
            print ('Saindo ...')
            break

        if op == '1':
            try:
                Medico.cadastrar_medico()
            except DEVinException as exception:
                print(exception)
        elif op == '2':
            Medico.exibir_medico()
        else:
            print('Opção inválida!')
        