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
            return False
        elif self.verSaldoLimite(valor_transferencia) == True:
            self.saldo -= valor_transferencia
            self.limite -= valor_transferencia
            print(f'Transferido(s) R$ {valor_transferencia} para a conta {conta_destino}')
            return True
            
