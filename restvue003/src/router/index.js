import { createMemoryHistory, createRouter } from 'vue-router'
import IndexPages from "@/components/index/IndexPages.vue";
import LanShareIndex from "@/components/LanShare/LanShareIndex.vue";
const routes = [
  { path: "/", 
    component: IndexPages },
  {
    path: "/LanShareIndex",
    component: LanShareIndex,
  },
];
const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
export default router;
