<template>
    <div>
        <el-button :class="{ disabled: isDisabled }" @click="topleveldirectory" class="tets">
            返回上级目录
        </el-button>
    </div>
</template>

<script defer>
import axios from 'axios';

export default {
    name: "TopLevelDirectory",
    data() {
        return {
            isDisabled: false, // 使用Vue的数据驱动控制按钮禁用状态
        };
    },
    methods: {
        async topleveldirectory() {
             // 禁用按钮
            let getDirs=await this.getDirs()
            if(getDirs==this.$store.state.DirPath){
                this.isDisabled = true;
                this.isDisabledTiem()
            }
            else{
                await this.TopLevelDirectory()
            }
        },
         async getDirs(){
            const response =
            await axios({
            url: this.$store.state.api + '/getDirs',
            method: 'get',
        });
        return response.data.data; // 返回数据
           }, 
        async isDisabledTiem(){
            setTimeout(() => {
                    this.isDisabled = false;
                }, 1000);
        },
        async TopLevelDirectory(){
        await axios({
                url:this.$store.state.api +'/TopLevelDirectory',
                method:'get',
                params:{
                    'TopLevelDirectoryPathName':this.$store.state.DirPath
                }
            }).then(async res=>{
                if(res.data.type=='成功'){
                    this.$store.state.DirPath=await this.getDirs()
                    this.$store.dispatch('DirsFileList')
                    this.$store.dispatch('openDirs')
                    this.$store.dispatch('filesypess')
                    
                }
                
            })
        }
    }
};
</script>

<style scoped>
.disabled {
    pointer-events: none;
}
</style>
