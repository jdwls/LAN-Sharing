<template>
  <div>
    <el-dialog  v-model="$store.state.dialogVisible" :title="$store.state.FilesTyoes" width="60%" webkitdirectory :destroy-on-close=true>
      <span>
        <updataFile1 v-if='$store.state.FilesTyoes == "上传文件"'></updataFile1>
        <updataFile2test v-show='$store.state.FilesTyoes == "上传目录"'> </updataFile2test>
        <progressEl v-if='$store.state.FilesTyoes == "进度条"'></progressEl>
        <OfficEword v-if='$store.state.FilesTyoes == ".docx"'></OfficEword>
        <OfficExcel v-if='$store.state.FilesTyoes == ".xlsx"'></OfficExcel>
        <OfficPdf v-if='$store.state.FilesTyoes == ".pdf"'></OfficPdf>
        <VideoPlay v-if='$store.state.FilesTyoes == ".mp4"'></VideoPlay>
        <imageSee v-if='$store.state.FilesTyoes == ".jpg"'></imageSee>
        <imageSee v-if='$store.state.FilesTyoes == ".png"'></imageSee>
        <imageSee v-if='$store.state.FilesTyoes == ".gif"'></imageSee>
        <textSee v-if='$store.state.FilesTyoes == ".txt"'></textSee>
        <NewText v-if='$store.state.FilesTyoes == "文本"'></NewText>
        <Login v-if='$store.state.FilesTyoes == "登录"'></Login>

      </span>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="dialogVisible()">
            取消
          </el-button>
        </span>
      </template>
    </el-dialog>

  </div>
</template>
<script>
import updataFile1 from '@/components/updataFile1.vue'
import updataFile2test from '@/components/updataFile2test.vue'
import progressEl from '@/components/progressEl.vue'
import OfficEword from '@/components/OfficEword.vue'
import OfficExcel from '@/components/OfficExcel.vue'
import OfficPdf from '@/components/OfficPdf.vue'
import VideoPlay from '@/components/VideoPlay.vue'
import imageSee from '@/components/imageSee.vue'
import textSee from '@/components/textSee.vue'
import NewText from '@/components/NewText.vue'
import Login from '@/components/ViewLogIn/Login.vue'
export default {
  name: 'DiaLog',
  components: {
    updataFile1, updataFile2test, progressEl, OfficEword, OfficExcel, OfficPdf, VideoPlay, imageSee, textSee,NewText,Login
  }, 
  methods: {
    dialogVisible() {
      this.$store.state.dialogVisible = false
      this.$store.state.VideoPlayercontrols = false
    }
  }
}
</script>