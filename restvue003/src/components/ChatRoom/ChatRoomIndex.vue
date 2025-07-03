<template>
  <div class="chat-room-container">
    <div class="sidebar">
      <UrseLIst @user-selected="startChat" />
    </div>
    <div class="main-content">
      <div class="chat-header">
        <el-row align="middle" :gutter="20">
          <el-col :span="3">
            <el-avatar :size="60" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
          </el-col>
          <el-col :span="21">
            <h2 style="margin:0 0 5px 0;font-weight:600;color:#303133">与 {{ currentChat }} 的对话</h2>
            <p style="margin:0;font-size:14px;color:#909399">
              <el-tag size="small" :type="userStatus.type">{{ userStatus.text }}</el-tag>
            </p>
          </el-col>
        </el-row>
        <el-divider style="margin:15px 0" />
      </div>
      <div class="chat-bgcolor">

      </div>
      <div class="message-input">
        <el-input placeholder="输入消息..." v-model="message" :disabled="!currentChat">
          <template #append>
            <el-button :disabled="!currentChat" @click="sendMessage()">发送</el-button>
          </template>
        </el-input>
      </div>
    </div>
  </div>
</template>

<script>
import UrseLIst from "@/components/ChatRoom/UrseLIst/UrseLIst.vue";
import {sendMessage} from "@/socke/index.js";
export default {
  name: "ChatRoomIndex",
  components: {
    UrseLIst,
  },
  data() {
    return {
      message: "",
      currentChat: null,
    };
  },
  methods: {
    startChat(user) {
      this.currentChat = user;
    },
    sendMessage() {
      if (this.message.trim()) {
        sendMessage(this.message,this.currentChat)
        this.message = "";
      }
     
    },
  },
  computed: {
    userStatus() {
      if (!this.currentChat) return { type: 'info', text: '未知' };
      const isOnline = this.$store.state.Online_Numbers.includes(this.currentChat);
      return {
        type: isOnline ? 'success' : 'info',
        text: isOnline ? '在线' : '离线'
      };
    },
  },
  mounted() {
    this.$store.dispatch("Tokers");
    // sendReport(this.currentChat)
  },
};
</script>

<style scoped>
.el-input {
  height: 6vh;
  background: #f0f8ff;
}

.chat-room-container {
  display: flex;
  /* height:100%; */
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
