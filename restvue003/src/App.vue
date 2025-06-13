<template>
  <div class="App">
    <div class="HomePages">
      <HomePages></HomePages>
    </div>
    <div class="list-FlieList">
      <router-view ></router-view>
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
  min-height: 100vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.App {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: row;
  transition: all 0.3s ease;
}
.HomePages {
  width: 250px;
  min-width: 200px;
  max-width: 300px;
  min-height: 100vh;
  background-color: #2c3e50;
  color: white;
  transition: all 0.3s ease;
}
.list-FlieList {
  flex: 1;
  padding: 20px;
  background-color: #f5f7fa;
}
.toolbar-table {
  width: auto;
  height: 60px;
  display: flex;
  justify-content: center;
  gap: 20px;
  align-items: center;
}
.Dirpath {
  text-align: center;
}

@media (max-width: 768px) {
  .App {
    flex-direction: column;
  }
  .HomePages {
    width: 100%;
    max-width: 100%;
    min-height: auto;
  }
}
</style>
