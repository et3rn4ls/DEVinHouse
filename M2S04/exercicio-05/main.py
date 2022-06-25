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

    def fazerSaque(self, valor_saque):

        if valor_saque <= self.saldo and valor_saque <= self.limite:
            self.saldo -= valor_saque
            self.limite -= valor_saque
            print('Saque liberado!')
            return True
        else:
            print('Valor indisponivel para saque!')
            return False


conta1 = Conta('Adriano Matos Meier', '1234-5', 5000.00, 2000.00)
print('Retorno Saque - Transação 1')
conta1.fazerSaque(3890)
print('--------------------------------')
print('Retorno Saque - Transação 2')
conta1.fazerSaque(1890)
print('--------------------------------')
conta1.mostraSaldo()