import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import Home from './views/home/Home';
import Cadastro from './views/pessoas/cadastro/Cadastro';
import Busca from './views/pessoas/busca/Busca';

const routes = [
    { path: '/', component: Home, alias: ["/home"] },
    { path: '/pessoas/cadastro', component: Cadastro },
    { path: '/pessoas/busca', component: Busca }
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

const app = createApp(App);

app.use(router);
app.mount('#app');