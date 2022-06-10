import Math as calc

while True:
    print("""
        Escolha a operação:

        [1] Somar
        [2] Subtrair
        [3] Dividir
        [4] Multiplicar

        [0] Sair
    """)

    op = int(input('Opção: '))

    if op == 0:
        print ('Tchau!')
        break

    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    if op == 1:
        print ('Resultado: ', calc.somar(num1, num2))
    elif op == 2:
        print ('Resultado: ', calc.subtrair(num1, num2))
    elif op == 3:
        print ('Resultado: ', calc.dividir(num1, num2))
    elif op == 4:
        print ('Resultado: ', calc.multiplicar(num1, num2))
