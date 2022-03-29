const produtos = [
    { nome: 'arroz', preco: 9 },
    { nome: 'feijao', preco: 12 },
    { nome: 'batata', preco: 8 },
    { nome: 'macarrao', preco: 5 }
];

const buscaProduto = () => {
    const prod  = produtos.find(prod => prod.nome === document.getElementById("produto").value);

    if (prod) {
        document.getElementById("retorno").innerHTML = `Produto: ${prod.nome} - Preço: R$${prod.preco},00!`;
    } else {
        document.getElementById("retorno").innerHTML = 'Produto não encontrado!';
    }
};

const somaPrecos = () => {
    const prodPreco = produtos.map(obj => obj.preco);

    const valorInicial = 0;
    const somaTotal = prodPreco.reduce(
        (valorAnterior, valorAtual) => valorAnterior + valorAtual,
        valorInicial
    );

    document.getElementById("soma").innerHTML = `Valor total dos produtos: R$ ${somaTotal},00!`;
};

document.getElementById("buscar").addEventListener("click", buscaProduto);
document.getElementById("somar").addEventListener("click", somaPrecos);