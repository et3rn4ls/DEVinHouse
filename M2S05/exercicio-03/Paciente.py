import json
import os
from os.path import exists

from Pessoa import Pessoa


filedb = os.path.join('./', 'data', 'pacientedb.json')
pacientes = []


class Paciente(Pessoa):

    #def __init__(self, nome: str, celular: int, email: str, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        #super().__init__(nome=nome, celular=celular, email=email)
    def __init__(self, rg: int, cpf: str, telefone: int, convenio: str, data_de_nascimento: str):
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.convenio = convenio
        self.data_de_nascimento = data_de_nascimento
    
    @staticmethod
    def cadastrar_paciente():
        rg = int(input('RG: '))
        cpf = input('CPF: ')
        telefone = int(input('Telefone: '))
        convenio = input('Convenio: ')
        data_de_nascimento = input('Data de nascimento: ')

        p = Paciente(rg, cpf, telefone, convenio, data_de_nascimento)
        p.__salvar_paciente()

    @staticmethod
    def exibir_paciente():
        with open(filedb) as pacientedb:
            print(json.load(pacientedb))

    def __salvar_paciente(self):
        print('\nSalvando ...')
        keys = ["rg", "cpf", "telefone", "convenio", "data_de_nascimento"]
        values = [self.rg, self.cpf, self.telefone, self.convenio, self.data_de_nascimento]
        paciente = dict(zip(keys, values))
        pacientes.append(paciente)

        if exists(filedb):
            with open(filedb) as pacientedb:
                listaPacientes = json.load(pacientedb)
                listaPacientes.append(paciente)
            with open(filedb, "w") as pacientedbrw:
                json.dump(listaPacientes, pacientedbrw)
        else:
            with open(filedb, "w") as pacientedbrw:
                json.dump(pacientes, pacientedbrw)

        print('\nPaciente salvo!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar paciente
            [2] Exibir paciente
            [0] Sair
        """)

        op = int(input('Opção: '))

        if op == 0:
            print ('Saindo ...')
            break

        if op == 1:
            Paciente.cadastrar_paciente()
        elif op == 2:
            Paciente.exibir_paciente()
        else:
            print('Opção inválida!')
        
