<template>
    <div class="app">
        <h3 v-text="msg"></h3>
        <hr>
        <label v-text="texto" :style="`color:${corTexto}`"></label>
        <br>
        <button class="botao-preto" @click="textoPreto">Mostrar Label Preto</button>
        <button class="botao-vermelho" @click="textoVermelho">Mostrar Label Vermelho</button>
        <button class="botao-azul" @click="textoAzul">Mostrar Label Azul</button>
    </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'M1S09 - Exercício 5',
      corTexto: null,
      texto: 'Texto'
    }
  },
  methods: {
    textoPreto() {
      this.corTexto = 'black';
      this.texto = 'Label Preto';
    },
    textoVermelho() {
      this.corTexto = 'red';
      this.texto = 'Label Vermelho';
    },
    textoAzul() {
      this.corTexto = 'blue';
      this.texto = 'Label Azul';
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
.botao-preto {
  background-color: white;
  padding: 8px 22px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  border: 2px solid black;
  border-radius: 10px;
}
.botao-preto:hover {
  background-color: black;
  color: white;
}
.botao-vermelho {
  background-color: white;
  padding: 8px 22px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
  border: 2px solid red;
  border-radius: 10px;
  color: black;
}
.botao-vermelho:hover {
  background-color: red;
  color: white;
}
.botao-azul {
  background-color: white;
  padding: 8px 22px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border: 2px solid blue;
  border-radius: 10px;
  color: black;
}
.botao-azul:hover {
  background-color: blue;
  color: white;
}
</style>
