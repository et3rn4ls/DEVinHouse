class Cliente {
    constructor(nome, cpf, endereco, celular) {
        this.nome = nome;
        this.cpf = cpf;
        this.endereco = endereco;
        this.celular = celular;
    }

    validaCPF() {
        if (this.cpf.length != 11) {
            return "invalido";
        } else {
            return "valido";
        }
    }
}

let enviar = document.getElementById("enviar");
enviar.addEventListener('click', addCliente);

function addCliente() {
    const nome = document.getElementById("nome").value;
    const cpf = document.getElementById("cpf").value;
    const endereco = document.getElementById("endereco").value;
    const celular = document.getElementById("celular").value;

    const cliente = new Cliente(`${nome}`, `${cpf}`, `${endereco}`, `${celular}`);

    if (cliente.validaCPF() === "valido") {
        document.getElementById("nome").value = '';
        document.getElementById("cpf").value = '';
        document.getElementById("endereco").value = '';
        document.getElementById("celular").value = '';
        document.getElementById("retorno").innerHTML = `CPF válido! <BR> Cliente cadastrado com sucesso!`;
        setTimeout(function() {
            document.getElementById("retorno").innerHTML = '';
        }, 3000)
    } else if (cliente.validaCPF() === "invalido") {
        document.getElementById("cpf").value = '';
        document.getElementById("retorno").innerHTML = `CPF invalido! <BR> Digite apenas números!`;
        setTimeout(function() {
            document.getElementById("retorno").innerHTML = '';
        }, 3000)
    }
}
