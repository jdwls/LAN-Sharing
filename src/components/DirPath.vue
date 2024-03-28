<<<<<<< HEAD
<template>
    <div>
        <h1>路径:{{ $store.state.DirPath }}</h1>
    </div>
</template>
<script>
import axios from 'axios'
export default{
    name:'DirPath',
    data(){
        return{
            DirPath:''
        }
    },
     mounted(){
        
            axios({
                url:this.$store.state.api+'/OptionDir',
                method:"post",
            }).then(res=>{
                this.$store.state.DirPath=res.data.data
                if(res.data.type=='成功选择目录'){
                    window.location.reload()
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
}
=======
<template>
    <div>
        <h1>路径:{{ $store.state.DirPath }}</h1>
    </div>
</template>
<script>
import axios from 'axios'
export default{
    name:'DirPath',
    data(){
        return{
            DirPath:''
        }
    },
     mounted(){
        
            axios({
                url:this.$store.state.api+'/OptionDir',
                method:"post",
            }).then(res=>{
                this.$store.state.DirPath=res.data.data
                if(res.data.type=='成功选择目录'){
                    window.location.reload()
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
}
>>>>>>> 87f22de17 (tshi)
</script>