<template>
  <div>
    <el-button @click="dropFile(dropFiles)" id="myButton"> 删除文件</el-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "dropFiles",

  props: ["dropFiles"],
  methods: {
  async  dropFile(dropFiles) {
      // let button = document.getElementById("myButton");
      // button.setAttribute("disabled", false);
      axios({
        url: this.$store.state.api + "/dropFiles",
        method: "get",
        params: {
          dropFilesName: this.$store.state.DirPath + "/" + dropFiles,
        },
      }).then((res) => {
        if (res.data.type == "删除文件成功") {
        this.$store.dispatch("DirsFileList");
        }
      })
      .catch((err) => {
        console.log(err);
      });
      
    },
  },
};
</script>
<style scoped></style>
