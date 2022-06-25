class Conta:
    def __init__(self, nome, numero, saldo, limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

conta1 = Conta('Adriano Matos Meier', '123-4', 5000.00, 2000.00)
print(f'Nome titular: {conta1.nome} \nNúmero da conta: {conta1.numero} \nSaldo: R${conta1.saldo} \nLimite Diário: R${conta1.limite}')