class Transacoes {
    constructor(conta, valorDaTransacao, saldo, idDeTransferencia, numeroDaConta, data) {
        this.conta = conta,
        this.valorDaTransacao = valorDaTransacao,
        this.saldo = saldo,
        this.idDeTransferencia = idDeTransferencia,
        this.numeroDaConta = numeroDaConta,
        this.data = data
    }

    set transfere(valor) {
        this.valorDaTransacao = valor;
        this.saldo -= valor;
        this.data = this.currentDate;
        this.idDeTransferencia = this.newID;
    }

    set deposita(valor) {
        this.valorDaTransacao = valor;
        this.saldo += valor;
        this.data = this.currentDate;
        this.idDeTransferencia = this.newID;
    }

    get novoSaldo() {
        return this.saldo;
    }

    get currentDate() {
        return new Date().toLocaleString();
    }

    get newID() {
        return this.idDeTransferencia + 1;
    }
}

let conta1 = new Transacoes('1234-5', 0, 1000, 0, '9876-5');
console.log(`O saldo da conta ${conta1.conta} em ${conta1.currentDate} é R$${conta1.novoSaldo},00.`);

let conta2 = new Transacoes('5432-1', 0, 2000, 0, '6669-X');
console.log(`O saldo da conta ${conta2.conta} em ${conta1.currentDate} é R$${conta2.novoSaldo},00.`);

console.log('------------------------------------------------------------------------');

setTimeout(function() {
    valorDaTransacao = 810;
    conta1.transfere = valorDaTransacao;
    console.log(`ID: ${conta1.idDeTransferencia} - Transferência realizada em ${conta1.data} no valor de R$${conta1.valorDaTransacao},00 - CC Origem: ${conta1.conta} / CC Destino: ${conta1.numeroDaConta}`);
    console.log(`O saldo da conta ${conta1.conta} em ${conta1.currentDate} é R$${conta1.novoSaldo},00.`);
}, 2000)

setTimeout(function() {
    valorDaTransacao = 580;
    conta1.deposita = valorDaTransacao;
    console.log(`ID: ${conta1.idDeTransferencia} - Depósito em conta ${conta1.conta} realizado em ${conta1.data} no valor de R$${conta1.valorDaTransacao},00.`);
    console.log(`O saldo da conta ${conta1.conta} em ${conta1.currentDate} é R$${conta1.novoSaldo},00.`);
}, 4000)

setTimeout(function() {
    valorDaTransacao = 90;
    conta1.deposita = valorDaTransacao;
    console.log(`ID: ${conta1.idDeTransferencia} - Depósito em conta ${conta1.conta} realizado em ${conta1.data} no valor de R$${conta1.valorDaTransacao},00.`);
    console.log(`O saldo da conta ${conta1.conta} em ${conta1.currentDate} é R$${conta1.novoSaldo},00.`);
}, 6000)

setTimeout(function() {
valorDaTransacao = 150;
conta2.transfere = valorDaTransacao;
console.log(`ID: ${conta2.idDeTransferencia} - Transferência realizada em ${conta2.data} no valor de R$${conta2.valorDaTransacao},00 - CC Origem: ${conta2.conta} / CC Destino: ${conta2.numeroDaConta}`);
console.log(`O saldo da conta ${conta2.conta} em ${conta1.currentDate} é R$${conta2.novoSaldo},00.`);
}, 8000)

setTimeout(function() {
valorDaTransacao = 320;
conta2.deposita = valorDaTransacao;
console.log(`ID: ${conta2.idDeTransferencia} - Depósito em conta ${conta2.conta} realizado em ${conta2.data} no valor de R$${conta2.valorDaTransacao},00.`);
console.log(`O saldo da conta ${conta2.conta} em ${conta1.currentDate} é R$${conta2.novoSaldo},00.`);
}, 12000)

setTimeout(function() {
valorDaTransacao = 450;
conta2.deposita = valorDaTransacao;
console.log(`ID: ${conta2.idDeTransferencia} - Depósito em conta ${conta2.conta} realizado em ${conta2.data} no valor de R$${conta2.valorDaTransacao},00.`);
console.log(`O saldo da conta ${conta2.conta} em ${conta1.currentDate} é R$${conta2.novoSaldo},00.`);
}, 14000)

setTimeout(function() {
    console.log('Sem mais transações');
    }, 15000)
