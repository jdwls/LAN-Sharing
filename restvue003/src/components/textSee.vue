<template>
  <div>
    <pre>{{ textSeedata }}</pre>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "textSee",
  data() {
    return {
      textSeedata: "",
    };
  },
  mounted() {
    axios({
      url: this.$store.state.api + "/textSee",
      method: "get",
      params: {
        textSee: this.$store.state.DirPath + "/" + this.$store.state.OfficEword,
      },
    })
      .then((res) => {
        this.textSeedata = res.data;
      })
      .catch((error) => {
        console.error("Error fetching text data:", error);
        this.textSeedata = "无法加载文本数据。";
      });
  },
};
</script>
