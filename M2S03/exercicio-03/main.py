from random import sample, shuffle

N = sample(range(1, 100), 20)
shuffle(N)
print(N)
numero = min(N)
posicao = N.index(numero)

print(f'O menor elemento de N é {numero} e a sua posição dentro da lista é {posicao}')
