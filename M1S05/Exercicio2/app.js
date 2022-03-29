const arrayNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let arrayQuadrados = arrayNumeros.map(n => n ** 2);

if (arrayQuadrados.length == arrayNumeros.length) {
    console.log(arrayQuadrados);
}

const resultado = arrayQuadrados.filter(n => n > 30);
console.log(resultado);
