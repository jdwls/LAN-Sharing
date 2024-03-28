<template>
    <div>
       <el-button @click="downloadFlie(down)">下载文件</el-button>
    </div>
</template>
<script>
// import axios from 'axios';
// import download from "downloadjs"

export default{
    name:'downloadFlie',
    props:['down'],
    data(){
        return{
            url:''
        }
    },
    methods:{
       

        downloadFlie(s){
            // axios({
            //     url:this.$store.state.api+'/download',
            //     method:'get',
            //     params:{
            //         'downloadName':s,
            //         'downloadPathName':this.$store.state.DirPath+'/'+s,

            //     },
            //      responseType: 'blob'
            // })
         
        //   console.log(p);
            // .then(res=>{
                // if(res.data.type=='成功下载'){
                    let url=this.$store.state.api+'/download?downloadPathName='+this.$store.state.DirPath+'/'+s+'&downloadName='+s
                    window.location.href=url
                    // return url
                    // download(url)
                    // axios({
                    //     url:urldown,
                    //     method:'get',
                    //     success: download.bind(true, urldown)
                    // })
                    

                // }
            // })
        }
    }
}
</script>