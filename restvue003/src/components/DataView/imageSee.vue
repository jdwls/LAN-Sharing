<template>
  <div>
    <el-image :src="imageSeesrc()" @load="tess(e)"></el-image>
  </div>
</template>

<script>
export default {
  name: "imageSee",
  props:['src'],
  methods: {
    imageSeesrc() {
      // console.log(this.$store.state.DirPath);
      
      if(this.$store.state.DirPath==null){
        console.log(this.$store.state.DirPath);
        return (
        this.$store.state.api +"/imageSee?imageSeeName=" +this.src
        // this.$store.state.DirPath +
        // "/" +
        
      );
      }
      return (
        this.$store.state.api +
        "/imageSee?imageSeeName=" +
        this.$store.state.DirPath +
        "/" +
        this.$store.state.OfficEword
      );
    },
    tess(e) {
      console.log(e);
    },
  },
};
</script>
