import { createRouter, createWebHistory } from "vue-router";
import IndexPages from "@/components/index/IndexPages.vue";
import LanShareIndex from "@/components/LanShare/LanShareIndex.vue";
const routes = [
  { path: "/", component: IndexPages },
  {
    path: "/LanShareIndex",
    component: LanShareIndex,
  },
];
const routerHistory = createWebHistory();
const router = createRouter({
  history: routerHistory,
  routes,
});
export default router;
