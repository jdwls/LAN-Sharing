<template>
     <el-table :data="$store.state.files" style="width: auto" border max-height="75vh" >
            <el-table-column :label=UpdataTotal>
            <el-table-column prop="data" label="文件名" width="360vw"  align="center" >
                <template #default="scope" >
                        <span>{{scope.row.name}}</span>
                  </template>
            </el-table-column>
            <el-table-column prop="data" label="文件大小" width="240vw" align="center"  >
                <template #default="scope" >
                        <span>{{FileSize(scope.row.size)}}</span>
                  </template>
            </el-table-column>
            <el-table-column prop="data" label="上传速度" width="240vw" align="center" >
                <template #default="scope" >
                        <span>速度:{{ SuLvZhuangHuang(scope.row.speed)}}</span>
                  </template>
            </el-table-column>
            <el-table-column prop="data" label="进度条" width="200vw" align="center">
                <template #default="scope" >
                         <el-progress :percentage="Number(scope.row.progress)"  :text-inside="true" :stroke-width="18"></el-progress> 
                  </template>
            </el-table-column>
            </el-table-column>
     </el-table>
    <!-- </div> -->
</template>

<script>


export default{
    name:"progressEl",
    data() {
        return {
            size:""
        }
    },
    computed:{
        UpdataTotal(){
            return    "当前文件上传总数为："+this.$store.state.upadaFileNumberSum+"个文件,已经上传"+this.$store.state.files.length+"个文件"

        }
    },
    methods:{
        SuLvZhuangHuang(i){
    if (i < 1024) {
            return i.toFixed(2) + ' B/s';
            } else if (i < 1024 * 1024) {
            return (i / 1024).toFixed(2) + ' KB/s';
            } else if (i < 1024 * 1024 * 1024) {
            return (i / (1024 * 1024)).toFixed(2) + ' MB/s';
            } else {
            return (i / (1024 * 1024 * 1024)).toFixed(2) + ' GB/s';
            }
},
        
        FileSize(i) {
         if (i < 1024) {
            return i.toFixed(2) + ' B';
            } else if (i < 1024 * 1024) {
            return (i / 1024).toFixed(2) + ' KB';
            } else if (i < 1024 * 1024 * 1024) {
            return (i / (1024 * 1024)).toFixed(2) + ' MB';
            } else {
            return (i / (1024 * 1024 * 1024)).toFixed(2) + ' GB';
            }
    },
      

}
}
</script>