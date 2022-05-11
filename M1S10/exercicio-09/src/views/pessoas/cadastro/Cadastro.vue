<template>
  <div class="cadastro">
      <h3>Cadastro de Pessoas</h3>
      <br><br>
      <vee-form @submit="salvarPessoa" :validation-schema="schema" v-slot="{ errors }">
        <div class="row g-2">
          <div class="col-md-4">
            <label for="nome">Nome Completo: </label>
            <vee-field name="nome" type="text" v-model="pessoa.nome"/>
            <span class="text-danger" v-text="errors.nome" v-show="errors.nome"></span>
          </div>
          <div class="col-3">
            <label for="dataNascimento">Data de nascimento: </label>
            <vee-field name="dataNascimento" type="date" v-model="pessoa.dataNascimento"/>
            <span class="text-danger" v-text="errors.dataNascimento" v-show="errors.dataNascimento"></span>
          </div>
          <div class="col-3">
            <button type="submit" class="btn btn-outline-primary btn-sm">Cadastrar</button>
          </div>
        </div>
      </vee-form>
  </div>
</template>

<script>
import { Form, Field, defineRule } from 'vee-validate';

defineRule("required", value => {
  if (!value || value.length === 0) {
    return "Campo obrigatório";
  }
  return true;
});

defineRule("dataNasc", value => {
  if (new Date(value + ' 00:00:00') <= new Date()) {
    return true;
  } else {
    return "Não pode ser superior a data atual";
  }
});

defineRule("nomeCompleto", value => {
  let regexp = /^[a-zA-Z]{2,}( [a-zA-Z]+)*?( [a-zA-Z]{2,}){1,}$/

  if (!regexp.test(value)) {
    return "Favor informar o nome completo";
  }
  return true;
});

export default {
  components: {
    'vee-form': Form,
    'vee-field': Field
  },
  data() {
    return {
      schema: {
        nome: "required|nomeCompleto",
        dataNascimento: "required|dataNasc"
      },
      pessoa: {}
    }
  },
  methods: {
    salvarPessoa() {
      if (this.$store.state.pessoas.length === 0) {
        this.pessoa.id = 1;
      } else {
        this.pessoa.id = this.$store.state.pessoas[this.$store.state.pessoas.length - 1].id + 1;
      }
      this.$store.commit('inserir', this.pessoa);
      this.pessoa = {};
    }
  }
}
</script>

<style>

</style>