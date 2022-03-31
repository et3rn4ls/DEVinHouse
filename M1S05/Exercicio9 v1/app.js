document.getElementById("consultar").addEventListener("click", buscaCEPpromise);

function buscaCEPpromise(){
    fetch(`https://viacep.com.br/ws/${document.getElementById("cep").value}/json`)
      .then(resposta => {
        if (resposta.ok) {
          resposta.json()
            .then(conteudo => {
                document.getElementById("retorno").innerHTML = `Cidade: ${conteudo.localidade}`
            })
        }
    })
}