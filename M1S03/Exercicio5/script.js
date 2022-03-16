var data = new Date();
var hora = data.getHours();
var minuto = data.getMinutes();

hora = zero(hora);
minuto = zero(minuto);

function zero(x) {
    if (x < 10) {
        x = '0' + x;
    } return x;
}

document.getElementById('acesso').innerHTML = `Horário do acesso: ${hora}:${minuto}`;

setInterval(function() {
    var data = new Date();
    var hora = data.getHours();
    var minuto = data.getMinutes();

    hora = zero(hora);
    minuto = zero(minuto);

    document.getElementById('relogio').innerHTML = `Relógio: ${hora}:${minuto}`;
}, 1000);

