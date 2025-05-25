<template>
  <div>
    <el-col :span="12">
      <el-button
        @click="
          $store.state.dialogVisible = true;
          FilesTyoe('上传文件');
        "
      >
        上传文件
      </el-button>
    </el-col>
  </div>
</template>

<script>
export default {
  name: "updataFile",

  methods: {
    FilesTyoe(s) {
      this.$store.state.FilesTyoes = s;
      this.$store.state.files = [];
    },
  },
};
</script>
<style scoped></style>
