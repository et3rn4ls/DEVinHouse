<template>
  <div class="container">
      <h3>Listagem</h3>
      <br><br>
      <div>
        <button type="button" class="btn btn-outline-primary btn-sm" @click="buscarPessoas">Listar Pessoas</button>
      </div>
      <hr>
      <div class="zerado" v-if="listaPessoas.length === 0">
        Não há pessoas cadastradas
      </div>

      <table class="table" v-else>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Data Nascimento</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in listaPessoas" :key="p.id">
            <td v-text="p.nome"></td>
            <td v-text="p.dataNascimento"></td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      listaPessoas: []
    }
  },
  methods: {
    buscarPessoas() {
      this.listaPessoas = this.$store.state.pessoas;
    }
  }
}
</script>

<style>

</style>