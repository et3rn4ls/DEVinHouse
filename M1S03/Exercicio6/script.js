var calc = document.getElementById("calc");
calc.addEventListener('click', calculaIdade);

function calculaIdade() {  
    let hoje = new Date;  
    let nascimento = new Date(document.getElementById('nasc').value);
    var anos = hoje.getFullYear() - nascimento.getFullYear();

    if (hoje.getMonth() != nascimento.getMonth()) {
        if (hoje.getMonth() < nascimento.getMonth()) {
            anos--;
        }
    }
    else {
        if (hoje.getDate() < nascimento.getDate()) {
            anos--;
        }
    }

    document.getElementById('retorno').innerHTML = `Você tem ${anos} anos!`;
}
