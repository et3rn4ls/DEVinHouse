<template>
  <div id="app">
      <CronCrontrol />
  </div>
</template>

<script>
import CronCrontrol from './components/CronControl.vue'

export default {
  name: 'App',
  components: {
    CronCrontrol
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
