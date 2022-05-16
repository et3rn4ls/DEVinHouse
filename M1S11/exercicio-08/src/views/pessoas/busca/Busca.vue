<template>
    <div class="container">
      <h3>Buscar Pessoa</h3>
      <hr>
      <div class="col-12" v-show="errorMsg.length > 0">
        <span class="badge bg-danger"> {{ errorMsg }}</span>
        <hr>
      </div>
      <div class="row g-2">
        <div class="col-md-4">
          <label for="id">Informe o ID: </label>
          <input class="id" type="number" v-model="id">
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-outline-success btn-sm" @click="buscarPessoa">Consultar</button>
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-outline-primary btn-sm" @click="listarTodas">Listar todas</button>
        </div>
        <div v-if="retorno.length !== 0">
          <hr>
          <pre v-text="retorno"></pre>
        </div>
      </div>
      <hr>
      <table class="table" v-if="listaPessoas.length !== 0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Data de Nascimento</th>
            <th>CEP</th>
            <th>Remover</th>
          </tr>
        </thead>
        <transition-group name="lista" tag="tbody">
          <tr v-for="p in listaPessoas" :key="p.id">
            <td v-text="p.id"></td>
            <td v-text="p.nome"></td>
            <td v-text="p.dataNascimento"></td>
            <td v-text="p.cep"></td>
            <td>
              <button type="button" class="btn btn-danger btn-sm" @click="excluirPessoa(p.id)">Excluir</button>
            </td>
          </tr>
        </transition-group>
      </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      id: '',
      listaPessoas: [],
      retorno: '',
      errorMsg: ''
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
          this.errorMsg = 'Ocorreu um erro: ' + err;
        });
    },
    listarTodas() {
      const promise = axios.get('https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users')
        promise.then((response) => {
          this.listaPessoas = response.data;
        }).catch((err) => {
          this.errorMsg = 'Ocorreu um erro: ' + err;
        });
    },
    excluirPessoa(id) {
      axios.delete(`https://627c406ebf2deb7174d8017a.mockapi.io/api/v1/users/${id}`)
        .then((response) => {
          this.retorno = 'Cadastro excluído: ' + response.data.nome;
          this.listarTodas();
        }).catch((err) => {
          this.errorMsg = 'Ocorreu um erro: ' + err;
        });
    }
  }
}
</script>

<style>
h3 {
  text-align: center;
}

.zerado {
  text-align: center;
}

.lista-leave-to,
.lista-enter-from {
  opacity: 0;
}

.lista-leave-from,
.lista-enter-to {
  opacity: 1;
}

.lista-move,
.lista-leave-active,
.lista-enter-active {
  transition: all 2s ease;
}
</style>