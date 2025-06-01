<template>
  <div class="homePages">
    <div class="Title1">
      <el-avatar
        shape="square"
        size="3vw"
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
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
    </div>
    <h1 class="Title" @click="$router.push('/')">欢迎来到集成功能网站</h1>
    <div class="LanshareFang">
      <h1 @click="Lanshare()" class="Lanshare">局域网文件共享系统</h1>
      <ul id="myList">
        <ol @click="$router.push('/LanShareIndex')">
          首页
        </ol>
      </ul>
    </div>
  </div>
</template>

<script>
import LoginButton from "@/components/ViewLogIn/LoginButton.vue";
import LogupButton from "@/components/ViewLogup/LogupButton.vue";
export default {
  name: "HomePages",
  components: {
    LoginButton,
    LogupButton,
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
      console.log("列表项被点击了", list);
    },
  },
};
</script>
<style scoped>
.icon:hover {
  transform: scale(1.2);
  cursor: pointer;
}
.Title {
  text-align: center;
  margin-top: 1vh;
  margin-bottom: 1vh;
}
.Title1 {
  display: flex;
  justify-content: space-around;
}
.Lanshare:hover {
  cursor: pointer;
}
.LanshareFang {
  background-color: rgb(254, 91, 32);
}
h1 {
  padding: 0;
  margin: 0;
}
.Lanshare {
  text-align: center;
  height: 3vh;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-content: center;
}
#myList {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s cubic-bezier(0.33, 1, 0.68, 1);
  cursor: pointer;
  font-size: 1vw;
  background-color: rgb(254, 91, 32);
}
</style>
