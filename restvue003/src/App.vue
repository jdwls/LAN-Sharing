<template>
  <div>
    <div class="luj">
      <el-row>
        <el-col :span="24">
          <Dirpath></Dirpath>
          <LoginButton></LoginButton>
          <LogupButton> </LogupButton>
        </el-col>
      </el-row>
    </div>
    <div class="nmnm">
      <el-row class="row-bg">
        <el-col :span="7">

        </el-col>
        <el-col :span="4">
          <updataFile></updataFile>
        </el-col>

        <el-col :span="2">
          <selectedDir></selectedDir>
        </el-col>

        <el-col :span="2">
          <TopLevelDirectory></TopLevelDirectory>
        </el-col>

        <el-col :span="2">
          <NewDir></NewDir>
        </el-col>
        <el-col :span="2">
          <NewTextButton></NewTextButton>
        </el-col>
      </el-row>
    </div>
    <!-- <updataFile></updataFile>
  <selectedDir></selectedDir>
    <TopLevelDirectory></TopLevelDirectory>
  <NewDir></NewDir> -->

    <DirsFileList class="luj"></DirsFileList>
  </div>
</template>
<script>
import NewTextButton from '@/components/NewTextButton.vue'
import Dirpath from '@/components/DirPath.vue'
import updataFile from '@/components/updataFile.vue'
import selectedDir from '@/components/selectedDir.vue'
import DirsFileList from '@/components/DirsFileList.vue'
import NewDir from '@/components/NewDir.vue'
import TopLevelDirectory from '@/components/TopLevelDirectory.vue'
import LoginButton from '@/components/ViewLogIn/LoginButton.vue'
import LogupButton from '@/components/ViewLogup/LogupButton.vue'


export default {
  name: "App",
  components: {
    Dirpath, updataFile, selectedDir, DirsFileList, NewDir, TopLevelDirectory,NewTextButton,LoginButton,LogupButton
  },


}
</script>
<style>
#app {
  height: 100%;
  width: 100%;
  overflow-y: hidden;
}

.luj {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.nmnm{
  padding-bottom  : 2%;
}
</style>