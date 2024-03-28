<<<<<<< HEAD
<template>
    <div>
        <el-button @click="topleveldirectory()" class="tets">
            返回上级目录
        </el-button>
    </div>
</template>
<script defer>
import axios from 'axios';


export default{
    name:"TopLevelDirectory",
    methods:{
        topleveldirectory(){
            document.querySelector('.tets').classList.add('disabled')
            let m=this.$store.state.DirPath.split('/')
            console.log(m.length);
            if(m.length>2){
            axios({
                url:this.$store.state.api+'/TopLevelDirectory',
                method:'get',
                params:{
                    'TopLevelDirectoryPathName':this.$store.state.DirPath
                }
            }).then(res=>{
                if(res.data.data!==''){
                this.$store.state.DirPath=res.data.data
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
        })
    } 
    
})
        }
        else{
            
                axios({
                url:this.$store.state.api+'/OptionDir',
                method:"post",
            }).then(res=>{
                this.$store.state.DirPath=res.data.data
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
         })
           
        }
        setTimeout(function(){
            document.querySelector(".tets").classList.remove('disabled')
        },1000)
    }
    }
}
</script>
<style scoped>
.disabled{
    pointer-events: none;
}
=======
<template>
    <div>
        <el-button @click="topleveldirectory()" class="tets">
            返回上级目录
        </el-button>
    </div>
</template>
<script defer>
import axios from 'axios';


export default{
    name:"TopLevelDirectory",
    methods:{
        topleveldirectory(){
            document.querySelector('.tets').classList.add('disabled')
            let m=this.$store.state.DirPath.split('/')
            console.log(m.length);
            if(m.length>2){
            axios({
                url:this.$store.state.api+'/TopLevelDirectory',
                method:'get',
                params:{
                    'TopLevelDirectoryPathName':this.$store.state.DirPath
                }
            }).then(res=>{
                if(res.data.data!==''){
                this.$store.state.DirPath=res.data.data
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
        })
    } 
    
})
        }
        else{
            
                axios({
                url:this.$store.state.api+'/OptionDir',
                method:"post",
            }).then(res=>{
                this.$store.state.DirPath=res.data.data
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
         })
           
        }
        setTimeout(function(){
            document.querySelector(".tets").classList.remove('disabled')
        },1000)
    }
    }
}
</script>
<style scoped>
.disabled{
    pointer-events: none;
}
>>>>>>> 87f22de17 (tshi)
</style>