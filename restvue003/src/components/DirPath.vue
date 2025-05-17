<template>
  <div>
    <h1>局域网文件共享系统</h1>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "DirPath",
  data() {
    return {
      DirPath: "",
    };
  },
  mounted() {
    axios({
      url: this.$store.state.api + "/OptionDir",
      method: "post",
    }).then((res) => {
      this.$store.state.DirPath = res.data.data;
      if (res.data.type == "成功选择目录") {
        window.location.reload();
      }
    });
  },
};
</script>
