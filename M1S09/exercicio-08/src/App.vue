<template>
  <div class="container">
    <h3>Formulário:</h3>
    <form @submit.prevent="salvar">
      <div class="row g-2">
        <div class="col-md-2">
          <label for="">Nome</label>
          <input type="text" v-model="pessoa.nome">
        </div>
        <div class="col-md-2">
          <label for="">Idade</label>
          <input type="number" v-model="pessoa.idade">
        </div>
        <div class="col-sm-12">
          <button type="submit" class="btn btn-primary btn-sm">Adicionar</button>
        </div>
      </div>
    </form>
    <hr>
    <h3>Lista:</h3>
    <div v-if="pessoas.length === 0">
      Não há informações cadastradas
    </div>
    <table class="table" v-else>
        <thead>
          <tr>
            <th scope="col">Nome</th>
            <th scope="col">Idade</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(p, i) in pessoas" :key="i">
            <td v-text="p.nome"></td>
            <td v-text="p.idade"></td>
          </tr>
        </tbody>
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
      this.pessoa.id = this.pessoas.length + 1;
      this.pessoas.push(this.pessoa);
      this.pessoa = {};
    }
  }
}
</script>

<style>
</style>
