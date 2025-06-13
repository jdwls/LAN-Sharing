<template>
  <div>
    <el-button @click="selectDir">选择根目录</el-button>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage } from "element-plus";
export default {
  name: "SelectedDir",
  methods: {
    async selectDir() {
      await axios({
        url:this.$store.state.api+"/selectedDir",
        method: "post",
      })
      .then((res) => {
        if (res.data.message == '已经选择目录') {
          ElMessage({
            message: "选择根目录成功",
            type: "success",
          });
          this.$store.state.DirPath = res.data.data;
          this.$store.dispatch('DirsFileList')
        } else {
          ElMessage({
            message: res.data.message,
            type: "error",
          })
          .catch((error) => {
            ElMessage({
              message: "选择根目录失败",
              type: error,
            })
          });
        }
      })
    }
  },
};
</script>
