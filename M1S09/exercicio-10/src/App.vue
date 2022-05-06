<template>
  <div class="container mt-5">
    <h2>M1S09 - Exercício 10</h2>
    <hr>
    <h3>Blackjack</h3>
    <hr>
    <div class="col-12" >
      <button :disabled="estado" class="btn btn-primary btn-sm" @click="novoJogo">Novo Jogo</button>
    </div>
    <hr>
    <div class="col-12" v-show="estadoPartida.length > 0">
      <span class="badge bg-success" v-show="estadoPartida === 'ganhou'">Você ganhou!</span>
      <span class="badge bg-danger" v-show="estadoPartida === 'perdeu'">Você perdeu!</span>
    </div>
    <hr v-show="estadoPartida.length > 0">
    <div>
      <div class="col-12">
        <label for="">Jogadas restantes: {{ quantidadeJogadas }} </label>
      </div>
      <div class="col-12">
        <label for="">Pontuação do Dealer: 17</label>
      </div>
      <div class="col-12">
         <label for="">Pontuação Atual: {{ pontuacaoAtual }} </label>
      </div>
      <hr>
      <div class="col-12">
        <h5>Carta retirada: {{ carta }} </h5>
      </div>
      <div class="col-12">
        <button :disabled="!estado" class="btn btn-success btn-sm" @click="novaCarta">Nova Carta</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      estado: false,
      quantidadeJogadas: 5,
      pontuacao: 0,
      carta: '',
      estadoPartida: ''
    }
  },
  methods: {
    novoJogo() {
      this.estado = true;
      this.quantidadeJogadas = 5;
      this.pontuacao = 0;
      this.carta = '';
      this.estadoPartida = '';
    },
    novaCarta() {
      this.carta = Math.round(Math.random() * (11 * 1) + 1);
      this.pontuacaoAtual = this.carta;
    }
  },
  computed: {
    pontuacaoAtual: {
      get() {
        return this.pontuacao;
      },
      set(value) {
        this.pontuacao += value;
        this.quantidadeJogadas -= 1;
        if ((this.pontuacao > 21) || (this.quantidadeJogadas === 0 && this.pontuacao < 17)) {
          this.estadoPartida = 'perdeu';
        } else if (this.pontuacao > 17) {
          this.estadoPartida = 'ganhou';
        }
        if (this.quantidadeJogadas === 0 || this.estadoPartida.length > 0) {
          this.estado = false;
        }
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

h2 {
  text-align: center;
}
</style>
