<template>
  <div>
    <el-button @click="NewTextButton()">新建文本</el-button>
  </div>
</template>
<script>
export default {
  name: "NewTextButton",
  methods: {
    NewTextButton() {
      console.log("text");
      this.$store.state.FilesTyoes = "文本";
      this.$store.state.dialogVisible = true;
    },
  },
};
</script>
