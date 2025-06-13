<template>
  <div>
    <el-button @click="dropFile(dropFiles)" id="myButton"> 删除文件</el-button>
  </div>
</template>

<script>
import axios from "axios";
import { ElMessageBox } from "element-plus";
export default {
  name: "dropFiles",

  props: ["dropFiles"],
  methods: {
    async dropFile(dropFiles) {
      ElMessageBox.alert(
        "是否删除" + dropFiles + "的文件",
        "是否确认删除文件",
        {
          showConfirmButton: true,
          showCancelButton: true,
          confirmButtonText: "确认",
          cancelButtonText: "取消",
        }
      )
        .then(async () => {
          axios({
            method: "get",
            url: this.$store.state.api + "/dropFiles",
            params: {
              dropFilesName: this.$store.state.DirPath + "/" + dropFiles,
            },
          }).then((res) => {
            if (res.data.type == "删除文件成功") {
              this.$store.dispatch("DirsFileList");
            }
          });
        })
        .catch(() => {
          console.log("成功取消");
        });
    },
  },
};
</script>
<style scoped></style>
