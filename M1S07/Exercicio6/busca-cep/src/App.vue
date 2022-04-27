<template>
  <div class="app">
      <BuscaCEP />
  </div>
</template>

<script>
import BuscaCEP from './components/BuscaCEP.vue'

export default {
  name: 'App',
  components: {
    BuscaCEP
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
