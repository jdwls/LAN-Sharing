<<<<<<< HEAD
<template>
    <div>
        <el-button @click="openDirs(openDir)">打开目录</el-button>
    </div>
</template>
<script>
import axios from 'axios';


export default{
    name:"openDir",
    props:['openDir'],
    data(){
        return{
            path:''
        }
    },
    methods:{
        openDirs(openDir){
            axios({
                url:this.$store.state.api+'/openDirs',
                method:'get',
                params:{
                    'OpenDirsName': this.$store.state.DirPath+'/'+openDir
                }
            }).then(res=>{
                this.$store.state.DirsFileList=res.data.data
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    this.$store.state.DirsFileList[i]={'index':i,'data':this.$store.state.DirsFileList[i],"FileType":false}
                        }
                this.$store.state.DirPath=res.data.dirName
               
                let h=Object.values(res.data.su)
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    for(let j=0;j<=h.length;j++){
                        if(this.$store.state.DirsFileList[i].data==h[j]){
                            this.$store.state.DirsFileList[i].FileType='文件夹'
                            break
                        }
                    }
                }
                  this.path= openDir 
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
                })
           
        }
    }
   
  
}
=======
<template>
    <div>
        <el-button @click="openDirs(openDir)">打开目录</el-button>
    </div>
</template>
<script>
import axios from 'axios';


export default{
    name:"openDir",
    props:['openDir'],
    data(){
        return{
            path:''
        }
    },
    methods:{
        openDirs(openDir){
            axios({
                url:this.$store.state.api+'/openDirs',
                method:'get',
                params:{
                    'OpenDirsName': this.$store.state.DirPath+'/'+openDir
                }
            }).then(res=>{
                this.$store.state.DirsFileList=res.data.data
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    this.$store.state.DirsFileList[i]={'index':i,'data':this.$store.state.DirsFileList[i],"FileType":false}
                        }
                this.$store.state.DirPath=res.data.dirName
               
                let h=Object.values(res.data.su)
                for(let i=0;i<this.$store.state.DirsFileList.length;i++){
                    for(let j=0;j<=h.length;j++){
                        if(this.$store.state.DirsFileList[i].data==h[j]){
                            this.$store.state.DirsFileList[i].FileType='文件夹'
                            break
                        }
                    }
                }
                  this.path= openDir 
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
                })
           
        }
    }
   
  
}
>>>>>>> 87f22de17 (tshi)
</script>