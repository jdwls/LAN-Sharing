<template>
    <div >
        <div class="InputStyle"> 
            <span>用户名:</span><el-input v-model="Uses" style="width: 30%" placeholder="请输入用户名" />
        </div>
        <div class="InputStyle">
            <span> 密 码 ：</span><el-input v-model="Password" style="width: 30%" placeholder="请输入密码" type='password' show-password/>
        </div>
        <div class="InputStyle" >
            <el-button @click=LogIn()>登录</el-button>
        </div>
    </div>
</template>

<script>
import {  ElMessageBox } from 'element-plus'
// import CryptoJS from 'crypto-js';
import axios from 'axios';
import {KeyMain}from '@/components/Common/KeyMain.js'
export default{
    name:'LogLn',
    data(){
        return{
            Uses:"",
            Password:''
        }
    },
    methods:{
        LogIn(){
            
            const UsesCheck=/^[A-Za-z0-9_]{6,12}$/
            const passwordCheck=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,16}$/
            if (this.Uses=='' && this.Password=='' ){
                ElMessageBox.alert("用户名和密码不能为空", '为空检测', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).catch(()=>{
                   this.Uses=''
                   this.Password=''
                    
               })
               return 0
            }
            if (this.Uses.match(UsesCheck)==null){
                ElMessageBox.alert("用户名只能包含大小写字母、数字和下划线，且长度在6到12个字符之间", '用户名错误', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).catch(()=>{
                    this.Uses=''
                    this.Password=''
                    
               })
               return 0
            }
            if (this.Password.match(passwordCheck)==null){
                ElMessageBox.alert("一个大写字母、一个小写字母、一个数字和一个特殊字符，且长度至少为8个字符", '密码错误', {
                    showConfirmButton:true,
                    confirmButtonText: '确认',
               }).catch(()=>{
                   this.Uses=''
                   this.Password=''
                    
               })
               console.log(this.Password );
               
               return 0
            }
            if (this.Password.match(passwordCheck)!=null && this.Uses.match(UsesCheck)!=null && this.Uses!='' && this.Password!='' ){
                    KeyMain(this.Password)
                
                axios({ 
                    url:this.$store.state.api+'/login',
                    method:"get",
                    params:{
                    'MD5AESBehind': KeyMain(this.Password)  ,
                    'Time':Date.now(),
                }
                })
            }
        }
    }
}
</script>
<style scoped>
/* .Uses{
   
} */
span{
    padding-right: 1%; 
      
} 
.InputStyle{
    padding-bottom: 2%;
    display: flex;
    justify-content: center;
    align-content: center;
}
</style>