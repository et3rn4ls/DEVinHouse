<template>
    <div class="app">
        <h1 v-once v-text="msg"></h1>
        <input type="text" v-model="msg">
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 2'
    }
  }
}
</script>

<style>
</style>
