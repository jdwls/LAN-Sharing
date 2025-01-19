<template>
    <div>
        <el-button @click="Logup()">注册</el-button>
    </div>
</template>
<script>
// import axios from 'axios'
export default{
    name:"LogupButton",
    methods:{
        Logup(){
            console.log('text');
            this.$store.state.FilesTyoes='注册'
            this.$store.state.dialogVisible=true
        
    }
}
}
</script>