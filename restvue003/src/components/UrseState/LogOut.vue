<template>
    <div>
        <el-button type="primary" @click="LogOut">注销</el-button>
    </div>
</template>

<script>
// import { ElMessageBox } from "element-plus";
import axios from "axios";
// import {disconnectSocket} from '@/socke/index.js'
export default {
    name: "LogOut",
    methods: {
        LogOut() {
            axios({
                url: this.$store.state.api + '/IsOlineNumber',
                method: "get",
                params: {
                    urse_Name: localStorage.getItem("UresName"),
                }
            })
                .then(() => {
                    localStorage.removeItem('Authority');
                    localStorage.removeItem('Time');
                    localStorage.removeItem('UresName');
                    this.$store.dispatch("Tokers");
                    this.$router.push("/");
                })
                .catch()



        }
    }
}
</script>
