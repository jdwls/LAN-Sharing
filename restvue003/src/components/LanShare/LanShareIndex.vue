<template>
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
</template>
<script>
import NewTextButton from "@/components/NewTextButton.vue";
import updataFile from "@/components/updataFileButton.vue";
import selectedDir from "@/components/selectedDir.vue";
import DirsFileList from "@/components/DirsFileList.vue";
import NewDir from "@/components/NewDir.vue";
import TopLevelDirectory from "@/components/TopLevelDirectory.vue";
import updataDirBuuton from "@/components/updataDirBuuton.vue";
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
  },
};
</script>
