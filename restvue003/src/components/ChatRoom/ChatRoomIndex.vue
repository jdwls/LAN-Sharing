<template>
  <div class="chat-room-container">
    <div class="sidebar">
      <UrseLIst />
    </div>
    <div class="main-content">
      <div class="chat-area">
        <!-- 聊天消息区域 -->
        <div class="message-list">
          <div class="empty-state">
            <el-empty description="选择对话开始聊天"></el-empty>
          </div>
        </div>

        <!-- 消息输入框 -->
        <div class="message-input">
          <el-input
            placeholder="输入消息..."
            v-model="message"
            :disabled="true"
          >
            <template #append>
              <el-button :disabled="true">发送</el-button>
            </template>
          </el-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UrseLIst from "@/components/ChatRoom/UrseLIst/UrseLIst.vue";
export default {
  name: "ChatRoomIndex",
  components: {
    UrseLIst,
  },
  data() {
    return {
      message: "",
    };
  },
  mounted() {
    this.$store.dispatch("Tokers");
  },
};
</script>

<style scoped>
.chat-room-container {
  display: flex;
  height: 100vh;
  background-color: #f5f7fa;
}

.sidebar {
  width: 300px;
  border-right: 1px solid #e2e5ec;
  background: rgb(255, 255, 255);
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.chat-area {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.message-list {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.empty-state {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.message-input {
  padding: 15px;
  border-top: 1px solid #ebeef5;
  background: white;
}
</style>
