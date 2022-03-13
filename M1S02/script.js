var sobrenome = prompt("Por favor, informe o seu sobrenome:");
var nome = prompt("Por favor, informe o seu nome:");
var idade = prompt("Por favor, nos diga a sua idade:");
var cidade = prompt("Por favor, nos diga onde você mora:");
var numIdade = Number(idade.value);

alert(`Valeu ${nome} ${sobrenome}!`);
console.log(`Nome: ${nome} - Idade: ${idade} - Cidade: ${cidade}`);

var cases = document.getElementById("cases");
var sobre = document.getElementById("sobre");
var faq = document.getElementById("faq");
var enviar = document.getElementById("enviar");

cases.addEventListener('click', abreCases);
sobre.addEventListener('click', abreSobre);
faq.addEventListener('click', abreFaq);
enviar.addEventListener('click', enviaContato);

function abreCases() {
    window.open("https://www.youtube.com/watch?v=ZDFMmTuWESc");
}

function abreSobre() {
    alert("Somos a \"Louro José Inc.\", uma empresa que há 2 semanas oferece serviço de treinamento de papagaio. Usamos diferentes tecnologias como: Machine Learning, Big Data e Inteligência Artificial.");
}

function abreFaq() {
    window.open("faq.html");
}

function enviaContato() {
    var email = document.getElementById("email").value;
    var telefone = document.getElementById("telefone").value;

    console.log(`E-mail: ${email} - Telefone: ${telefone}`);

    if (email.length == 0 || telefone.length == 0) {
        alert("Necessário preencher todos os campos do formulário!");
    } else {
        if (window.confirm("Enviar os dados informados?")) {
            alert(`Obrigado por enviar os seus dados ${nome}. Entraremos em contato via WhatsApp pelo número ${telefone}. Enviamos mais informações para o e-mail ${email}.`);
        }
    }
}
