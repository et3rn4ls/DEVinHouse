<template>
  <div class="calculadora">
        <div class="entrada">
            <p>Informe o seu peso: </p>
            <input type="number" v-model="peso">
        </div>
        <div class="entrada">
            <p>Informe a sua altura: </p>
            <input type="number" v-model="altura">
        </div>
        <br>
        <button v-on:click="calcular" class="btn btn-outline-dark btn-sm">Calcular IMC</button>
        <br><br>
        <p class="imc">Resultado: {{ resultado }}</p>
        <div class="resultado">            
            <p v-if="resultado > 0 && resultado < 18.5">Abaixo do peso!</p>
            <p v-if="resultado >= 18.5 && resultado <= 24.9">Peso normal!</p>
            <p v-if="resultado >= 25 && resultado <= 29.9">Sobrepeso!</p>
            <p v-if="resultado >= 30 && resultado <= 34.9">Obesidade grau 1!</p>
            <p v-if="resultado >= 35 && resultado <= 39.9">Obesidade grau 2!</p>
            <p v-if="resultado >= 40">Obesidade grau 3</p>
        </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            peso: null,
            altura: null,
            r: null,
            resultado: 0
        }
    },
    methods: {
        calcular() {
            this.r = this.peso / (this.altura **2)
            this.resultado = parseFloat(this.r).toFixed(2)
        }
    }
}
</script>

<style>
    .entrada {
        color:darkblue; 
    }
    .imc {
        font-style: italic;
    }
    .resultado {
        color: red;
        font-weight: bold;
    }
</style>