<template>
  <div class="modal-formulario-produto">
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Adicionar produto</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <Form @submit="salvarProduto">
                        <div class="mb-3">
                            <label for="nome" class="form-label">Nome do produto</label>
                            <Field type="text" class="form-control" id="nome" name="nome" v-model="produto.nomeProduto" :rules="validations.validarCampoObrigatorio"/>
                            <span class="error">
                                <ErrorMessage name="nome"/>
                            </span>
                        </div>
                        <div class="mb-3">
                            <label for="valor" class="form-label">Valor do produto</label>
                            <Field type="number" class="form-control" id="valor" name="valor" v-model="produto.valorProduto" :rules="validations.validarCampoValor"/>
                            <span class="error">
                                <ErrorMessage name="valor"/>
                            </span>
                        </div>
                        <div class="botao-salvar">
                            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal" :disabled="!habilitaBotao">Salvar</button>
                        </div>
                    </Form>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate'
import validations from '../validations.js'

export default {
    components: {
        Form,
        Field,
        ErrorMessage
    },
    data() {
        return {
            produto: {
                nomeProduto: null,
                valorProduto: null
            },
            validations: null
        }
    },
    computed: {
        habilitaBotao() {
            return this.produto.nomeProduto && this.produto.valorProduto
        }
    },
    methods: {
        salvarProduto() {
            this.$emit('produtoSalvar', this.produto)
            this.limparCampos()
        },
        limparCampos() {
            this.produto.nomeProduto = null
            this.produto.valorProduto = null
        }
    },
    beforeMount() {
        this.validations = validations
    }
}
</script>

<style>

</style>