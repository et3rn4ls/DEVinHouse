import json
import os

from Util import DEVinException
from Pessoa import Pessoa


filedb = os.path.join('./', 'data', 'pacientedb.json')
pacientes = {"pacientes": []}


class Paciente(Pessoa):

    def __init__(self, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.convenio = convenio
        self.data_de_nascimento = data_de_nascimento
    
    @staticmethod
    def cadastrar_paciente():
        print('\n---- Cadastro de Pessoa ----')
        Pessoa.cadastrar_pessoa()

        print('\n---- Cadastro do Paciente ----')
        rg = int(input('RG: '))
        cpf = input('CPF: ')
        telefone = int(input('Telefone: '))
        convenio = input('Convenio: ')
        data_de_nascimento = input('Data de nascimento: ')

        if len(cpf) == 0 or len(telefone) == 0 or len(convenio) ==0 or len(data_de_nascimento) == 0:
            raise DEVinException('\n[ERRO] - Todos os campos sao obrigatorios!')
        else:
            p = Paciente(rg, cpf, telefone, convenio, data_de_nascimento)
            p.__salvar_paciente()


    @staticmethod
    def exibir_paciente():
        try:
            with open(filedb) as pacientedb:
                print(json.load(pacientedb))
        except FileNotFoundError as exception:
            print('\nNenhum cadastrado de paciente localizado.')

    def __salvar_paciente(self):
        print('\nSalvando ...')
        keys = ["rg", "cpf", "telefone", "convenio", "data_de_nascimento"]
        values = [self.rg, self.cpf, self.telefone, self.convenio, self.data_de_nascimento]
        paciente = dict(zip(keys, values))
        pacientes['pacientes'].append(paciente)

        try:
            with open(filedb, 'r+') as pacientedb:
                listaPacientes = json.load(pacientedb)
                listaPacientes['pacientes'].append(paciente)
                pacientedb.seek(0)
                json.dump(listaPacientes, pacientedb)
        except FileNotFoundError as exception:
            with open(filedb, 'w') as pacientedb:
                json.dump(pacientes, pacientedb)
            self.__salvar_paciente

        print('\nCadastro do paciente salvo!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar paciente
            [2] Exibir paciente
            [0] Sair
        """)

        op = input('Opção: ')

        if op == '0':
            print ('Saindo ...')
            break

        if op == '1':
            try:
                Paciente.cadastrar_paciente()
            except DEVinException as exception:
                print(exception)
        elif op == '2':
            Paciente.exibir_paciente()
        else:
            print('Opção inválida!')
        
