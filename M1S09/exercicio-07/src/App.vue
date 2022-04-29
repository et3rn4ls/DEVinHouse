<template>
  <div class="container">
      <my-header :title="title" v-show="title"></my-header>
      <hr>
      <input type="text" v-model="title">
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'

export default {
  name: 'App',
  components: {
    'my-header': MyHeader
  },
  data() {
    return {
      title: 'M1S09 - Exercício 07'
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
