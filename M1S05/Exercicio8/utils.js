export function calculaTotal(...obj) {
    const produtos = Object.values(obj);
    const calc = produtos.reduce((acc, prod) => acc + (prod.qtd * prod.valor),0);    
    return calc;
}