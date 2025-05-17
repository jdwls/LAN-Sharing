<template>
  <div>
    <div class="luj">
      <Dirpath></Dirpath>
    </div>
    <div style="display: flex; justify-content: center">
      <div
        style="
          display: flex;
          gap: 1vw;
          justify-content: center;
          align-items: center;
          margin-bottom: 1%;
          padding: 0.5%;
          background: #f5f7fa;
          border-radius: 8px;
          box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
          border: 1px solid #ebeef5;
          width: auto;
        "
      >
        <LoginButton></LoginButton>
        <LogupButton></LogupButton>
        <updataFile></updataFile>
        <updataDirBuuton></updataDirBuuton>
        <selectedDir></selectedDir>
        <TopLevelDirectory></TopLevelDirectory>
        <NewDir></NewDir>
        <NewTextButton></NewTextButton>
      </div>
    </div>
    <div>
      <DirsFileList class="luj"></DirsFileList>
    </div>
    <div>
      <DiaLog></DiaLog>
    </div>
  </div>
</template>
<script>
import NewTextButton from "@/components/NewTextButton.vue";
import Dirpath from "@/components/DirPath.vue";
import updataFile from "@/components/updataFileButton.vue";
import selectedDir from "@/components/selectedDir.vue";
import DirsFileList from "@/components/DirsFileList.vue";
import NewDir from "@/components/NewDir.vue";
import TopLevelDirectory from "@/components/TopLevelDirectory.vue";
import LoginButton from "@/components/ViewLogIn/LoginButton.vue";
import LogupButton from "@/components/ViewLogup/LogupButton.vue";
import updataDirBuuton from "./components/updataDirBuuton.vue";
import DiaLog from "@/components/DiaLog.vue";
export default {
  name: "App",
  components: {
    Dirpath,
    updataFile,
    selectedDir,
    DirsFileList,
    NewDir,
    TopLevelDirectory,
    NewTextButton,
    LoginButton,
    LogupButton,
    updataDirBuuton,
    DiaLog,
  },
};
</script>
<style>
#app {
  height: 100%;
  width: 100%;
}

.luj {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.toolbar-table {
  width: auto;
  margin: 0 auto;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.toolbar-table .el-table__cell {
  padding: 0;
  border: none;
  background: transparent !important;
}

.toolbar-table .el-table__body-wrapper {
  overflow: auto;
}
</style>
