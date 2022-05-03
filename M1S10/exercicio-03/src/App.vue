<template>
  <div class="app">
    <h2>M1S10 - Exercício 03</h2>
    <hr>
    <div>
      <button @click="show = !show">Alterar estado</button>
      <br><br>
      <transition name="header" mode="out-in">
        <header v-if="show">Apresentando o H1</header>
        <span v-else>O header não está disponível</span>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: true
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

.header-leave-to,
.header-enter-from {
  opacity: 0;
}

.header-leave-active,
.header-enter-active {
  transition: opacity 2s;
}

.header-leave-from,
.header-enter-to {
  opacity: 1;
}
</style>
