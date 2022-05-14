<template>
    <div class="container">
      <h3>Buscar Pessoa</h3>
      <hr>
      <div class="row g-2">
        <div class="col-md-4">
          <label for="id">Informe o ID: </label>
          <input class="id" type="number" v-model="id">
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-outline-success btn-sm" @click="buscarPessoa">Consultar</button>
        </div>
        <hr>
        <pre v-text="retorno"></pre>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      id: '',
      retorno: ''
    }
  },
  methods: {
    async buscarPessoa() {
      const promise = axios.get(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`)
        await promise.then((response) => {
          this.retorno = 'Nome: ' + response.data.nome + '\n' +
                         'Data de nascimento: ' + response.data.dataNascimento + '\n' +
                         'CEP: ' + response.data.cep;
        }).catch((err) => {
          this.retorno = err;
        });
    }
  }
}
</script>

<style>
h3 {
  text-align: center;
}
</style>