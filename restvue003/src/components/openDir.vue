<template>
  <div>
    <el-button @click="openDirs(openDir)">打开目录</el-button>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "openDir",
  props: ["openDir"],
  data() {
    return {
      path: "",
    };
  },
  methods: {
    openDirs(openDir) {
      axios({
        url: this.$store.state.api + "/openDirs",
        method: "get",
        params: {
          OpenDirsName: this.$store.state.DirPath + "/" + openDir,
        },
      }).then((res) => {
        if (res.data.type == "成功") {
          this.$store.state.DirPath = res.data.dirName;
          this.$store.dispatch("DirsFileList");
        }
      });
    },
  },
};
</script>
