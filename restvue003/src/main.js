import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import zhCn from "element-plus/es/locale/lang/zh-cn";
import { store } from "./store";
import "lib-flexible/flexible.js";

// import VueCoreVideoPlayer from 'vue-core-video-player'
const app = createApp(App);
app.use(store);
// app.use(ElementPlus)
// app.use(VueCoreVideoPlayer)
app.use(ElementPlus, {
  locale: zhCn,
  size: "default", // 可选组件尺寸配置
});
app.mount("#app");
