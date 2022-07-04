from Medico import Medico, menuMedico
from Paciente import Paciente, menuPaciente
from Agenda import Agenda, menuAgenda


if __name__ == '__main__':

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
            menuMedico()
        if op == '2':
            menuPaciente()
        if op == '3':
            menuAgenda()