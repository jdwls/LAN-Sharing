<template>
  <div>
    <el-dialog v-model="$store.state.dialogVisible" :title="$store.state.FilesTyoes" width="60%" webkitdirectory
      :destroy-on-close="true" 
      :before-close="Show_Progress_el_notification()">
      <span>
        <updataFile1 v-show="$store.state.FilesTyoes == '上传文件'"></updataFile1>
        <updataFile2test v-show="$store.state.FilesTyoes == '上传目录'"></updataFile2test>
        <progressEl v-show="$store.state.FilesTyoes == '进度条'"></progressEl>
        <OfficEword v-if="$store.state.FilesTyoes == '.docx'"></OfficEword>
        <OfficExcel v-if="$store.state.FilesTyoes == '.xlsx'"></OfficExcel>
        <OfficPdf v-if="$store.state.FilesTyoes == '.pdf'"></OfficPdf>
        <VideoPlay v-if="$store.state.FilesTyoes == '.mp4'"></VideoPlay>
        <imageSee v-if="$store.state.FilesTyoes == '.jpg'"></imageSee>
        <imageSee v-if="$store.state.FilesTyoes == '.png'"></imageSee>
        <imageSee v-if="$store.state.FilesTyoes == '.gif'"></imageSee>
        <textSee v-if="$store.state.FilesTyoes == '.txt'"></textSee>
        <NewText v-if="$store.state.FilesTyoes == '文本'"></NewText>
        <textSee v-if="$store.state.FilesTyoes == '.json'"></textSee>
        <Login v-if="$store.state.FilesTyoes == '登录'"></Login>
        <LogupView v-if="$store.state.FilesTyoes == '注册'"></LogupView>
        <steeingView v-if="$store.state.FilesTyoes == '设置'"></steeingView>
      </span>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="dialogVisible()"> 取消 </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
<script>
import updataFile1 from "@/components/LanShare/LanShareIndexButton/updataFile1.vue";
import updataFile2test from "@/components/LanShare/LanShareIndexButton/updataFile2.vue";
import progressEl from "@/components/Common/VueCommon/progressEl.vue";
import OfficEword from "@/components/DataView/OfficEword.vue";
import OfficExcel from "@/components/DataView/OfficExcel.vue";
import OfficPdf from "@/components/DataView/OfficPdf.vue";
import VideoPlay from "@/components/DataView/VideoPlay.vue";
import imageSee from "@/components/DataView/imageSee.vue";
import textSee from "@/components/DataView/textSee.vue";
import NewText from "@/components/LanShare/LanShareIndexButton/NewText.vue";
import Login from "@/components/UrseState/ViewLogIn/Login.vue";
import LogupView from "@/components/UrseState/ViewLogup/LogupView.vue"
import steeingView from "@/components/Common/VueCommon/steeingView.vue";
import ClickShowProgress from "@/components/Common/VueCommon/ClickShowProgress.vue"
import { h } from "vue";


export default {
  name: "DiaLog",
  components: {
    updataFile1,
    updataFile2test,
    progressEl,
    OfficEword,
    OfficExcel,
    OfficPdf,
    VideoPlay,
    imageSee,
    textSee,
    NewText,
    Login,
    LogupView,
    steeingView,
    // ClickShowProgress,
  },
  methods: {
    dialogVisible() {
      this.$store.state.dialogVisible = false;
      this.$store.state.VideoPlayercontrols = false; // 关闭视频播放器控制条
    },
    Show_Progress_el_notification() {
      if (this.$store.state.FilesTyoes == '进度条' && this.$store.state.dialogVisible==false) {
        this.$nextTick(() => {
        this.$notify({
          title: '上传进度',
          dangerouslyUseHTMLString: true,
          message:h(ClickShowProgress),        
          duration: 0,
        });
         });
      }
      
    }
  },
};
</script>
