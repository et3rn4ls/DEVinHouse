// Função tradicional -  assim eu já sei brincar! =)

// document.getElementById("enviar").addEventListener('click', mensagemOla);

// function mensagemOla() {
//     const nome = document.getElementById("nome").value;
//     document.getElementById("retorno").innerHTML = `Olá, ${nome}!`;
// }

// =====================================================================

// Arrow function v1 - opaaaa... primeira vez que funciona com arrow function!

// const mensagemOla = () => {
//     const nome = document.getElementById("nome").value;
//     document.getElementById("retorno").innerHTML = `Olá, ${nome}!`;
// }

// document.getElementById("enviar").addEventListener("click", mensagemOla);

// =====================================================================

// Arrow function v2 - tentando umas coisas diferentes e pior que deu boaaaaaa!

// const mensagemOla = () => {
//     document.getElementById("retorno").innerHTML = `Olá, ${document.getElementById("nome").value}!`;
// }

// document.getElementById("enviar").addEventListener("click", mensagemOla);

// =====================================================================

// Arrow function v3 - creeeedooo.... esse guri vai longe! =D

const mensagemOla = () => document.getElementById("retorno").innerHTML = `Olá, ${document.getElementById("nome").value}!`;
document.getElementById("enviar").addEventListener("click", mensagemOla);