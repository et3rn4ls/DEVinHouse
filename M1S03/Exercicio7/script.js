window.addEventListener("load", verEstacao);

function verEstacao() {
    let hoje = new Date;
    var dia = hoje.getDate();
    var mes = hoje.getMonth();
    
    const mesesVerao = [0, 1, 2];
    const mesesOutono = [3, 4, 5];
    const mesesInverno = [6, 7, 8];
    const mesesPrimavera = [9, 10, 11];

    if (dia >= 22 && mes === 11 || dia <= 21 && mesesVerao.includes(mes)) {
        document.getElementById("retorno").innerHTML = "Verão";
        document.getElementById("image").src="img/verao.jpg";
    } else if (dia >= 22 && mes === 2 || dia <= 21 && mesesOutono.includes(mes)) {
        document.getElementById("retorno").innerHTML = "Outono";
        document.getElementById("image").src="img/outono.jpg";
    } else if (dia >= 22 && mes === 5 || dia <= 21 && mesesInverno.includes(mes)) {
        document.getElementById("retorno").innerHTML = "Inverno";
        document.getElementById("image").src="img/inverno.jpg";
    } else if (dia >= 22 && mes === 8 || dia <= 21 && mesesPrimavera.includes(mes)) {
        document.getElementById("retorno").innerHTML = "Primavera";
        document.getElementById("image").src="img/primavera.jpg";
    }
}
