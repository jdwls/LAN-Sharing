<template>
  <div>
    <el-button @click="downloadFlie(down)">下载文件</el-button>
  </div>
</template>
<script>
export default {
  name: "downloadFlie",
  props: ["down"],
  data() {
    return {
      url: "",
    };
  },
  methods: {
    downloadFlie(s) {
      let url =
        this.$store.state.api +
        "/download?downloadPathName=" +
        this.$store.state.DirPath +
        "/" +
        s +
        "&downloadName=" +
        s;
      window.location.href = url;
    },
  },
};
</script>
