<<<<<<< HEAD
<template>
    <div>
       <el-button @click="selectedDir">选择根目录</el-button> 
    </div>
</template>

<script>
import axios from 'axios';
import {  ElMessage,ElMessageBox } from 'element-plus'
export default{
    name:'selectedDir',
    methods:{
        
        selectedDir(){
            let api=this.$store.state.api
            axios({
                url:this.$store.state.api+'/'+'selectedDir',
                method:'post'
            }).then(res=>{
                let dirname=res.data.data
                ElMessageBox.confirm(
                    dirname,
                    'Warning',{
                        confirmButtonText: 'OK',
                        cancelButtonText: 'Cancel',
                        type: 'warning',
                    }
                 ).then(()=>{
                    ElMessage({
                        type: 'success',
                        message: dirname,
                        })
                        if(res.data.data!=''){
                            axios({
                            url:api+'/'+'SucceedselectedDir',
                            method:'get',
                            params:{
                            'dirname':res.data.data
                            }
                        }).then(res=>{
                            this.$store.state.DirPath=res.data.data
                            console.log(res.data.data);
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
                axios({
                    url:api+"/filesypess",
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
            }) 
        }
        })
                        })
                        
                        }
                    
                 })
                 .catch(() => {
                ElMessage({
                    type: 'info',
                    message: '取消选择',
      })
    })
            })
            
        }
    }
}
=======
<template>
    <div>
       <el-button @click="selectedDir">选择根目录</el-button> 
    </div>
</template>

<script>
import axios from 'axios';
import {  ElMessage,ElMessageBox } from 'element-plus'
export default{
    name:'selectedDir',
    methods:{
        
        selectedDir(){
            let api=this.$store.state.api
            axios({
                url:this.$store.state.api+'/'+'selectedDir',
                method:'post'
            }).then(res=>{
                let dirname=res.data.data
                ElMessageBox.confirm(
                    dirname,
                    'Warning',{
                        confirmButtonText: 'OK',
                        cancelButtonText: 'Cancel',
                        type: 'warning',
                    }
                 ).then(()=>{
                    ElMessage({
                        type: 'success',
                        message: dirname,
                        })
                        if(res.data.data!=''){
                            axios({
                            url:api+'/'+'SucceedselectedDir',
                            method:'get',
                            params:{
                            'dirname':res.data.data
                            }
                        }).then(res=>{
                            this.$store.state.DirPath=res.data.data
                            console.log(res.data.data);
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
                axios({
                    url:api+"/filesypess",
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
            }) 
        }
        })
                        })
                        
                        }
                    
                 })
                 .catch(() => {
                ElMessage({
                    type: 'info',
                    message: '取消选择',
      })
    })
            })
            
        }
    }
}
>>>>>>> 87f22de17 (tshi)
</script>