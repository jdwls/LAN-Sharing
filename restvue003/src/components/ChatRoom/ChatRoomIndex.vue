<template>
  <div class="chat-room-container">
    <div class="sidebar">
      <UrseLIst @user-selected="startChat" />
    </div>
    <div class="main-content">
      <!-- 使用 props 传递数据而不是事件监听 -->
      <Chat_Room_infomation_view :current-chat="cu" />
    </div>
  </div>
</template>

<script>
import UrseLIst from "@/components/ChatRoom/UrseLIst/UrseLIst.vue";
import Chat_Room_infomation_view from "@/components/ChatRoom/Chat_Room_infomation/Chat_Room_infomation_view.vue"
import {disconnectSocket,connectSocket} from '@/socke/index.js'
export default {
  name: "ChatRoomIndex",
  components: {
    UrseLIst,
    Chat_Room_infomation_view
  },
  data() {
    return {
      cu: '' // 当前选中的用户
    }
  },
  methods: {
    startChat(user) {
      this.cu = user; // 设置当前聊天用户
    },
  },
  mounted() {
    this.$store.dispatch("Tokers");
    connectSocket();
  },
   beforeUnmount() {
 
       disconnectSocket()
 
   
  },
};
</script>

<style scoped>
/* 保持原有样式不变 */
.el-input {
  height: 6vh;
  background: #f0f8ff;
}

.chat-room-container {
  display: flex;
  background-color: #f5f7fa;
}

.sidebar {
  width: 300px;
  border-right: 1px solid #e2e5ec;
  background: #f0f8ff;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-top: 2vh;
}

.chat-header {
  padding: 15px 0;
  background: #fff;
  position: sticky;
  top: 0;
  z-index: 1;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
}

.message-input {
  width: 70vw;
  margin-top: 3vh;
}

.chat-bgcolor {
  width: 70vw;
  height: 67vh;
  background-color: #ffffff;
  overflow-y: hidden;
  margin-top: 3vh;
  border-radius: 10px;
}
</style>