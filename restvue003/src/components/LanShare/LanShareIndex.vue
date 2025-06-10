<template>
  <div >
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
import NewTextButton from "@/components/NewTextButton.vue";
import updataFile from "@/components/updataFileButton.vue";
import selectedDir from "@/components/selectedDir.vue";
import DirsFileList from "@/components/DirsFileList.vue";
import NewDir from "@/components/NewDir.vue";
import TopLevelDirectory from "@/components/TopLevelDirectory.vue";
import updataDirBuuton from "@/components/updataDirBuuton.vue";
import DirPath from '@/components/DirPath.vue'
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
