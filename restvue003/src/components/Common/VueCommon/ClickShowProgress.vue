<template>
  <div>
    <el-button @click="showProgress()" type="primary" round v-if="Is_showProgress()">点击显示进度条</el-button>
    <h4>当前文件上传总数为{{ $store.state.upadaFileNumberSum }}个文件,已经上传{{ $store.state.files.length }}个文件,上传速度{{$store.state.SuLvZhuangHuang_Data_vuex }}</h4>
  </div>
</template>

<script>
export default {
  name: 'ClickShowProgress',
  computed: {
    
  },
  methods: {
    showProgress() {
      this.$store.state.FilesTyoes = '进度条';
      this.$store.state.dialogVisible = true;
    },
    Is_showProgress() {
      if (this.$store.state.upadaFileNumberSum  == this.$store.state.files.length &&  this.$store.state.SuLvZhuangHuang_Data_vuex==0) {
        return false
      } else {
        return true
      }
    }
  },

}
</script>
