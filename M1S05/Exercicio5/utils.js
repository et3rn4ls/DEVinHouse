export function somaNumeros(...n) {
    return n.reduce((valorAnterior, valorAtual) => valorAnterior + valorAtual, 0);
}
