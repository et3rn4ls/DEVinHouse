class Transacoes {
    constructor(conta, valorDaTransacao, saldo) {
        this.conta = conta,
        this.valorDaTransacao = valorDaTransacao,
        this.saldo = saldo
    }

    set transfere(valor) {
        this.saldo = this.saldo - valor;
    }

    set deposita(valor) {
        this.saldo = this.saldo + valor;
    }

    get novoSaldo() {
        return this.saldo;
    }
}

let conta1 = new Transacoes('1234-5', 0, 1000);
console.log(`O saldo da conta ${conta1.conta} é R$${conta1.novoSaldo},00.`);
valorDaTransacao = 810;
conta1.transfere = valorDaTransacao;
console.log(`O saldo da conta ${conta1.conta} é R$${conta1.novoSaldo},00.`);
valorDaTransacao = 580;
conta1.deposita = valorDaTransacao;
console.log(`O saldo da conta ${conta1.conta} é R$${conta1.novoSaldo},00.`);

console.log('-----------------------------------');

let conta2 = new Transacoes('5432-1', 0, 1000);
console.log(`O saldo da conta ${conta2.conta} é R$${conta2.novoSaldo},00.`);
valorDaTransacao = 150;
conta2.transfere = valorDaTransacao;
console.log(`O saldo da conta ${conta2.conta} é R$${conta2.novoSaldo},00.`);
valorDaTransacao = 320;
conta2.deposita = valorDaTransacao;
console.log(`O saldo da conta ${conta2.conta} é R$${conta2.novoSaldo},00.`);


