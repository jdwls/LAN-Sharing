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
import DiaLog from "./components/DiaLog.vue";
import HomePages from "./components/Home/HomePages.vue";

export default {
  name: "App",
  components: {
    DiaLog,
    HomePages,
  },
  mounted() {
    this.$store.dispatch("Tokers");
  },
};
</script>

<style>
:root {
  --sidebar-bg: #2c3e50;
  --main-bg: #f5f7fa;
  --text-color: white;
  --transition-time: 0.3s;
}

#app, .App {
  width: 100%;
  min-height: 100vh;
  will-change: transform;
}

#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.App {
  display: flex;
  flex-direction: row;
  transition: transform var(--transition-time) ease, flex-direction var(--transition-time) ease;
}

.HomePages {
  width: 250px;
  min-width: 200px;
  max-width: 300px;
  min-height: 100vh;
  background-color: var(--sidebar-bg);
  color: var(--text-color);
  transition: width var(--transition-time) ease, max-width var(--transition-time) ease;
  will-change: width, max-width;
}

.list-FlieList {
  flex: 1;
  padding: 20px;
  background-color: var(--main-bg);
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
