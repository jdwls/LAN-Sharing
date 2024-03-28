import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { store } from './store'
import 'lib-flexible/flexible.js'
// import VueCoreVideoPlayer from 'vue-core-video-player'
const app = createApp(App)
app.use(store)
app.use(ElementPlus)
// app.use(VueCoreVideoPlayer)
app.mount('#app')
