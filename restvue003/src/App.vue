<template>
  <div class="App">
    <div class="HomePages">
      <HomePages></HomePages>
    </div>
    <div class="list-FlieList">
      <router-view></router-view>
    </div>
    <DiaLog></DiaLog>
  </div>
</template>
<script>
import DiaLog from "@/components/DiaLog.vue";
import HomePages from "@/components/Home/HomePages.vue";
export default {
  name: "App",
  components: {
    DiaLog,
    HomePages,
  },
mounted() {
    this.$store.dispatch("Tokers");
},  
}
</script>
<style>
#app {
  width: 100%;
  height: 100%;
}
.App {
  width: 99%;
  height: 100%;
  display: flex;
  margin-top: 1vh;
}
.HomePages {
  width: 17vw;
  height: 99vh;
  background-color: coral;
}
.list-FlieList {
  width: 80%;
  height: 100%;
}
.toolbar-table {
  width: auto;
  height: 8vh;
  display: flex;
  justify-content: center;
  gap: 3vw;
}
.Dirpath {
  text-align: center;
}
</style>
