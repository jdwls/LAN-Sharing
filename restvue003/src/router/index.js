import { createMemoryHistory, createRouter } from "vue-router";
import IndexPages from "@/components/index/IndexPages.vue";
import LanShareIndex from "@/components/LanShare/LanShareIndex.vue";
import ChatRoomIndex from "@/components/ChatRoom/ChatRoomIndex.vue";
const routes = [
  { path: "/", component: IndexPages },
  {
    path: "/LanShareIndex",
    component: LanShareIndex,
  },
  {
    path: "/ChatRoomIndex",
    component: ChatRoomIndex,
  },
];
const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
export default router;
