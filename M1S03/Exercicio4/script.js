function calculaPA() {
    let inicial = parseInt(document.getElementById('inicial').value);
    let raiz = parseInt(document.getElementById('raiz').value);
    var array = [inicial];

    pa = inicial + raiz;
    array.push(pa);

    for (let i = 0; i < 8; i++) {
        pa = pa + raiz;
        array.push(pa);
    }
    document.getElementById("resultado").innerHTML = `Resultado da PA: ${array}`
}
