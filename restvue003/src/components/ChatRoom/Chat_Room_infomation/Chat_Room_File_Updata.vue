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
                ref="Chat_Room_File_Updata_input_ref" multiple
                accept=".jpg,.jpeg,.png,.gif,.bmp,.webp,.svg,.mp4,.webm,.ogg,.apng,.avif,.bmp,.quicktime,.x-matroska,.mpeg" />
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
            let FileS_name_arr=[]
            let FileS_Types=[]
            const fileIput = this.$refs.Chat_Room_File_Updata_input_ref
            const file = fileIput.files;
            if (file) {
                for (let i = 0; i < file.length; i++) {
                    const formData = new FormData()
                    console.log(file[i].name);
                    formData.append('file', file[i]); // 字段名与后端一致
                    formData.append('file_name', file[i].name);
                    // formData.append('file_type', file[i].type);
                    formData.append('send_name', localStorage.getItem('UresName'));
                    formData.append('report_name', this.$store.state.currentChat);
                    formData.append('Time', new Date().getTime())
                    FileS_name_arr.push(file[i].name)
                    FileS_Types.push(file[i].type)
                    if(i==file.length-1){
                    FileS_name_arr=JSON.stringify(FileS_name_arr)
                    FileS_Types=JSON.stringify(FileS_Types)
                    formData.append('FileS_Types',FileS_Types )
                    formData.append('FileS_name_arr',FileS_name_arr )
                    console.log(FileS_name_arr);
                    }
                    else{
                    formData.append('FileS_name_arr',false )
                    formData.append('FileS_Types',false)
                    }
                    axios({
                        url: this.$store.state.api + '/Chat_Room_File_Updata_api',
                        method: 'post',
                        data: formData,
                        headers: {
                            'Content-Type': 'multipart/form-data',
                        }
                    })
                        .then((res) => {
                            console.log(res);
                        })
                        .catch((err) => {
                            console.log(err);
                        })
                }
                setTimeout(async () => {
                      seend_message_Files_fun(this.$store.state.currentChat);  
                       this.$refs.Chat_Room_File_Updata_input_ref.value=''
                }, 1000)
                
                
            }
             
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