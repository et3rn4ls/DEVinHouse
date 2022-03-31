document.getElementById("cat").addEventListener("click", novaImagem);

async function novaImagem(){    
    try {
        await fetch('https://api.thecatapi.com/v1/images/search')
            .then(response => response.json())
            .then((data) => {
                let img = data[0].url
                document.getElementById("img").src=`${img}`;
            })
    }
    catch (err) {
          document.getElementById("retorno").innerHTML = `Ocorreu um erro: ${err}!`
    }
}

novaImagem();
