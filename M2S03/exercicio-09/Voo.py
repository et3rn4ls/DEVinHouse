class Voo:
    
    def __init__(self, numero = 1456, origem = 'FLN', destino = 'GRU', assentos = 30, valor = 450.00):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.assentos = assentos
        self.valor = valor
    
    def getAsseDisp(self):
        return self.assentos
    

class Reserva(Voo):
    desc25 = 0
    desc15 = 0
    desc05 = 0
    nodesc = 0
    assentos_desc25 = list(range(1,10+1))
    assentos_desc15 = list(range(11,15+1))
    assentos_desc05 = list(range(16,20+1))
    assentos_nodesc = list(range(21,30+1))

    def __init__(self, codigo = 1456, valor_cobrado = 0, assentos = 30):
        super().__init__(assentos)
        self.codigo = codigo
        self.valor_cobrado = valor_cobrado
        self.valor_arrecadado = 0

    def valorArrecadado(self):
        return self.valor_arrecadado

    def fazerReserva(self, assento):
        if self.assentos == 0:
            print(f'O avião do voo {self.numero} - {self.origem}-{self.destino} está lotado!')
        elif assento in range(1-10):
            if assento in self.assentos_desc25:
                self.valor_cobrado += (self.valor - 0.25)
                self.valor_arrecadado += self.valor_cobrado
                self.desc25 += 1
                self.assentos -= 1
                self.assentos_desc25.remove(assento)
                print(f'Reserva efetuada! Assento: {assento} - Valor: R$ {self.valor_cobrado}')
            else:
                print(f'Poltrona indisponível!')
        elif assento in range(11-15):
            if assento in self.assentos_desc15:
                self.valor_cobrado += (self.valor - 0.15)
                self.valor_arrecadado += self.valor_cobrado
                self.desc15 += 1
                self.assentos -= 1
                self.assentos_desc15.remove(assento)
                print(f'Reserva efetuada! Assento: {assento} - Valor: R$ {self.valor_cobrado}')
            else:
                print(f'Poltrona indisponível!')
        elif assento in range(16-20):
            if assento in self.assentos_desc05:
                self.valor_cobrado += (self.valor - 0.05)
                self.valor_arrecadado += self.valor_cobrado
                self.desc05 += 1
                self.assentos_desc05.remove(assento)
                print(f'Reserva efetuada! Assento: {assento} - Valor: R$ {self.valor_cobrado}')
            else:
                print(f'Poltrona indisponível!')
        elif assento in range(21-30):
            if assento in self.assentos_nodesc:
                self.valor_cobrado += self.valor
                self.valor_arrecadado += self.valor_cobrado
                self.nodesc += 1
                self.assentos_nodesc.remove(assento)
                print(f'Reserva efetuada! Assento: {assento} - Valor: R$ {self.valor_cobrado}')
            else:
                print(f'Poltrona indisponível!')

    def assentosLivres(self):
        print(f'Assentos com 25% de desconto: {self.assentos_desc25}')
        print(f'Assentos com 15% de desconto: {self.assentos_desc15}')
        print(f'Assentos com 5% de desconto: {self.assentos_desc05}')
        print(f'Assentos sem desconto: {self.assentos_nodesc}')
    
