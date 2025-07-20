<template>
  <div>
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
      <div v-for="msg in $store.state.messages_lists" :key="msg.id" class="message-item"
        :class="{ 'current-user': msg.current_usrs }">
        <div class="message-content">
          <div><el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" /></div>
          <div class="message-text">{{ msg.message }}</div>
          <div class="message-time">{{ new Date(msg.Time * 1000).toLocaleTimeString() }}</div>
        </div>
      </div>
    </div>
    <div class="message-input">
      <el-input placeholder="输入消息..." v-model="message" :disabled="!currentChat" @keyup.enter="sendMessage">
        <template #append>
          <el-button :disabled="!currentChat" @click="sendMessage">发送</el-button>
        </template>
      </el-input>
    </div>
  </div>
</template>

<script>
import { seend_message_fun } from "@/socke/index.js";

export default {
  name: 'Chat_Room_infomation_view',
  props: {
    currentChat: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      message: "",
    }
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
  methods: {
    sendMessage() {
      seend_message_fun(this.message, this.currentChat)
      this.message = "";
    },
  }
}
</script>

<style scoped>
.chat-bgcolor {
  width: 70vw;
  height: 67vh;
  background-color: #ffffff;
  overflow-y: auto;
  margin-top: 3vh;
  border-radius: 10px;
  padding: 15px;
  box-sizing: border-box;
}

.message-item {
  margin-bottom: 15px;

}

.message-content {
  padding: 10px 15px;
  border-radius: 8px;
  background-color: #f0f8ff;
  max-width: 25vw;
  word-break: break-all
}

.current-user .message-content {
  background-color: #e1f3ff;
  margin-left: auto;
}

.message-sender {
  font-weight: bold;
  font-size: 12px;
  color: #666;
}

.message-text {
  margin: 5px 0;
  font-family: '宋体';
  font-size: 1vw;
}

.message-time {
  font-size: 10px;
  color: #999;
  text-align: right;
}

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
</style>
