import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import Home from './views/home/Home';
import Cadastro from './views/pessoas/cadastro/Cadastro';
import Listagem from './views/pessoas/listagem/Listagem';

const routes = [
    { path: '/home', component: Home },
    { path: '/pessoas/cadastro', component: Cadastro },
    { path: '/pessoas/listagem', component: Listagem },
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

const app = createApp(App);

app.use(router);
app.mount('#app');