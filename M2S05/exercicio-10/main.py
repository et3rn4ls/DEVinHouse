import time

from Medico import Medico, menuMedico
from Paciente import Paciente, menuPaciente
from Agenda import Agenda, menuAgenda
from Util import *


if __name__ == '__main__':

    hr_ini = time.time()

    while True:
        print("""
            Selecione uma opção:

            [1] Medico
            [2] Paciente
            [3] Agenda
            [0] Sair
        """)

        op = input('Opção: ')

        if op == '0':
            print ('Saindo ...')
            break

        if op == '1':
            hi = time.time()
            menuMedico()
            hf = time.time()
            total = tempo(hi, hf)
            print(f'\nTempo menu Medico {total}')
        if op == '2':
            hi = time.time()
            menuPaciente()
            hf = time.time()
            total = tempo(hi, hf)
            print(f'\nTempo menu Paciente {total}')
        if op == '3':
            hi = time.time()
            menuAgenda()
            hf = time.time()
            total = tempo(hi, hf)
            print(f'\nTempo menu Agenda {total}')

    hr_fim = time.time()
    uso_total = tempo(hr_ini, hr_fim)
    print(f'\nTempo de uso do sistema {uso_total}\n')
