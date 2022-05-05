<template>
  <div class="container">
    <h2>M1S10 - Exercício 04</h2>
    <hr>
      <form @submit.prevent="salvar">
        <div class="row g-2">
          <div class="col-md-2">
            <label for="">Nome</label>
            <input type="text" v-model="pessoa.nome">
          </div>
          <div class="col-md-2">
            <label for="">Data Nascimento</label>
            <input type="date" v-model="pessoa.dataNascimento">
          </div>
          <div class="col-sm-12">
            <button type="submit" class="btn btn-outline-primary btn-sm">Adicionar</button>
          </div>
        </div>
    </form>
    <hr>
    <div v-if="pessoas.length === 0">
      Não há pessoas cadastradas
    </div>
    <table class="table" v-else>
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">Idade</th>
          </tr>
        </thead>
        <transition-group name="lista" tag="tbody">
            <tr v-for="(p, index) in pessoas" :key="p.id">
              <td v-text="p.nome"></td>
              <td v-text="p.idade"></td>
              <td>
                <button class="btn btn-outline-danger btn-sm" @click="removePessoa(index)">Excluir</button>
              </td>
          </tr>
        </transition-group>
    </table>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      pessoas: [],
      pessoa: {}
    }
  },
  methods: {
    salvar() {
      this.calculaIdade();
      this.pessoa.id = this.pessoas.length + 1;
      this.pessoas.push(this.pessoa);
      this.pessoas.sort((x, y) => {
        return x.idade - y.idade;
      });
      this.pessoa = {};
    },
    calculaIdade() {
      let hoje = new Date;
      let nascimento = new Date(this.pessoa.dataNascimento);
      let anos = hoje.getFullYear() - nascimento.getFullYear();

      if (hoje.getMonth() != nascimento.getMonth()) {
          if (hoje.getMonth() < nascimento.getMonth()) {
              anos--;
          }
      }
      else {
          if (hoje.getDate() < nascimento.getDate()) {
              anos--;
          }
      }
      this.pessoa.idade = anos;
    },
    removePessoa(index) {
      this.pessoas.splice(index, 1);
    }
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  h2 {
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
