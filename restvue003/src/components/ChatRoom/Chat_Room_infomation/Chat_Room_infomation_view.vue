<template>
  <div>
    <div class="chat-header card">
      <el-row align="middle" :gutter="20">
        <el-col :span="2" style="padding-left: 1.5vw;">
          <el-avatar :size="60" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
        </el-col>
        <el-col :span="21">
          <h2 style="margin:0 0 0.2604vw 0;font-weight:600;color:#303133">与 {{ $store.state.currentChat }} 的对话</h2>
          <p style="margin:0;font-size:0.7292vw;color:#909399">
            <el-tag size="small" :type="userStatus.type">{{ userStatus.text }}</el-tag>
          </p>
        </el-col>
      </el-row>
      <el-divider style="margin:0.4vw 0" />
    </div>
    <div class="chat-bgcolor" ref="chat_bgcolor">
      <div v-for="msg in $store.state.messages_lists" :key="msg.id" class="message-item"
        :class="{ 'current-user': msg.current_usrs, 'other-user': !msg.current_usrs }">
        <div class="message-content">
          <div class="message-avatar"><el-avatar
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" /></div>
          <div class="message-bubble">
            <div class="message-text">{{ msg.message }}</div>
            <div class="message-time">{{ new Date(msg.Time * 1000).toLocaleTimeString() }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="message-input">
      <div class="ms-in">
        <el-input placeholder="输入消息..." v-model="message" type="textarea" :autosize="{ minRows: 2, maxRows: 2 }"
          resize="none" class="el-input_s">
        </el-input>
      </div>

      <div class="send_Message_css">
        <el-button @click="sendMessage" type="primary" size="large">发送</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { seend_message_fun } from "@/socke/index.js";
export default {
  name: 'Chat_Room_infomation_view',
  data() {
    return {
      message: "",
    }
  },
  computed: {
    userStatus() {
      if (!this.$store.state.currentChat) return { type: 'info', text: '未知' };
      const isOnline = this.$store.state.Online_Numbers.includes(this.$store.state.currentChat);
      return {
        type: isOnline ? 'success' : 'info',
        text: isOnline ? '在线' : '离线'
      };
    },
  },
  methods: {
    sendMessage() {
      if (this.message) {
        seend_message_fun(this.message, this.$store.state.currentChat)
        this.message = "";
        this.chat_bgcolor_fun()
      }

    },
    chat_bgcolor_fun() {
      const scrollTop = this.$refs.chat_bgcolor
      scrollTop.scrollTop = this.$refs.chat_bgcolor.scrollHeight
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.chat_bgcolor_fun()
    })
  },
  watch: {
    '$store.state.messages_lists': {
      handler() {
        this.$nextTick(() => {
          this.chat_bgcolor_fun();
        });
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.ms-in {
  width: 65vw;
}

.chat-bgcolor {
  height: 63vh;
  background-color: #ffffff;
  overflow-y: auto;
  margin: 1.5vh 1vw;
  border-radius: 12px;
  padding: 1.5vw;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  box-shadow: 0 0.2vw 0.8vw rgba(0, 0, 0, 0.08);
  border: 1px solid #ebeef5;
  flex: 1;
}

.message-item {
  margin-bottom: 1.5vh;
  display: flex;
  padding: 0.5vh 0;
}

/* 当前用户消息样式 (右侧) */
.message-item.current-user {
  justify-content: flex-end;
}

.current-user .message-content {
  flex-direction: row-reverse;
}

.current-user .message-bubble {
  background-color: #409EFF;
  color: white;
  border-radius: 18px 18px 0 18px;
  margin-right: 0.8vw;
  box-shadow: 0 0.1vw 0.3vw rgba(0, 0, 0, 0.1);
}

.current-user .message-time {
  color: rgba(255, 255, 255, 0.7);
}

/* 其他用户消息样式 (左侧) */
.message-item.other-user {
  justify-content: flex-start;
}

.other-user .message-content {
  flex-direction: row;
}

.other-user .message-bubble {
  background-color: #f5f7fa;
  color: #303133;
  border-radius: 18px 18px 18px 0;
  margin-left: 0.8vw;
  box-shadow: 0 0.1vw 0.3vw rgba(0, 0, 0, 0.08);
  border: 1px solid #ebeef5;
}

.other-user .message-time {
  color: #909399;
}

.message-content {
  display: flex;
  max-width: 30vw;
}

.message-avatar {
  display: flex;
  align-items: flex-end;
}

.message-bubble {
  padding: 0.625vw 0.8333vw;
  position: relative;
  word-break: break-word;
}

.message-text {
  margin: 0;
  font-size: 0.8vw;
  line-height: 1.5;
}

.message-time {
  font-size: 0.5vw;
  margin-top: 0.2083vw;
  text-align: right;
}

/* 输入框样式 */
.el-input {
  height: 6vh;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 0.1042vw 0.5208vw rgba(0, 0, 0, 0.08);
}

.chat-header {
  padding: 1.5vh 1.5vw;
  background: #fff;
  position: sticky;
  top: 0;
  z-index: 1;
  box-shadow: 0 0.1vw 0.4vw rgba(0, 0, 0, 0.08);
  border-radius: 12px;
  margin: 1vh 1vw;
  border: 1px solid #ebeef5;
}

.message-input {
  font-family: '黑体';
  display: flex;
  flex-direction: column;
  margin: 1.5vh 1vw;
  padding: 1vw;
  width: 64.9vw;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 0.1vw 0.4vw rgba(0, 0, 0, 0.08);
  border: 1px solid #ebeef5;
  gap: 0.8vw;
  /* 新增样式使容器向上拉伸 */
  position: relative;
  bottom: 0;
  z-index: 100;
}

.el-textarea__inner {
  resize: none;
  align-items: flex-end;
}

:deep(.el-textarea__inner) {
  box-shadow: none;
  padding: 10px;
  border: none;
  resize: none;
  font-size: 0.9vw;
  /* max-height: 200px; */
  /* 设置最大高度 */
  overflow-y: auto;
  /* 内容超出时显示滚动条 */
  /* background-color: #f0f2f5; */
}

.send_Message_css {
  align-self: flex-end
}
</style>
