<template>
  <div>
    <el-button
      @click="
        $store.state.dialogVisible = true;
        FilesTyoe('上传目录');
      "
    >
      上传目录
    </el-button>
  </div>
</template>
<script>
export default {
  name: "updataDirBuuton",
  methods: {
    FilesTyoe(FilesTyoes) {
      this.$store.state.FilesTyoes = FilesTyoes;
      this.$store.state.files = [];
    },
  },
};
</script>
