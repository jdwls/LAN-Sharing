<template>
  <div>
    <el-button @click="Login()">登录</el-button>
  </div>
</template>
<script>
// import axios from 'axios'
export default {
  name: "LoginButton",
  methods: {
    Login() {
      console.log("text");
      this.$store.state.FilesTyoes = "登录";
      this.$store.state.dialogVisible = true;
    },
  },
};
</script>
