import json
import os

from Medico import Medico
from Paciente import Paciente


filedb = os.path.join('./', 'data', 'agendadb.json')
agendas = {"agendas": []}


class Agenda(Paciente, Medico):

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
        crm_medico = int(input('CRM Medico: '))
        cpf_paciente = input('CPF Paciente: ')
        dia = int(input('Dia: '))
        mes = int(input('Mes: '))
        ano = int(input('Ano: '))
        hora = input('Hora: ')
        observacao = input('Observacao: ')

        a = Agenda(crm_medico, cpf_paciente, dia, mes, ano, hora, observacao)
        a.__salvar_agenda()

    @staticmethod
    def exibir_agenda():
        try:
            with open(filedb) as agendadb:
                print(json.load(agendadb))
        except FileNotFoundError as exception:
            print('\nNenhum cadastro de agenda localizado.')


    def __salvar_agenda(self):
        print('\nSalvando...')
        keys = ["crm_medico", "cpf_paciente", "dia", "mes", "ano", "hora", "observacao"]
        values = [self.crm_medico, self.cpf_paciente, self.dia, self.mes, self.ano, self.ano, self.observacao]
        agenda = dict(zip(keys, values))
        agendas['agendas'].append(agenda)

        try:
            with open(filedb, "r+") as agendadb:
                listaAgendas = json.load(agendadb)
                listaAgendas["agendas"].append(agenda)
                agendadb.seek(0)
                json.dump(listaAgendas, agendadb)
        except FileNotFoundError as exception:
            with open(filedb, "w") as agendadb:
                json.dump(agendas, agendadb)
            self.__salvar_agenda

        print('\nAgenda salva!')


if __name__ == "__main__":

    while True:
        print("""
            Selecione uma opção:

            [1] Cadastrar agenda
            [2] Exibir agendas
            [0] Sair
        """)

        op = int(input('Opção: '))

        if op == 0:
            print ('Saindo ...')
            break

        if op == 1:
            Agenda.cadastrar_agenda()
        elif op == 2:
            Agenda.exibir_agenda()
        else:
            print('Opção inválida!')

