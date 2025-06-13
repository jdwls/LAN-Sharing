<template>
    <div>
        <el-button type="primary" @click="LogOut">注销</el-button>
    </div>
</template>

<script>
// import { ElMessageBox } from "element-plus";
// import axios from "axios";
export default {
    name: "LogOut",
    methods: {
        LogOut() {
            localStorage.removeItem('Authority');
            localStorage.removeItem('Time');
            localStorage.removeItem('UresName');
            this.$store.dispatch("Tokers");
            this.$router.push("/");
        }
    }
}
</script>
