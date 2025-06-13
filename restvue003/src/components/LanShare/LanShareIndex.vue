<template>
  <div v-if="$store.state.ButtonAuthority[5].DirsFileList">
    <DirPath class="DirPath"></DirPath>
  <div class="toolbar-table">
    <updataFile></updataFile>
    <updataDirBuuton></updataDirBuuton>
    <selectedDir></selectedDir>
    <TopLevelDirectory></TopLevelDirectory>
    <NewDir></NewDir>
    <NewTextButton></NewTextButton>
  </div>
  <div>
    <DirsFileList></DirsFileList>
  </div>   
  </div>
</template>
<script>
import NewTextButton from "@/components/LanShare/LanShareIndexButton/NewTextButton.vue";
import updataFile from "@/components/LanShare/LanShareIndexButton/updataFileButton.vue";
import selectedDir from "@/components/LanShare/LanShareIndexButton/selectedDir.vue";
import DirsFileList from "@/components/LanShare/LanShareData/DirsFileList.vue";
import NewDir from "@/components/LanShare/LanShareIndexButton/NewDir.vue";
import TopLevelDirectory from "@/components/Common/VueCommon/TopLevelDirectory.vue";
import updataDirBuuton from "@/components/LanShare/LanShareIndexButton/updataDirBuuton.vue";
import DirPath from '@/components/LanShare/DirPath.vue'
export default {
  name: "LanShareIndex",
  components: {
    updataFile,
    selectedDir,
    DirsFileList,
    NewDir,
    TopLevelDirectory,
    NewTextButton,
    updataDirBuuton,
    DirPath
  },
};
</script>
<style scoped>
.DirPath{
  font-size: 1.1vw;
  text-align: center;
}
</style>
