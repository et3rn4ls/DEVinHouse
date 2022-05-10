<template>
  <div class="listagem">
      <h3>Listagem</h3>
      <br><br>
      <div>
        <button type="button" class="btn btn-outline-primary btn-sm" @click="buscarPessoas">Listar Pessoas</button>
      </div>
      <div>{{ listaPessoas }}</div>
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