import time

from Medico import Medico, menuMedico
from Paciente import Paciente, menuPaciente
from Agenda import Agenda, menuAgenda


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
            hora_inicial = time.time()
            menuMedico()
            hora_final = time.time()
            total = hora_final - hora_inicial
            print(f'\nTempo menu Medico {total}')
        if op == '2':
            hora_inicial = time.time()
            menuPaciente()
            hora_final = time.time()
            total = hora_final - hora_inicial
            print(f'\nTempo menu Paciente {total}')
        if op == '3':
            hora_inicial = time.time()
            menuAgenda()
            hora_final = time.time()
            total = hora_final - hora_inicial
            print(f'\nTempo menu Agenda {total}')

    hr_fim = time.time()
    uso_total = hr_fim - hr_ini
    print(f'\nTempo de uso do sistema {uso_total}\n')
