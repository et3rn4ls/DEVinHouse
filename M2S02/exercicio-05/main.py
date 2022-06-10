vogais = ('a', 'e', 'i', 'o', 'u')

while True:
    letra = input('Informe uma letra: ')

    if letra == '0':
        print ('Saindo...')
        break
    elif letra.isdigit() == True:
        print ('Informe uma letra e não um número!')
        continue
    else:
        if letra in vogais:
            print('{0} é uma vogal' .format(letra))
            continue
        print('{0} é uma consoante' .format(letra))