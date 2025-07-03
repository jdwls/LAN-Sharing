<template>
  <div class="container">
    <div class="header">
      <el-avatar shape="square" :size="60" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        v-if="$store.state.ButtonAuthority[3].HeadIcon"></el-avatar>
      <h1 class="user-name">{{ LocationUrseName }}</h1>
    </div>
    <div class="scrollable-list">
      <el-collapse v-model="activeCollapse" accordion>
        <div class="IconBuuton">
          <svg t="1751253186885" class="rato" viewBox="0 0 1024 1024" version="1.1"
            p-id="9703" width="25" height="25" @click="Animation360deg()">
            <path
              d="M721.024 725.333333A298.666667 298.666667 0 1 1 810.666667 512a42.666667 42.666667 0 0 0 85.333333 0 384 384 0 1 0-128 286.208V810.666667c0 23.722667 19.114667 42.666667 42.666667 42.666666 23.722667 0 42.666667-19.114667 42.666666-42.666666v-128a42.538667 42.538667 0 0 0-42.666666-42.666667h-128c-23.722667 0-42.666667 19.114667-42.666667 42.666667 0 23.722667 19.114667 42.666667 42.666667 42.666666h38.357333z"
              fill="#3D3D3D" p-id="9704"></path>
          </svg>
        </div>
        <el-collapse-item name="online">
          <template #title>
            <h2 class="section-title">在线人数 ({{ $store.state.Online_Numbers.length }})</h2>
          </template>
          <transition-group name="user-list" tag="div" class="user-cards">
            <div class="user-card online" v-for="(name, index) in $store.state.Online_Numbers" :key="'online-' + index" @click="handleUserClick(name)">
              <el-avatar shape="square" :size="40"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                v-if="$store.state.ButtonAuthority[3].HeadIcon"></el-avatar>
              <span class="name">{{ name }}</span>
            </div>
          </transition-group>
        </el-collapse-item>

        <el-collapse-item name="offline">
          <template #title>
            <h2 class="section-title">离线人数 ({{ $store.state.disconnectNumber.length }})</h2>
          </template>
          <transition-group name="user-list" tag="div" class="user-cards">
            <div class="user-card offline" v-for="(name, index) in $store.state.disconnectNumber"
              :key="'offline-' + index" @click="handleUserClick(name)">
              <el-avatar shape="square" :size="40"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                v-if="$store.state.ButtonAuthority[3].HeadIcon"></el-avatar>
              <span class="name">{{ name }}</span>
            </div>
          </transition-group>
        </el-collapse-item>
      </el-collapse>
    </div>
    <IsOlineNumber></IsOlineNumber>
  </div>
</template>

<style scoped>
/* 容器样式 */
.container {
  padding: 0;
  max-width: 300px;
  background: white;
  border-radius: 8px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  height: 100vh;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

/* 头部样式 */
.header {
  display: flex;
  align-items: center;
  padding: 15px;
  background: RGB(235, 235, 235);
  border-radius: 8px 8px 0 0;
  position: sticky;
  top: 0;
  z-index: 1;
}

/* 滚动区域样式 */
.scrollable-list {
  flex: 1;
  overflow-y: auto;
  padding: 0 15px;
}

/* 自定义滚动条 */
.scrollable-list::-webkit-scrollbar {
  width: 6px;
}

.scrollable-list::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.scrollable-list::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

.scrollable-list::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

/* 用户卡片样式 */
.user-cards {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 10px 0;
}

.user-card {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
}

.user-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.user-card.online {
  border-left: 3px solid #67c23a;
}

.user-card.offline {
  border-left: 3px solid #909399;
  opacity: 0.7;
}

/* 用户动画效果 */
.user-list-enter-active,
.user-list-leave-active {
  transition: all 0.5s ease;
}

.user-list-enter-from,
.user-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.user-list-move {
  transition: transform 0.5s ease;
}

/* 标题样式 */
.section-title {
  font-size: 16px;
  color: #606266;
  margin: 0;
}

.name {
  margin-left: 10px;
  font-size: 14px;
  color: #606266;
}

/* 折叠面板样式 */
:deep(.el-collapse) {
  border: none;
}

:deep(.el-collapse-item__header) {
  border: none;
  /* padding: 15px 0; */
  height: auto;
}

:deep(.el-collapse-item__content) {
  padding: 0;
}

.IconBuuton {
  width: 14vw;
  height: 8vh;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.rato:hover {
  cursor: pointer;
  transform: scale(1.3);
}

.transform_rotate {
  animation: rotate360 5s ease;
}

@keyframes rotate360 {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(1440deg);
  }
}
</style>

<script>
import axios from "axios";
import IsOlineNumber from "@/components/ChatRoom/UrseLIst/IsOlineNumber.vue";
// import { io } from "socket.io-client";
import {
  connectSocket,
  disconnectSocket,
  // socket_user_online_name_list
  // socket
} from "@/socke/index.js";
// , DisconnectSendNumber
export default {
  name: "UrseLIst",
  comments: {
    IsOlineNumber,
  },
  data() {
    return {
      LocationUrseName: localStorage.getItem("UresName"),
      activeCollapse: ["online", "offline"],
      Urselist: [],
      DisconnectUresNameNumber: [
        "赵六",
        "钱七",
        "孙八",
        "赵六2",
        "钱七2",
        "孙八2",
        "赵六3",
        "钱七3",
        "孙八3",
      ],
    };
  },
  computed: {
    onlineUresNumber() {
      return this.$store.state.Online_Numbers.length;
    },
    DisconnectUresNumber() {
      return this.DisconnectUresNameNumber.length;
    },
  },
  mounted() {
    connectSocket()
    // socket_user_online_name_list()
    // axios({
    //   url: this.$store.state.api + "/UreList",
    //   method: "get",
    // })
    //   .then((res) => {
    //     this.$store.state.Urselist = res.data.data;
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });
  },
  beforeUnmount() {
    disconnectSocket()
  },
  methods: {
    handleUserClick(name) {
      this.$emit('user-selected', name)
    },
    Animation360deg() {
      const svg = document.getElementsByClassName('rato')[0]
        svg.classList.add('transform_rotate');
        axios({
          url:this.$store.state.api + "/Online_UreList",
          method:"get"
        })
        .then((res)=>{
          this.$store.state.Online_Numbers = res.data.data['online_users']
          this.$store.state.disconnectNumber = res.data.UreList
          this.$store.state.disconnectNumber=this.$store.state.disconnectNumber.filter((item)=>{
            return !this.$store.state.Online_Numbers.includes(item)
          })
          setTimeout(()=>{
            svg.classList.remove('transform_rotate');
          },1000)
          
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
};
</script>
