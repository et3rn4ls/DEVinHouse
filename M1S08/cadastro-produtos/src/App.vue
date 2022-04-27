<template>
  <div class="app">
    <button type="button" class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#exampleModal">Cadastrar produto</button>
    <div class="abre-modal">
      <ModalFormularioProduto @produtoSalvar="adicionarProduto"/>
    </div>
    <div class="tabela-produtos mt-5">
      <TabelaProdutos :produtos="produtos" @excluirProduto="excluirProduto"/>
    </div>
    <div id="rodape">
      <div class="container">
        <div class="saldo">
          <p>Saldo: R$ {{ saldo }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ModalFormularioProduto from './components/ModalFormularioProduto.vue'
import TabelaProdutos from './components/TabelaProdutos.vue'

export default {
  name: 'App',
  data() {
    return {
      produtos: [],
      saldo: 0
    }
  },
  components: {
    ModalFormularioProduto,
    TabelaProdutos
  },
  methods: {
    adicionarProduto(prod) {
      this.produtos.push({
        "nomeProduto":prod.nomeProduto,
        "valorProduto":prod.valorProduto
      })
      this.calculaValores();
    },
    excluirProduto(prod) {
      this.produtos.splice(prod, 1)
      this.calculaValores();
    },
    calculaValores() {
      this.saldo = 0
      this.produtos.forEach(produto => {
          this.saldo += Number(produto.valorProduto)
      })
    }
  }
}
</script>

<style>
body {
  background-color: #5C9BA4;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#rodape {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 30px;
  background-color: #33526E;
  color: white;
  font-size: 13px;
}
</style>
