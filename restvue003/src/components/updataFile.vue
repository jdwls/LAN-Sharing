<template>
    <div>
    <el-row>
        <el-col :span="12">  <el-button  @click="$store.state.dialogVisible= true; FilesTyoe('上传文件')"  >
      上传文件
  </el-button></el-col>
  
  <el-col :span="12"><el-button  @click="$store.state.dialogVisible= true;FilesTyoe('上传目录')">
      上传目录
  </el-button>
</el-col>
</el-row>
        <DiaLog></DiaLog>
    </div>
</template>

<script>
import DiaLog from '@/components/DiaLog.vue'
export default{
    name:"updataFile",
    components:{
        DiaLog
    },
    methods:{
        FilesTyoe(FilesTyoes){
            this.$store.state.FilesTyoes=FilesTyoes
            this.$store.state.files=[]
        }
    }
}
</script>