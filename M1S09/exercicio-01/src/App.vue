<template>
    <div class="exercicio">
        <h1 v-text="msg"></h1>
        <input type="text" v-model="msg">
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 1'
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
