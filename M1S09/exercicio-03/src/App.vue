<template>
    <div class="app">
        <h3 v-once v-text="msg"></h3>
        <hr>
        <p v-html="html"></p>
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 3',
      html: '<html><body><h6>Banner</h6><img src="https://softauthor.com/wp-content/uploads/2020/04/create-a-banner-hero-unit-in-css-1-1024x365.png" style="width:300px"/></body></html>'
    }
  }
}
</script>

<style>
body {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
