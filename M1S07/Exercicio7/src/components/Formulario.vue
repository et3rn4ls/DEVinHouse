<template>
    <div class="entrada">
        <form>
            <div class="mb-3">
                <label for="peso" class="form-label">Informe o seu peso:</label>
                <input type="number" class="form-control" id="peso" v-model="peso">
            </div>
            <div class="mb-3">
                <label for="altura" class="form-label">Informe a sua altura: </label>
                <input type="number" class="form-control" id="altura" v-model="altura">
            </div>
            <button v-on:click="calcular" class="btn btn-outline-dark btn-sm">Calcular IMC</button>
        </form>
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
    .mb-3 {
        max-width: 10%;
        display: block;
        margin-right: auto;
        margin-left: auto;
    }
</style>