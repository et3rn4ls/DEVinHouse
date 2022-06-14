def formatar(t, c="-"):
    print(f'{c * 24} {t} {c * 24}')

texto = input('Digite um texto: ')
caractere = input('Informe o caractere: ')

if len(caractere) == 0:
    formatar(texto)
else:
    formatar(texto, caractere)
