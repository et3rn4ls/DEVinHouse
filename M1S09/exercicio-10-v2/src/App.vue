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
      <span class="badge bg-info" v-show="estadoPartida === 'empate'">Empate!</span>
      <span class="badge bg-dark" v-show="estadoPartida === 'blackjack'">BLACKJACK!!!</span>
    </div>
    <hr v-show="estadoPartida.length > 0">
    <div>
      <div class="col-12">
        <label for="">Jogadas restantes: {{ quantidadeJogadas }} </label>
      </div>
      <div class="col-12">
        <label for="">Pontuação Dealer: {{ pontuacaoAtualDealer }} </label>
      </div>
      <div class="col-12">
         <label for="">Sua Pontuação: {{ pontuacaoAtual }} </label>
      </div>
      <hr>
      <div class="col-12">
        <h5>Cartas Dealer: {{ cartasDealer }}  </h5>
        <h5>Suas cartas: {{ minhasCartas }} </h5>
      </div>
      <div>
        <button type="button" :disabled="!estado" class="btn btn-success btn-sm" @click="novaCarta">Nova Carta</button>
        <button type="button" :disabled="!estado" class="btn btn-warning btn-sm" @click="pararJogo">Quero parar</button>
      </div>
      <br>
      <div class="col-12">
        <span class="badge bg-danger" v-show="msg.length > 0">Você não pode parar com menos de 14 pontos!</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: '',
      estado: false,
      quantidadeJogadas: 5,
      pontuacao: 0,
      pontuacaoDealer: 0,
      carta: '',
      cartaDealer: '',
      estadoPartida: '',
      minhasCartas: [],
      cartasDealer: []
    }
  },
  methods: {
    novoJogo() {
      this.msg = '';
      this.estado = true;
      this.quantidadeJogadas = 5;
      this.pontuacao = 0;
      this.pontuacaoDealer = 0;
      this.carta = '';
      this.cartaDealer = '';
      this.estadoPartida = '';
      this.minhasCartas = [];
      this.cartasDealer = [];
    },
    novaCarta() {
      this.msg = '';
      this.carta = Math.round(Math.random() * (11 * 1) + 1);
      this.pontuacaoAtual = this.carta;
      this.minhasCartas.push(this.carta);
      this.novaCartaDealer();
    },
    novaCartaDealer() {
      if (this.pontuacaoAtualDealer <= 16) {
        this.cartaDealer = Math.round(Math.random() * (11 * 1) + 1);
        this.pontuacaoAtualDealer = this.cartaDealer;
      }
      this.cartasDealer.push(this.cartaDealer);
    },
    pararJogo() {
      if (this.pontuacaoAtual < 14) {
        this.msg = 'nooooo';
      } else if (this.pontuacaoAtual > this.pontuacaoAtualDealer) {
        this.estadoPartida = 'ganhou';
        this.estado = false;
      } else if (this.pontuacaoAtual === this.pontuacaoAtualDealer) {
        this.estadoPartida = 'empate';
        this.estado = false;
      }
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
        if ((this.pontuacao > 21) || (this.quantidadeJogadas === 0 && this.pontuacao < this.pontuacaoDealer)) {
          this.estadoPartida = 'perdeu';
        } else if (this.quantidadeJogadas === 0 && this.pontuacao > this.pontuacaoDealer) {
          this.estadoPartida = 'ganhou';
        } else if (this.pontuacao === 21) {
          this.estadoPartida = 'blackjack';
        }
        if (this.quantidadeJogadas === 0 || this.estadoPartida.length > 0) {
          this.estado = false;
        }
      }
    },
    pontuacaoAtualDealer: {
      get() {
        return this.pontuacaoDealer;
      },
      set(value) {
        this.pontuacaoDealer += value;
        if ((this.pontuacao > 21 && this.pontuacaoDealer > 21) || (this.pontuacao === 21 && this.pontuacaoDealer === 21)) {
          this.estadoPartida = 'empate';
        } else if (this.pontuacaoDealer === 21) {
          this.estadoPartida = 'perdeu';
          this.estado = false;
        } else if (this.pontuacaoDealer > 21) {
          this.estadoPartida = 'ganhou';
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

h6 {

}
</style>
