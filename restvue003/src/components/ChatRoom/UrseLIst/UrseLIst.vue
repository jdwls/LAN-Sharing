<template>
  <div class="container">
    <div class="header">
      <el-avatar
        shape="square"
        :size="60"
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        v-if="$store.state.ButtonAuthority[3].HeadIcon"
      ></el-avatar>
      <h1 class="user-name">{{ LocationUrseName }}</h1>
    </div>
    <div class="scrollable-list">
      <el-collapse v-model="activeCollapse" accordion>
        <el-collapse-item name="online">
          <template #title>
            <h2 class="section-title">在线人数 ({{ onlineUresNumber }})</h2>
          </template>
          <transition-group name="user-list" tag="div" class="user-cards">
            <div
              class="user-card online"
              v-for="(name, index) in onlineUresNameAndAvatar"
              :key="'online-' + index"
            >
              <el-avatar
                shape="square"
                :size="40"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                v-if="$store.state.ButtonAuthority[3].HeadIcon"
              ></el-avatar>
              <span class="name">{{ name }}</span>
            </div>
          </transition-group>
        </el-collapse-item>

        <el-collapse-item name="offline">
          <template #title>
            <h2 class="section-title">离线人数 ({{ DisconnectUresNumber }})</h2>
          </template>
          <transition-group name="user-list" tag="div" class="user-cards">
            <div
              class="user-card offline"
              v-for="(name, index) in DisconnectUresNameAndAvatar"
              :key="'offline-' + index"
            >
              <el-avatar
                shape="square"
                :size="40"
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                v-if="$store.state.ButtonAuthority[3].HeadIcon"
              ></el-avatar>
              <span class="name">{{ name }}</span>
            </div>
          </transition-group>
        </el-collapse-item>
      </el-collapse>
    </div>
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
  padding: 15px 0;
  height: auto;
}
:deep(.el-collapse-item__content) {
  padding: 0;
}
</style>

<script>
export default {
  name: "UrseLIst",
  data() {
    return {
      LocationUrseName: localStorage.getItem("UresName"),
      activeCollapse: ["online", "offline"],
    };
  },
  computed: {
    onlineUresNumber() {
      return this.onlineUresNameAndAvatar.length;
    },
    onlineUresNameAndAvatar() {
      return [
        "张三",
        "李四",
        "王五",
        "张三2",
        "李四2",
        "王五2",
        "张三3",
        "李四3",
        "王五3",
      ];
    },
    DisconnectUresNumber() {
      return this.DisconnectUresNameAndAvatar.length;
    },
    DisconnectUresNameAndAvatar() {
      return ["赵六", "钱七", "孙八"];
    },
  },
};
</script>
