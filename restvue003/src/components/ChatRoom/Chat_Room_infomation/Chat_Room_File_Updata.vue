<template>
    <div>
        <div class="chat-room-file-updata">
            <svg t="1754017969599" class="icon" viewBox="0 0 1024 1024" version="1.1" p-id="1548" width="40" height="40"
                @click="Chat_Room_File_Updata_uploadFile_fun()">
                <path
                    d="M371.2 455.111111L483.555556 343.893333v262.826667a28.444444 28.444444 0 1 0 56.888888 0v-262.826667L652.8 455.111111a28.444444 28.444444 0 0 0 40.106667-40.106667L532.195556 256a28.444444 28.444444 0 0 0-40.106667 0l-160.995556 160.995556A28.444444 28.444444 0 0 0 371.2 455.111111zM739.555556 663.608889a28.444444 28.444444 0 0 0-28.444445 28.444444v28.444445H312.888889v-28.444445a28.444444 28.444444 0 0 0-56.888889 0v56.888889a28.444444 28.444444 0 0 0 28.444444 28.444445h455.111112a28.444444 28.444444 0 0 0 28.444444-28.444445v-56.888889a28.444444 28.444444 0 0 0-28.444444-28.444444z"
                    p-id="1549"></path>
            </svg>
            <input type="file" @change="Chat_Room_File_Updata_input_handleFileUpload()" v-show="false"
                ref="Chat_Room_File_Updata_input_ref" multiple />
        </div>
    </div>

</template>

<script>
import axios from 'axios';

import { seend_message_Files_fun } from "@/socke/index.js";

export default {
    name: 'Chat_Room_File_Updata',
    methods: {
        Chat_Room_File_Updata_uploadFile_fun() {
            const fileIput = this.$refs.Chat_Room_File_Updata_input_ref
            fileIput.click();
        },
        Chat_Room_File_Updata_input_handleFileUpload() {
            const fileIput = this.$refs.Chat_Room_File_Updata_input_ref
            const file = fileIput.files;
            const formData = new FormData()
            console.log(file);
            if (file) {
                for (let i = 0; i < file.length; i++) {
                    formData.append('file', file[i]);
                    formData.append('FileInput', file[i]);  // 字段名与后端一致
                    formData.append('file_name', file[i].name);
                    formData.append('file_type', file[i].type);
                    formData.append('send_name', localStorage.getItem('UresName'));
                    formData.append('report_name', this.$store.state.currentChat);
                    axios({
                        url: this.$store.state.api + '/Chat_Room_File_Updata_api',
                        method: 'post',
                        data: formData,
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                        .then((res) => {
                            if(res.data.ms=='文件上传成功'){
                                seend_message_Files_fun(file[i].name,this.$store.state.currentChat,this.$store.state.messages_lists.length,file[i].type)
                            }
                        })
                        .catch((err) => {
                            console.log(err);
                        })
                }

            }
            else {
                console.log("没有选择文件");
            }
            // if(file){
            //     const formData = new FormData();
            //     formData.append('file', file);
            //     // 这里可以添加上传文件的逻辑，比如使用axios发送POST请求
            //     this.$emit('file-uploaded', formData); // 向父组件发送事件，传递文件数据
            // } else {
            //     console.error("没有选择文件");
            // }
        }
    }

}
</script>

<style scoped>
.icon {
    cursor: pointer;
}

.icon:hover {
    background-color: azure;
}
</style>