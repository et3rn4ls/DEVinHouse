<template>
    <div class="app">
        <h3 v-text="msg"></h3>
        <hr>
        <label :style="`color:${corTexto}`">Cor</label>
        <br>
        <input type="text" v-model="corTexto">
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 4',
      corTexto: null
    }
  }
}
</script>

<style>
body {
  text-align: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
h3 {
    color:slategray;
}
</style>
