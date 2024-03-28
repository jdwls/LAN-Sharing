<<<<<<< HEAD
<template>
<div>
    <el-button @click="NewDir">新建文件</el-button>
</div>
</template>

<script>
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
export default{
    name:"NewDir",
    methods:{
        NewDir(){
    ElMessageBox.prompt('请输入文件名:', '新建文件夹', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    inputPattern:
    /^[a-zA-Z0-9_-]+$/,
    inputErrorMessage: '请输入文件名',
  })
    .then(({ value }) => {
      ElMessage({
        type: 'success',
        message: `你文件夹名称是:${value}`,

      })
      axios({
        url:this.$store.state.api+'/NewDir',
        method:"get",
        params:{
            'NewDirName':value,
            'NewDirPath':this.$store.state.DirPath
        }
      }).then(res=>{
        if(res.data=='成功'){
            axios({
            url:this.$store.state.api+'/DirsFileList',
            method:"post",
            params:{
                            'DirsFileList':this.$store.state.DirPath
                        },
        }).then(res=>{
            console.log(res.data.data);
            this.$store.state.DirsFileList=res.data.data
            for(let i=0;i<this.$store.state.DirsFileList.length;i++){
            this.$store.state.DirsFileList[i]={'index':i,'data':this.$store.state.DirsFileList[i],"FileType":false}
            axios({
                url:this.$store.state.api+"/OpenDir",
                method:'post',
            }).then(res=>{
                let h=Object.values(res.data.su)
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    for(let j=0;j<=h.length;j++){
                        if(this.$store.state.DirsFileList[i].data==h[j]){
                            this.$store.state.DirsFileList[i].FileType='文件夹'
                            break
                        }
                    }
                }
                    
            }) 
        }
        })
        axios({
                    url:this.$store.state.api+"/filesypess",
                    method:"get",
                    params:{
                'filesypessPath':this.$store.state.DirPath
            }
        }).then(res=>{
            this.$store.state.otherDirsType=res.data.data
            let h=Object.values(res.data.filesypessPathlistTypes)
            for(let i=0;i<h.length;i++){
                this.$store.state.DirsFileList[h[i].index].FileType=h[i].filesypessPathlistType
            }
        })
        }
      })
      
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '你取消新建文件夹',
      })
    })
        }
    }
}
=======
<template>
<div>
    <el-button @click="NewDir">新建文件</el-button>
</div>
</template>

<script>
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
export default{
    name:"NewDir",
    methods:{
        NewDir(){
    ElMessageBox.prompt('请输入文件名:', '新建文件夹', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    inputPattern:
    /^[a-zA-Z0-9_-]+$/,
    inputErrorMessage: '请输入文件名',
  })
    .then(({ value }) => {
      ElMessage({
        type: 'success',
        message: `你文件夹名称是:${value}`,

      })
      axios({
        url:this.$store.state.api+'/NewDir',
        method:"get",
        params:{
            'NewDirName':value,
            'NewDirPath':this.$store.state.DirPath
        }
      }).then(res=>{
        if(res.data=='成功'){
            axios({
            url:this.$store.state.api+'/DirsFileList',
            method:"post",
            params:{
                            'DirsFileList':this.$store.state.DirPath
                        },
        }).then(res=>{
            console.log(res.data.data);
            this.$store.state.DirsFileList=res.data.data
            for(let i=0;i<this.$store.state.DirsFileList.length;i++){
            this.$store.state.DirsFileList[i]={'index':i,'data':this.$store.state.DirsFileList[i],"FileType":false}
            axios({
                url:this.$store.state.api+"/OpenDir",
                method:'post',
            }).then(res=>{
                let h=Object.values(res.data.su)
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    for(let j=0;j<=h.length;j++){
                        if(this.$store.state.DirsFileList[i].data==h[j]){
                            this.$store.state.DirsFileList[i].FileType='文件夹'
                            break
                        }
                    }
                }
                    
            }) 
        }
        })
        axios({
                    url:this.$store.state.api+"/filesypess",
                    method:"get",
                    params:{
                'filesypessPath':this.$store.state.DirPath
            }
        }).then(res=>{
            this.$store.state.otherDirsType=res.data.data
            let h=Object.values(res.data.filesypessPathlistTypes)
            for(let i=0;i<h.length;i++){
                this.$store.state.DirsFileList[h[i].index].FileType=h[i].filesypessPathlistType
            }
        })
        }
      })
      
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '你取消新建文件夹',
      })
    })
        }
    }
}
>>>>>>> 87f22de17 (tshi)
</script>