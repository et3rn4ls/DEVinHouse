export default class Pessoa {
    #cpf;
    constructor(nome, cpf) {
        this.nome = nome;
        this.#cpf = cpf;
    }
    
    imprime() {
        console.log(`Nome: ${this.nome} - CPF: ${this.#cpf}`);
    }
}
