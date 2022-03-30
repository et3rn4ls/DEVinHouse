async function aguarda3Segundos() {
    await new Promise(resolve => setTimeout(resolve, 3000));
    console.log('Função diz: Terminei!');
}

async function euNaoEspero() {
    aguarda3Segundos();
    console.log("Eu não espero!");
}

async function euEspero() {
    await aguarda3Segundos();
    console.log("Eu espero!");
}

euEspero();
euNaoEspero();