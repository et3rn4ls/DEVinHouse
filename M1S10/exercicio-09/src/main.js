import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import { createStore } from 'vuex';
import App from './App.vue';
import Home from './views/home/Home';
import Cadastro from './views/pessoas/cadastro/Cadastro';
import Listagem from './views/pessoas/listagem/Listagem';
import CadastroUsuarios from './views/user/cadastro/Cadastro';

const routes = [
    { path: '/', component: Home, alias: ["/home"] },
    { path: '/pessoas/cadastro', component: Cadastro },
    { path: '/pessoas/listagem', component: Listagem },
    { path: '/user/cadastro', component: CadastroUsuarios }
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

const store = createStore({
    state() {
        return {
            pessoas: [],
            usuarios: []
        }
    },
    mutations: {
        inserir(state, pessoa) {
            state.pessoas.push(pessoa);
        },
        remover(state, id) {
            let indice;
            for (let i=0; i < state.pessoas.length ; i++) {
                if (id === state.pessoas[i].id) {
                    indice = i;
                }
            }
            if (indice) {
                state.pessoas.splice(indice, 1);
            }
        },
        cadastrarUsuario(state, usuario) {
            state.usuarios.push(usuario);
        }
    }
});

const app = createApp(App);

app.use(router);
app.use(store);
app.mount('#app');