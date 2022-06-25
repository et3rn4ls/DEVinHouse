class Conta:
    def __init__(self, nome, numero, saldo, limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def mostraSaldo(self):
        print(f'Saldo da conta {self.numero}: R$ {self.saldo}')
    
    def fazerDeposito(self, valor_deposito):
        self.saldo += valor_deposito


conta1 = Conta('Adriano Matos Meier', '1234-5', 5000.00, 2000.00)
conta1.fazerDeposito(589.98)
conta1.mostraSaldo()