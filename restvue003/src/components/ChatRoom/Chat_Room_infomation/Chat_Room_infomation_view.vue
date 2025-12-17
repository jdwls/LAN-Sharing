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
      <div v-for="(msg, index) in $store.state.messages_lists" :key="msg.id" class="message-item"
        :class="is_classs(msg.send_name)" v-show="message_is(index)">
        <div class="message-content">
          <div class="message-avatar"><el-avatar
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" /></div>
          <div class="message-bubble" ref="message_text">
            <pre class="message-text"
              v-show="msg.message_type == 'text'">{{ msg.message }}<span v-show="false">{{ index }}</span></pre>
            <imageSee class="image" :src="msg.send_name_to_report_name_File_path" v-if="is_image_fun(msg.message_type)"></imageSee>
            <VideoPlay class="Video_play" v-if="is_Viedo_fun(msg.message_type)" :src="msg.send_name_to_report_name_File_path"></VideoPlay>
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
        <Chat_Room_File_Updata class="button_send_Message_css"></Chat_Room_File_Updata>
        <el-button @click="sendMessage" type="primary" size="large" class="button_send_Message_css">发送</el-button>
      </div>
    </div>
    <div class="meau">
      <button @click="Copy_message_fun()">复制</button>
      <button @click="Drop_message_fun()">删除</button>
      <button @click="Revocation_mesage_fun()" v-show="revocation_right_key">撤回</button>
    </div>
  </div>
</template>

