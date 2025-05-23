<template>
  <div>
    <el-button @click="NewDir">新建文件夹</el-button>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessage, ElMessageBox } from "element-plus";
export default {
  name: "NewDir",
  methods: {
    NewDir() {
      ElMessageBox.prompt("请输入文件名:", "新建文件夹", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /^[a-zA-Z0-9_-]+$/,
        inputErrorMessage: "请输入文件名",
      })
        .then(({ value }) => {
          axios({
            url: this.$store.state.api + "/NewDir",
            method: "get",
            params: {
              NewDirName: value,
              NewDirPath: this.$store.state.DirPath,
            },
          })
            .then(async (res) => {
              console.log(res.data.message);
              if (res.data.message == "文件夹创建成功") {
                console.log(res.data);

                ElMessage({
                  type: "success",
                  message: `${res.data.message}:${value}`,
                });
                await this.$store.dispatch("DirsFileList");
                await this.$store.dispatch("openDirs");
              }
            })
            .catch((res) => {
              ElMessage({
                type: "error",
                message: `您创建的文件夹${value},${res.data}`,
              });
            });
        })
        .catch(() => {
          ElMessage({
            type: "info",
            message: "你取消新建文件夹",
          });
        });
    },
  },
};
</script>
