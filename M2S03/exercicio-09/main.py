from Voo import Voo, Reserva

voo1456 = Voo()
res = Reserva()

while True:
    print("""
        Escolha a operação:

        [1] Mostrar quantidade de assentos livres
        [2] Mostrar assentos livres
        [3] Fazer uma reserva
        [4] Mostrar valor arrecadado com o voo
        [0] Sair
    """)

    operacao = int(input('Operação: '))

    if operacao == 0:
        print ('\nSaindo ...\n')
        break

    if operacao == 1:
        print(voo1456.getAsseDisp())
    elif operacao == 2:
        res.assentosLivres()
    elif operacao == 3:
        poltrona = int(input('Poltrona: '))
        res.fazerReserva(poltrona)
    elif operacao == 4:
        print(res.valorArrecadado())
    else:
        print('Opção inválida!')

