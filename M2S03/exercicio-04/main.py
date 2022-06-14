def formatar(t, c="-"):
    print(f'{c * 5} {t} {c * 5}')

texto = input('Digite uma palavra: ')
caractere = input('Informe o caractere: ')

if len(caractere) == 0:
    formatar(texto)
else:
    formatar(texto, caractere)
