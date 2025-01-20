<template>
    <div   class="InputStyle">
        <el-form :model="form" label-width="auto"  style="width: 45%">
            <el-form-item label="用户名:">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="密码:">
                <el-input v-model="form.password" show-password></el-input>
            </el-form-item>
            <el-form-item label="在输入一次密码:">
                <el-input v-model="form.Twopassword" show-password></el-input>
            </el-form-item>
            <el-button type="primary" @click="submitForm()">注册</el-button>
            <el-button @click="resetForm()">重置</el-button>
        </el-form>
    </div>
</template>

<script>
import {  ElMessageBox } from 'element-plus'
import axios from 'axios';
import {KeyMain}from '@/components/Common/KeyMain.js'
export default{
    name:'LogupView',
    data(){
        return{
            form:{
                name:"",
                password:"",
                Twopassword:""
            }
        }
    },
    methods:{
        submitForm(){    
            const UsesCheck=/^[A-Za-z0-9_]{6,12}$/
            const passwordCheck=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,16}$/
            if (this.form.name=='' || this.form.password=='' || this.form.Twopassword==''){
                ElMessageBox.alert("用户名和密码不能为空", '为空检测', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).then(()=>{
                this.form.name='' 
                this.form.password=''
                this.form.Twopassword=''
               }).catch(()=>{
                console.log('无');
                
               })
               return 0
            }
            if (this.form.name.match(UsesCheck)==null){
                ElMessageBox.alert("用户名只能包含大小写字母、数字和下划线，且长度在6到12个字符之间", '用户名错误', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).then(()=>{
                this.form.name='' 
                this.form.password=''
                this.form.Twopassword=''
                    
               }).catch(()=>{
                console.log('无');
                
               })
               return 0
            }
            if ( this.form.password.match(passwordCheck)==null){
                ElMessageBox.alert("一个大写字母、一个小写字母、一个数字和一个特殊字符，且长度至少为8个字符", '密码错误', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).then(()=>{
                this.form.name='' 
                this.form.password=''
                this.form.Twopassword=''  
               }).catch(()=>{
                console.log('无');
                
               })
               
               return 0
            }
            if(this.form.password!=this.form.Twopassword){
                ElMessageBox.alert("第一次输入的密码需要第二次一样", '密码没有重复', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).then(()=>{
                this.form.name='' 
                this.form.password=''
                this.form.Twopassword=''
                    
               }).catch(()=>{
                console.log('无');
                
               })
               return 0
            }
            if (this.form.password.match(passwordCheck)!=null && this.form.Twopassword.match(passwordCheck)!=null && this.form.name.match(UsesCheck)!=null && this.form.Twopassword!='' && this.form.password!='' && this.form.name){
                axios({ 
                    url:this.$store.state.api+'/Logup',
                    method:"get",
                    params:{
                    'name':this.form.name,
                    'MD5AESBehind': KeyMain(this.form.password)  ,
                    'Time':Date.now(),
                }
                }).then(res=>{
                    console.log(res.data.error);
                    
                    if(res.data.error=='用户名已经存在,请重新输入用户名'){
                        ElMessageBox.alert("用户名已经存在："+res.data.message, '用户名已经存在', {
                        showConfirmButton:true,
                        confirmButtonText: '确认',
                        }).then(()=>{
                            return 0
                        }).catch(()=>{
                            return 0
                        })
                    }
                    else{
                        ElMessageBox.alert("用户创建名为："+res.data.message, '用户创建成功', {
                        showConfirmButton:true,
                        confirmButtonText: '确认',
                    }).then(()=>{
                        this.form.name='' 
                        this.form.password=''
                        this.form.Twopassword=''
                        this.$store.state.dialogVisible=false
                        this.$store.state.FilesTyoes='登录'
                        this.$store.state.dialogVisible=true
                    })
                    .catch(()=>{
                        return 0
                    })
                    }
                   
                }
           ) }
        },
        resetForm(){
            ElMessageBox.alert("重置成功", '重置成功', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).then(()=>{
                this.form.name='' 
                this.form.password=''
                this.form.Twopassword=''
               }).catch(()=>{
                console.log('无');
                
               })
               return 0
            
        }
    }
}
</script>
<style scoped>
.InputStyle{
    padding-bottom: 2%;
    display: flex;
    justify-content: center;
    align-content: center;
}
</style>