function somaNum() {
    let num1 = parseInt(document.getElementById('num1').value);
    let num2 = parseInt(document.getElementById('num2').value);
    let resultado = num1 + num2;
    document.getElementById('resultado').readOnly = false;
    document.getElementById('resultado').value = resultado;
    document.getElementById('resultado').readOnly = true;
}

function subNum() {
    let num1 = parseInt(document.getElementById('num1').value);
    let num2 = parseInt(document.getElementById('num2').value);
    let resultado = num1 - num2;
    document.getElementById('resultado').readOnly = false;
    document.getElementById('resultado').value = resultado;
    document.getElementById('resultado').readOnly = true;
}

function multNum() {
    let num1 = parseInt(document.getElementById('num1').value);
    let num2 = parseInt(document.getElementById('num2').value);
    let resultado = num1 * num2;
    document.getElementById('resultado').readOnly = false;
    document.getElementById('resultado').value = resultado;
    document.getElementById('resultado').readOnly = true;
}

function divNum() {
    let num1 = parseInt(document.getElementById('num1').value);
    let num2 = parseInt(document.getElementById('num2').value);
    let resultado = num1 / num2;
    document.getElementById('resultado').readOnly = false;
    document.getElementById('resultado').value = resultado;
    document.getElementById('resultado').readOnly = true;
}
