<template>
  <div class="homePages">
    <div class="Title1">
      <el-avatar
        shape="square"
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        v-if="$store.state.ButtonAuthority[3].HeadIcon"
      ></el-avatar>
      <svg
        t="1748396562479"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="3515"
        width="2vw"
        height="2vw"
        v-if="$store.state.ButtonAuthority[2].steeingButton"
      >
        <path
          d="M933.868272 511.691752a140.807706 140.807706 0 0 1 90.131728-131.067068 525.562914 525.562914 0 0 0-57.334136-138.64997 139.882962 139.882962 0 0 1-184.948826-184.948826A525.562914 525.562914 0 0 0 643.067068 0a140.376159 140.376159 0 0 1-262.134136 0A525.562914 525.562914 0 0 0 242.282962 57.334136a139.882962 139.882962 0 0 1-184.948826 184.948826A506.698134 506.698134 0 0 0 0 380.932932a140.376159 140.376159 0 0 1 0 262.134136 525.562914 525.562914 0 0 0 57.334136 138.64997 139.882962 139.882962 0 0 1 184.948826 184.948826 525.562914 525.562914 0 0 0 138.64997 57.334136 140.376159 140.376159 0 0 1 262.134136 0 525.562914 525.562914 0 0 0 138.64997-57.334136 139.882962 139.882962 0 0 1 184.948826-184.948826 506.698134 506.698134 0 0 0 57.334136-138.64997A140.807706 140.807706 0 0 1 933.868272 511.691752zM511.691752 652.437809A140.437809 140.437809 0 1 1 652.437809 511.691752 140.499458 140.499458 0 0 1 511.691752 652.437809z"
          fill="#1D85ED"
          p-id="3516"
          @click="stteing()"
        ></path>
      </svg>
      <LoginButton></LoginButton>
      <LogupButton></LogupButton>
      <LogOut v-if="$store.state.ButtonAuthority[6].LogOutButton"></LogOut>
    </div>
    <h1 class="Title" @click="$router.push('/')">欢迎来到集成功能网站</h1>
    <div
      class="LanshareFang"
      v-if="$store.state.ButtonAuthority[4].LanShareView"
    >
      <h1 @click="Lanshare()" class="Lanshare">局域网文件共享系统</h1>
      <ul id="myList">
        <ol @click="$router.push('/LanShareIndex')">
          首页
        </ol>
      </ul>
    </div>
    <div
      class="LanshareFang"
      v-if="$store.state.ButtonAuthority[4].LanShareView"
      @click="$router.push('/ChatRoomIndex')"
    >
      <h1 class="Lanshare">聊天功能</h1>
    </div>
  </div>
</template>

<script>
// import LoginButton from "@/components/ViewLogIn/LoginButton.vue";
import LoginButton from "@/components/UrseState/ViewLogIn/LoginButton.vue";
import LogupButton from "@/components/UrseState/ViewLogup/LogupButton.vue";
import LogOut from "@/components/UrseState/LogOut.vue";
export default {
  name: "HomePages",
  components: {
    LoginButton,
    LogupButton,
    LogOut,
  },

  data() {
    return {};
  },
  methods: {
    stteing() {
      this.$store.state.FilesTyoes = "设置";
      console.log((this.$store.state.FilesTyoes = "设置"));
      this.$store.state.dialogVisible = true;
    },
    Lanshare() {
      const list = document.getElementById("myList");
      if (list.style.maxHeight) {
        list.style.maxHeight = null;
      } else {
        list.style.display = "block";
        requestAnimationFrame(() => {
          list.style.maxHeight = list.scrollHeight + "px";
        });
      }
    },
  },
};
</script>
<style scoped>
.homePages {
  padding: 20px;
  color: white;
}

.icon {
  transition: all 0.3s ease;
}
.icon:hover {
  transform: scale(1.2);
  cursor: pointer;
  filter: brightness(1.2);
}

.Title {
  text-align: center;
  margin: 15px 0;
  font-size: 1vw;
  font-weight: 500;
  transition: color 0.3s ease;
}
.Title:hover {
  cursor: pointer;
  color: #42b983;
}

.Title1 {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 15px;
  padding: 10px 0;
}

.LanshareFang {
  background-color: #e74c3c;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}
.LanshareFang:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.Lanshare {
  text-align: center;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1vw;
  transition: all 0.3s ease;
}
.Lanshare:hover {
  cursor: pointer;
  background-color: #c0392b;
}

#myList {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s cubic-bezier(0.33, 1, 0.68, 1);
  cursor: pointer;
  font-size: 0.8vw;
  background-color: #e74c3c;
  padding: 0 20px;
  text-align: center;
}

#myList ol {
  padding: 10px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  transition: background-color 0.3s ease;
}
#myList ol:hover {
  background-color: #c0392b;
}

@media (max-width: 768px) {
  .Title {
    font-size: 1rem;
    margin: 10px 0;
  }
  .Lanshare {
    height: 32px;
    font-size: 0.9rem;
  }
}
</style>
