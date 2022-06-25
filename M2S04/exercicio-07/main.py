from Operacoes import Conta

conta1 = Conta('Adriano Matos Meier', '1234-5', 5000.00, 2000.00)
conta2 = Conta('Serj Tankian', '4321-X', 3000.00, 1000.00)

while True:
    print("""
        Escolha a operação:

        [1] Saque
        [2] Deposito
        [3] Transferencia
        [4] Sair
    """)

    operacao = int(input('Operação: '))

    if operacao == 4:
        print ('\nSaindo ...\n')
        break

    if operacao == 1:
        valor = float(input('Valor do saque: '))
        print('\n-----------------------------------------')
        print('Retorno Transação - Saque')
        conta1.fazerSaque(valor)
        conta1.mostraSaldo()
        print('-----------------------------------------')
    elif operacao == 2:
        valor = float(input('Valor do deposito: '))
        print('\n-----------------------------------------')
        print('Retorno Transação - Deposito')
        conta1.fazerDeposito(valor)
        conta1.mostraSaldo()
        print('-----------------------------------------')
    elif operacao == 3:
        valor = float(input('Valor da transferencia: '))
        print('\n-----------------------------------------')
        print('Retorno Transação - Transferencia')
        if conta1.fazerTransferencia(valor, '4321-X') == True:
            conta2.fazerDeposito(valor)
        print('\n-----------------------------------------')
        conta1.mostraSaldo()
        print('-----------------------------------------')
        conta2.mostraSaldo()
        print('-----------------------------------------')
    else:
        print('\n----------------------')
        print('Opcao invalida!')
        print('----------------------')
