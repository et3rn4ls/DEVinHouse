var nome = window.prompt("Informe o seu nome:");
var idade = parseInt(window.prompt("Informe a sua idade:"));
var praticarEsportes = confirm("Quer praticar um esporte?");

if (praticarEsportes) {
    alert(`${nome}, de ${idade} anos, quer praticar esportes`);
} else {
    alert(`${nome}, de ${idade} anos, não quer praticar esportes`);
}
