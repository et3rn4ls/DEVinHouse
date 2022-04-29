import { createApp } from 'vue'
import App from './App.vue'

let app = createApp(App);

app.directive('size', {
    created(el) {
        el.addEventListener('mouseover', () => {
            el.style = 'font-size: 20px'
        });
        el.addEventListener('mouseout', () => {
            el.style = 'font-size: 15px'
        })
    }
})

app.mount('#app')
