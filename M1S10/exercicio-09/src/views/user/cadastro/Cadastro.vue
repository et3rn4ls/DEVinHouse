<template>
    <div class="container">
        <h3>Cadastro de Usuários</h3>
        <br><br>
        <vee-form @submit="salvarUsuario" :validation-schema="schema" v-slot="{ errors }">
            <div class="row g-2">
                <div class="col-md-4">
                    <label for="nome">Nome Completo: </label>
                    <vee-field name="nome" type="text" v-model="usuario.nome"/>
                    <span class="text-danger" v-text="errors.nome" v-show="errors.nome"></span>
                </div>
                <div class="col-3">
                    <label for="email">E-mail: </label>
                    <vee-field name="email" type="text" v-model="usuario.email"/>
                    <span class="text-danger" v-text="errors.email" v-show="errors.email"></span>
                </div>
                <div class="col-3">
                    <label for="senha">Senha: </label>
                    <vee-field name="senha" type="password" v-model="usuario.senha"/>
                    <span class="text-danger" v-text="errors.senha" v-show="errors.senha"></span>
                </div>
                <div class="col-2">
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

defineRule("nomeCompleto", value => {
  let regexp = /^[a-zA-Z]{2,}( [a-zA-Z]+)*?( [a-zA-Z]{2,}){1,}$/

  if (!regexp.test(value)) {
    return "Favor informar o nome completo";
  }
  return true;
});

defineRule("password", value => {
  let regexp = /^[a-zA-Z0-9]{6,}$/

  if (!regexp.test(value)) {
    return "A senha deve ter pelo menos 6 caracteres";
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
        email: "required",
        senha: "required|password"
      },
      usuario: {}
    }
  },
  methods: {
    salvarUsuario() {
      if (this.$store.state.usuarios.length === 0) {
        this.usuario.id = 1;
      } else {
        this.usuario.id = this.$store.state.usuarios[this.$store.state.usuarios.length - 1].id + 1;
      }
      this.$store.commit('cadastrarUsuario', this.usuario);
      this.usuario = {};
    }
  }
}
</script>

<style>

</style>