<script>
import { seend_message_fun, emit_revocation_message_socket_fun } from "@/socke/index.js";
import Chat_Room_File_Updata from '@/components/ChatRoom/Chat_Room_infomation/Chat_Room_File_Updata.vue'
import imageSee from '@/components/DataView/imageSee.vue'
import VideoPlay from '@/components/DataView/VideoPlay.vue'
import axios from "axios";
export default {
  name: 'Chat_Room_infomation_view',
  components: {
    Chat_Room_File_Updata, imageSee, VideoPlay
  },
  data() {
    return {
      message: "",
      Copy_message: "",
      message_index: "",
      login: localStorage.getItem('UresName'),
      revocation_right_key: false
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
    message_is(index) {
      let messages_lists = this.$store.state.messages_lists
      console.log(messages_lists[index]['revocation_or_drop']['drop']);
      
      if (messages_lists[index]['revocation_or_drop']['drop']['drop_name'][0] == this.login) {
        return messages_lists[index]['revocation_or_drop']['drop']['drop_state'][0]
      }
      if (messages_lists[index]['revocation_or_drop']['drop']['drop_name'][1] == this.login) {
        return messages_lists[index]['revocation_or_drop']['drop']['drop_state'][1]
      }
      if (messages_lists[index]['revocation_or_drop']['revocation']['revocation_name'] == null) {
        return messages_lists[index]['revocation_or_drop']['revocation']['revocation_state']
      }
      else {
        return messages_lists[index]['revocation_or_drop']['revocation']['revocation_state']
      }
    },
    sendMessage() {
      let message = this.message.trim()
      console.log(message);
      if (message !== "") {
        seend_message_fun(message, this.$store.state.currentChat, this.$store.state.messages_lists.length)
        this.message = "";
        this.chat_bgcolor_fun()
      }
      this.message = "";
    },
    chat_bgcolor_fun() {
      const scrollTop = this.$refs.chat_bgcolor
      scrollTop.scrollTop = this.$refs.chat_bgcolor.scrollHeight
    },
    Copy_message_fun() {
      navigator.clipboard.writeText(this.Copy_message)
    },
    Drop_message_fun() {
      axios({
        url: this.$store.state.api + '/Drop_message_api',
        method: "get",
        params: {
          'message_index': this.message_index,
          'send_name': localStorage.getItem('UresName'),
          'report_name': this.$store.state.currentChat,
        }
      })
        .then((res) => {
          if (res.data.msg == '成功')
            this.$store.state.messages_lists = res.data.data
          // console.log(this.$store.state.messages_lists[0]['revocation_or_drop']['drop']['drop_name'] == this.login ? this.$store.state.messages_lists[0]['revocation_or_drop']['drop']['drop_state'] : true);

        })
        .catch((res) => {
          console.log(res);

        })
    },
    Revocation_mesage_fun() {
      emit_revocation_message_socket_fun(this.message_index, localStorage.getItem('UresName'), this.$store.state.currentChat)
    },
    is_image_fun(message_type) {
      for (let i = 0; i < this.$store.state.File_MIME[0].length; i++) {
        if (message_type == this.$store.state.File_MIME[0][i]) {
          return true
        }
      }
      return false
    },
    is_Viedo_fun(message_type) {
      for (let i = 0; i < this.$store.state.File_MIME[1].length; i++) {
        if (message_type == this.$store.state.File_MIME[1][i]) {
          console.log(message_type);
          return true
        }
      }
      return false
    },
    is_classs(send_name) {
      if (send_name == localStorage.getItem('UresName')) {
        return 'current-user'
      }
      else {
        return 'other-user'
      }

    },
  },
  mounted() {
    this.$nextTick(async () => {
      this.chat_bgcolor_fun()
    })
  },
  updated() {
    this.$nextTick(() => {
      let chat_bgcolor_element = this.$refs.chat_bgcolor
      // 阻止聊天背景的默认右键菜单
      chat_bgcolor_element.addEventListener("contextmenu", (e) => {
        e.preventDefault();
      });
      let message_texts = this.$refs.message_text
      const menu = document.querySelector('.meau');
      let lastHighlightedElement = null;
      if (message_texts) {
        message_texts.forEach((element) => {
          element.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            // console.log(element.innerHTML);
            this.Copy_message = element.innerHTML
            this.message_index = element.querySelector('span').innerHTML
            if (this.$store.state.messages_lists[this.message_index]["send_name"] == localStorage.getItem('UresName')) {
              this.revocation_right_key = true
            }
            // 移除之前的高亮
            if (lastHighlightedElement) {
              lastHighlightedElement.classList.remove('gray-out');
            }

            // 高亮当前元素
            element.classList.add('gray-out');
            lastHighlightedElement = element;

            // 计算菜单位置（防止超出屏幕）
            let clickX = e.pageX;
            let clickY = e.pageY;

            if (clickY + menu.offsetHeight > window.innerHeight) {
              clickY = clickY - menu.offsetHeight;
            }
            if (clickX + menu.offsetWidth > window.innerWidth) {
              clickX = clickX - menu.offsetWidth;
            }

            // 显示菜单
            menu.style.display = 'flex';
            menu.style.left = `${clickX}px`;
            menu.style.top = `${clickY}px`;
          });
        });
      }


      // 点击其他地方时关闭菜单并取消高亮
      document.addEventListener('click', () => {
        menu.style.display = 'none'
        if (lastHighlightedElement) {
          lastHighlightedElement.classList.remove('gray-out');
        }
      });
    });
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

.gray-out {
  background-color: #e0e0e0 !important;
  color: #333 !important;
}

.image {
  max-width: 320px;
  /* max-height:   */
}

.Video_play {
  width: 320px;
  max-height: 180px;
}

.meau {
  position: absolute;
  display: none;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  flex-direction: column;
  z-index: 1000;
  min-width: 120px;
  padding: 4px 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  font-size: 14px;
  color: #333;
  overflow: hidden;
  margin: 0;
  padding: 0;
}

.meau>button {
  transition: background-color 0.2s ease;
  padding: 0.5vw 1vw;
  background-color: white;
  cursor: pointer;
  border: none;
  font-size: 0.8vw;
}

.meau>button:hover {
  background-color: #f5f5f5;
}

.meau>button:active {
  background-color: #ebebeb;
}

/* Optional divider between items */
.meau>button:not(:last-child) {
  border-bottom: 1px solid #f0f0f0;
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
  padding: 0.3vw 0.3vw;
  position: relative;
  word-break: break-word;
}

.message-text {
  margin: 0;
  font-size: 0.8vw;
  line-height: 1.5;
  max-width: 30vw;
  word-break: break-word;
  overflow-wrap: break-word;
  word-break: break-word;
  white-space: pre-wrap;
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
  align-self: flex-end;
  display: flex;
}

.button_send_Message_css {
  margin-left: 0.5vw;
  height: 3.5vh;
  /* width: 2.5vw; */
}
</style>
