file = open('lista.json', 'r')
lista = file.readlines()
file.close()

for i in lista:
    d = (i.split(';'))

v = ''
dicio = dict.fromkeys(d, v)
print(dicio)

dicio.update({'primeiro_nome': 'Adriano'})
print(dicio)

dicio.update({'segundo_nome': 'Matos'})
print(dicio)

dicio.update({'idade': 42})
print(dicio)