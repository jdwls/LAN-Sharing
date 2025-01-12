<template>
    <div >
        <el-form  label-position="left">
            <div>
            <el-form-item label="文本名称:"  style="max-width: 70%">
            <el-input  v-model="TextName"/>
            </el-form-item>
        </div>
        
        <div>
        <el-form-item label="文本内容:" style="max-width: 70%">
            <el-input  type="textarea" v-model="TextConter" />      
            </el-form-item>
            
        </div>
      
           
        </el-form> 
        <div class="onSubmitbutton">
            <!-- <el-button type="primary" @click="onSubmit">确认</el-button> -->
            <el-button  type="primary" :plain="true" @click="onSubmit">确认</el-button>
        </div>
       
    </div>
</template>
<script>
import axios from 'axios';
import {  ElMessageBox } from 'element-plus'


export default{
    name:'NewText',
    data(){
        return{
            TextName:'',
            TextConter:'',
            iscatch:0
        }
    },
    methods:{
        onSubmit(){
            if (this.TextName!=''){
                ElMessageBox.alert('是否创建'+this.TextName+"的文本文件", '是否确认创建文本文件', {
                    showConfirmButton:true,
                    showCancelButton:true,
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
               }).catch(()=>{
                
                console.log("成功取消");
                }).then(()=>{
                axios({
                method:"get",
                url:this.$store.state.api+'/TextLnsert',
                params:{
                    'TextName': this.TextName,
                    'TextConter':this.TextConter,
                    'NowPath':this.$store.state.DirPath
                }
            }).then(res=>{
                if(this.iscatch!=1){
                    ElMessageBox.alert(res.data.message, '创建文本状态', {
                    showConfirmButton:true,
                    showCancelButton:true,
                    confirmButtonText: '再来一个',
                    cancelButtonText: '取消',
               }).catch(()=>{
                this.$store.state.dialogVisible=false
                this.iscatch=1
                console.log( this.iscatch);
               })
                }
               

            })
                this.$store.dispatch('DirsFileList')
                this.$store.dispatch('openDirs')
                this.$store.dispatch('filesypess')
                    
                })
 
    }
        else{
            console.log('当前文件名为空');
            
        }
            
        }
    }

}   
</script>
<style scoped>
.el-form-item{
    /* padding-top: 1%;    */
    margin: 0 auto;
    margin-top: 1%  ;
}
.onSubmitbutton{
    display: flex;
    justify-content: center;
    margin-top: 1%  ;       
}
</style>