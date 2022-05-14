<template>
  <div class="container">
    <h3>Cadastro de Pessoa</h3>
    <hr>
    <div class="row g-2">
      <div class="col-md-4">
        <label for="nome">Nome Completo: </label>
        <input class="nome" type="text" v-model="nome">
      </div>
      <div class="col-3">
        <label for="dataNascimento">Data de Nascimento: </label>
        <input class="dataNascimento" type="date" v-model="dataNascimento">
      </div>
      <div class="col-3">
        <label for="cep">CEP: </label>
        <input class="cep" type="number" placeholder="Ex: 88123000" v-model="cep">
      </div>
      <div class="col-2">
        <button type="button" class="btn btn-outline-success btn-sm" @click="cadastrarPessoa">Cadastrar</button>
      </div>
    </div>
    <hr>
    <span class="badge bg-info" v-text="retorno"></span>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      id: '',
      nome: '',
      dataNascimento: '',
      cep: '',
      users: [],
      user: {},
      retorno: ''
    }
  },
  methods: {
    async buscaUser() {
      const promise = axios.get(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`)
        await promise.then((response) => {
          this.user = response.data;
        }).catch((err) => {
          this.retorno = err;
        });
    },
    cadastrarPessoa() {
      axios.post('https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users', {
        nome: `${this.nome}`,
        dataNascimento: `${this.dataNascimento}`,
        cep: `${this.cep}`
      }).then((response) => {
        this.retorno = response.statusText;
      }).catch((err) => {
        this.retorno = err;
      });
    },
    updateUser() {
      axios.put(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`, {
        nome: `${this.nome}`,
        email: `${this.email}`
      }).then((response) => {
        this.retorno = response.data;
      }).catch((err) => {
        this.retorno = err;
      });
    },
    deleteUser() {
      axios.delete(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`)
        .then((response) => {
          this.retorno = response.data;
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