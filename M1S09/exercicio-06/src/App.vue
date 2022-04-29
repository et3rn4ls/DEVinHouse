<template>
    <div class="app">
        <h3 v-text="msg"></h3>
        <hr>
          <div class="mt-2">
            <ul type="none">
              <li v-for="(item, index) in lista" :key="index">
                {{ item }}
              </li>
            </ul>
          </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 6',
      lista: ['Item 01', 'Item 02', 'Item 03']
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
  color:slategray;
}
</style>
