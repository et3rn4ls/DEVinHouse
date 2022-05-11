<template>
  <div class="container">
    <h2>M1S11 - Exercício 01</h2>
    <hr>
    <label for="cep">Informe o CEP: </label>
    <input class="cep" type="number" placeholder="Ex: 88123000" v-model="cep">
    <br><br>
    <button type="button" class="btn btn-outline-success btn-sm" @click="buscaCEP">Consultar</button>
    <hr>
    <pre v-text="retorno"></pre>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cep: null,
      retorno: null
    }
  },
  methods: {
    async buscaCEP() {
      const promise = axios.get(`https://viacep.com.br/ws/${this.cep}/json`)
        await promise.then((response) => {
          let conteudo = response.data;
            if (conteudo.localidade) {
              this.retorno = 'Cidade: ' + conteudo.localidade + '\n' +
                             'Logradouro: ' + conteudo.logradouro + '\n' +
                             'Bairro: ' + conteudo.bairro + '\n' +
                             'Estado: ' + conteudo.uf;
            } else {
              this.retorno = 'CEP incorreto ou não localizado!';
            }
        }).catch((err) => {
          this.retorno = err;
        });
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
