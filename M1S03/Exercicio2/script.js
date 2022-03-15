function checkNumber() {
    var numero = parseInt(document.getElementById("number").value);
    const parImpar = numero % 2 === 0 
        ? document.getElementById("retorno").innerHTML = `O número ${numero} é par!`
        : document.getElementById("retorno").innerHTML = `O número ${numero} é impar!`
}
