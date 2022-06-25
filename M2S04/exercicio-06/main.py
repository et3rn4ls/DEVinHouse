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

    def verSaldoLimite(self, valor_movimentacao):
        if valor_movimentacao <= self.saldo:
            if valor_movimentacao <= self.limite:
                return True
            else:
                print('Valor excede o limite diario!')
                return False
        else:
            print('Valor excede o saldo atual!')
            return False

    def fazerSaque(self, valor_saque):
        if self.verSaldoLimite(valor_saque) == True:
            self.saldo -= valor_saque
            self.limite -= valor_saque
            print('Saque liberado!')
            return True
        else:
            print('Valor indisponivel para saque!')
            return False
    
    def fazerTransferencia(self, valor_transferencia, conta_destino):
        if valor_transferencia <= 1:
            print('Valor inválido! Valor mínimo R$ 1.00')
        elif self.verSaldoLimite(valor_transferencia) == True:
            self.saldo -= valor_transferencia
            self.limite -= valor_transferencia
            print(f'Transferido(s) R$ {valor_transferencia} para a conta {conta_destino}')


conta1 = Conta('Adriano Matos Meier', '1234-5', 5000.00, 2000.00)
conta2 = Conta('Serj Tankian', '4321-X', 3000.00, 1000.00)

# Conta1 - Transferencia acima do limite diario
print('-----------------------------------------')
print('Retorno Transferencia - Transação 1')
conta1.fazerTransferencia(2390, '4321-X')

# Conta1 - Transferencia abaixo do valor minimo
print('-----------------------------------------')
print('Retorno Transferencia - Transação 2')
conta1.fazerTransferencia(0.5, '4321-X')

# Conta1 - Transferencia dentro do limite/saldo
print('-----------------------------------------')
print('Retorno Transferencia - Transação 3')
conta1.fazerTransferencia(390, '4321-X')
print('-----------------------------------------')

# Conta2 - Recebe transferencia (deposito)
conta2.fazerDeposito(390)

# Mostra saldo das contas após movimentações
print('\n-----------------------------------------')
conta1.mostraSaldo()
print('-----------------------------------------')
conta2.mostraSaldo()
print('-----------------------------------------')
