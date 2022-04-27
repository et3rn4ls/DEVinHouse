<template>
    <div class="busca-cep">
        <h1>M1S07 - Exercicio 6</h1>
        <hr>
        <label>Informe o CEP</label><br>
        <input type="texto" placeholder="Ex: 88123000" v-model="cep">
        <br><br>
        <button type="button" class="btn btn-outline-primary btn-sm" @click="buscaCEP">Consultar</button>
        <br><br>
        <pre v-text="retorno"></pre>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cep: null,
            retorno: null
        }
    },
    methods: {
        async buscaCEP() {
            try {
                let response = await fetch(`https://viacep.com.br/ws/${this.cep}/json`);
                if (response.ok) {
                    let conteudo = await response.json();
                    if (conteudo.localidade) {
                        this.retorno = 'Cidade: ' + conteudo.localidade + '\n' +
                                       'Logradouro: ' + conteudo.logradouro + '\n' +
                                       'Bairro: ' + conteudo.bairro + '\n' +
                                       'Estado: ' + conteudo.uf;
                    } else {
                        this.retorno = 'CEP incorreto ou não localizado!';
                    }
                }
            }
            catch (err) {
                this.retorno = `Ocorreu um erro: ${err}!`
            }
        }
    }
}
</script>

<style>

</style>