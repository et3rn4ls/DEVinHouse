import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import { createStore } from 'vuex';
import App from './App.vue';
import Home from './views/home/Home';
import Cadastro from './views/pessoas/cadastro/Cadastro';
import Listagem from './views/pessoas/listagem/Listagem';

const routes = [
    { path: '/', component: Home, alias: ["/home"] },
    { path: '/pessoas/cadastro', component: Cadastro },
    { path: '/pessoas/listagem', component: Listagem }
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

const store = createStore({
    state() {
        return {
            pessoas: []
        }
    },
    mutations: {
        inserir(state, pessoa) {
            state.pessoas.push(pessoa);
        }
    }
});

const app = createApp(App);

app.use(router);
app.use(store);
app.mount('#app');