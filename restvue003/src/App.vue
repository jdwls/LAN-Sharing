<template>
  <div>
  <el-row>
    <el-col :span="24"><Dirpath></Dirpath></el-col>
</el-row>
<el-row class="row-bg" >
<el-col :span="4"><updataFile></updataFile></el-col>

<el-col :span="2"><selectedDir></selectedDir></el-col>

<el-col :span="2"><TopLevelDirectory></TopLevelDirectory></el-col>

<el-col :span="2"><NewDir></NewDir></el-col>
</el-row>
  <!-- <updataFile></updataFile>
  <selectedDir></selectedDir>
    <TopLevelDirectory></TopLevelDirectory>
  <NewDir></NewDir> -->

  <DirsFileList></DirsFileList>
  </div>
</template>
<script>
import Dirpath from '@/components/DirPath.vue'
import updataFile from '@/components/updataFile.vue'
import selectedDir from '@/components/selectedDir.vue'
import DirsFileList from '@/components/DirsFileList.vue'
import NewDir from '@/components/NewDir.vue'
import TopLevelDirectory from '@/components/TopLevelDirectory.vue'



export default{
  name:"App",
  components:{
    Dirpath,updataFile,selectedDir,DirsFileList,NewDir,TopLevelDirectory,
  },

 
}
</script>
<style>
#app{
  height: 100%;
  width: 100%;
}
</style>