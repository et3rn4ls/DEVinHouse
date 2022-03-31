document.getElementById("consultar").addEventListener("click", buscaCEPpromise);

async function buscaCEPpromise(){    
    try {
        let response = await fetch(`https://viacep.com.br/ws/${document.getElementById("cep").value}/json`);

        if (response.ok) {
            let conteudo = await response.json();
            if (conteudo.localidade) {
                document.getElementById("retorno").innerHTML = `Cidade: ${conteudo.localidade}`;
            } else {
              document.getElementById("retorno").innerHTML = `CEP incorreto ou não localizado!`
            }
        }        
    }
    catch (err) {
          document.getElementById("retorno").innerHTML = `Ocorreu um erro: ${err}!`
    }
}