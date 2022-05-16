<template>
  <div class="container">
    <h3>Cadastro de Pessoa</h3>
    <hr>
    <vee-form @submit="cadastrarPessoa" :validation-schema="schema" v-slot="{ errors }">
      <div class="row g-2">
        <div class="col-md-4">
          <label for="nome">Nome Completo: </label>
          <vee-field name="nome" class="nome" type="text" v-model="nome" />
          <span class="text-danger" v-text="errors.nome" v-show="errors.nome"></span>
        </div>
        <div class="col-3">
          <label for="dataNascimento">Data de Nascimento: </label>
          <vee-field name="dataNascimento" class="dataNascimento" type="date" v-model="dataNascimento" />
          <span class="text-danger" v-text="errors.dataNascimento" v-show="errors.dataNascimento"></span>
        </div>
        <div class="col-3">
          <label for="cep">CEP: </label>
          <vee-field name="cep" class="cep" type="number" placeholder="Ex: 88123000" v-model="cep" />
          <span class="text-danger" v-text="errors.cep" v-show="errors.cep"></span>
        </div>
        <div class="col-2">
          <button type="submit" class="btn btn-outline-success btn-sm">Cadastrar</button>
          <button type="button" class="btn btn-outline-info btn-sm" @click="atualizarPessoa">Atualizar</button>
        </div>
      </div>
    </vee-form>
    <div v-if="retorno.length !== 0">
      <hr>
      <span class="badge bg-info" v-text="retorno"></span>
    </div>
    <hr>
    <h5>Atualizar cadastro</h5>
    <div class="row g-2">
      <div class="col-md-4">
        <label for="id">Informe o ID: </label>
        <input class="id" type="number" v-model="id">
      </div>
      <div class="col-2">
        <button type="button" class="btn btn-outline-success btn-sm" @click="buscarPessoa">Consultar</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Form, Field, defineRule } from 'vee-validate';

defineRule("required", value => {
  if (!value || value.length === 0) {
    return "Campo obrigatório";
  }
  return true;
});

defineRule("dataNasc", value => {
  if (new Date(value + ' 00:00:00') <= new Date()) {
    return true;
  } else {
    return "Não pode ser superior a data atual";
  }
});

defineRule("nomeCompleto", value => {
  let regexp = /^[a-zA-Z]{2,}( [a-zA-Z]+)*?( [a-zA-Z]{2,}){1,}$/

  if (!regexp.test(value)) {
    return "Favor informar o nome completo";
  }
  return true;
});

defineRule("validaCEP", value => {
  let regexp = /^[0-9]{8}$/

  if (!regexp.test(value)) {
    return "Formato de CEP inválido! Informe 8 números. Exemplo: 88132373";
  }
  return true;
});

export default {
  components: {
    'vee-form': Form,
    'vee-field': Field
  },
  data() {
    return {
      schema: {
        nome: "required|nomeCompleto",
        dataNascimento: "required|dataNasc",
        cep: "required|validaCEP"
      },
      id: '',
      nome: '',
      dataNascimento: '',
      cep: '',
      retorno: ''
    }
  },
  methods: {
    cadastrarPessoa() {
      axios.post('https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users', {
        nome: `${this.nome}`,
        dataNascimento: `${this.dataNascimento}`,
        cep: `${this.cep}`
      }).then((response) => {
        this.retorno = "Cadastro realizado com sucesso";
      }).catch((err) => {
        this.retorno = err;
      });
        this.nome = '';
        this.dataNascimento = '';
        this.cep = '';
    },
    async buscarPessoa() {
      const promise = axios.get(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`)
        await promise.then((response) => {
          this.nome = response.data.nome;
          this.dataNascimento = response.data.dataNascimento;
          this.cep = response.data.cep;
        }).catch((err) => {
          this.retorno = 'ID não localizado!';
        });
    },
    atualizarPessoa() {
      axios.put(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${this.id}`, {
        nome: `${this.nome}`,
        dataNascimento: `${this.dataNascimento}`,
        cep: `${this.cep}`
      }).then((response) => {
        this.retorno = "Cadastro atualizado com sucesso!"
      }).catch((err) => {
        this.retorno = 'Informe o ID do usuário no formulário abaixo e pressione o botão "Consultar"';
      });
        this.nome = '';
        this.dataNascimento = '';
        this.cep = '';
    },
  }
}
</script>

<style>
h5,
h3 {
  text-align: center;
}
</style>