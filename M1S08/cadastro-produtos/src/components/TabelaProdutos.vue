<template>
    <div class="tabela-produtos container">
      <h4>Lista de Produtos</h4>
        <table class="table" v-if="produtos.length > 0">
            <thead>
                <tr>
                <th scope="col">Produto</th>
                <th scope="col">Valor</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(produto, indice) in produtos" :key="indice">
                <td>{{ produto.nomeProduto }}</td>
                <td>{{ produto.valorProduto }}</td>
                <td>
                    <button type="button" class="btn btn-danger btn-sm ms-1" @click="excluirProduto">Excluir</button>
                </td>
                </tr>
            </tbody>
        </table>
        <span v-else>
            Nenhum produto cadastrado até o momento!
        </span>
    </div>
</template>

<script>
export default {
    props: {
        produtos: {
            type: Array,
            require: true,
            default: null
        }
    },
    methods: {
        excluirProduto(indice) {
            this.$emit('excluirProduto', indice)
        }
    }
}
</script>

<style>
.table {
    background-color: white;
}
</style>