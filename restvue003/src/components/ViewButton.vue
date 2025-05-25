<template>
  <div>
    <el-button @click="ViewButton(ViewButtonOfficEword)"> 查看文件</el-button>
  </div>
</template>

<script>
export default {
  name: "ViewButton",
  props: ["ViewButtonOfficEword"],
  data() {
    return {
      fty: [".doc", ".zip"],
    };
  },
  methods: {
    ViewButton(ViewButtonOfficEword) {
      this.$store.commit("ViewButtonOfficEword", ViewButtonOfficEword);
      this.$store.dispatch("ViewButton");
    },
  },
};
</script>
