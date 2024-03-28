<<<<<<< HEAD
<template>
    <div>
    <el-button @click="ViewButton(ViewButtonOfficEword)" > 查看文件</el-button>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name:"ViewButton",
    props:['ViewButtonOfficEword'],
    data(){
        return{
            fty:['.doc','.zip',]
        }
    },
    methods:{
        ViewButton(ViewButtonOfficEword){
            axios({
                url:this.$store.state.api+'/fileypess',
                method:'get',
                params:{
                    'ViewButtonOfficEword':this.$store.state.DirPath+'/'+ViewButtonOfficEword
                }
            }).then(res=>{
                this.$store.state.FilesTyoes=res.data.data
                
                
            })
            this.$store.state.VideoPlayercontrols=true
            this.$store.state.dialogVisible=true
            this.$store.state.OfficEword=ViewButtonOfficEword
        }
    }

}
=======
<template>
    <div>
    <el-button @click="ViewButton(ViewButtonOfficEword)" > 查看文件</el-button>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name:"ViewButton",
    props:['ViewButtonOfficEword'],
    data(){
        return{
            fty:['.doc','.zip',]
        }
    },
    methods:{
        ViewButton(ViewButtonOfficEword){
            axios({
                url:this.$store.state.api+'/fileypess',
                method:'get',
                params:{
                    'ViewButtonOfficEword':this.$store.state.DirPath+'/'+ViewButtonOfficEword
                }
            }).then(res=>{
                this.$store.state.FilesTyoes=res.data.data
                
                
            })
            this.$store.state.VideoPlayercontrols=true
            this.$store.state.dialogVisible=true
            this.$store.state.OfficEword=ViewButtonOfficEword
        }
    }

}
>>>>>>> 87f22de17 (tshi)
</script>