import { createMemoryHistory, createRouter } from "vue-router";
import IndexPages from "@/components/index/IndexPages.vue";
import LanShareIndex from "@/components/LanShare/LanShareIndex.vue";
import ChatRoomIndex from "@/components/ChatRoom/ChatRoomIndex.vue";
import never_loader_chat_infomation_index from "@/components/ChatRoom/never_loader_chat_infomation/never_loader_chat_infomation_index.vue";
import Chat_Room_infomation_view from "@/components/ChatRoom/Chat_Room_infomation/Chat_Room_infomation_view.vue";
const routes = [
  { path: "/", 
    component: IndexPages 
  },
  {
    path: "/LanShareIndex",
    component: LanShareIndex,
  },
  {
    path: "/ChatRoomIndex",
    component: ChatRoomIndex,
     children: [
      {
        path: '/ChatRoomIndex/never_loader_chat_infomation_index',
        component: never_loader_chat_infomation_index,
      },
      {
        path: '/ChatRoomIndex/Chat_Room_infomation_view',
        component: Chat_Room_infomation_view,
      }]
  }
];
const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
export default router;
