<template>
    <div>
        <el-button @click="dropFile(dropFiles)" id="myButton"> 删除文件</el-button>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: 'dropFiles',

    props: ['dropFiles'],
    methods: {
        dropFile(dropFiles) {
            let button = document.getElementById('myButton')
            button.setAttribute('disabled', false)
            axios({
                url: this.$store.state.api + '/dropFiles',
                method: 'get',
                params: {
                    'dropFilesName': this.$store.state.DirPath + '/' + dropFiles
                },


            }).then(res => {
                if (res.data.type == '删除文件成功') {

                    axios({
                        url: this.$store.state.api + '/DirsFileList',
                        method: "post",
                        params: {
                            'DirsFileList': this.$store.state.DirPath
                        },
                    }).then(res => {
                        this.$store.state.DirsFileList = res.data.data
                        for (let i = 0; i < this.$store.state.DirsFileList.length; i++) {
                            this.$store.state.DirsFileList[i] = { 'index': i, 'data': this.$store.state.DirsFileList[i], "FileType": '查看文件' }

                        }

                    })
                }
                button.setAttribute('disabled', true)
                if (res.data.type == '删除文件夹成功') {
                    axios({
                        url: this.$store.state.api + '/' + 'DirsFileList',
                        method: "post",
                        params: {
                            'DirsFileList': 'no'
                        }
                    }).then(res => {

                        this.$store.state.DirsFileList = res.data.data
                        for (let i = 0; i < this.$store.state.DirsFileList.length; i++) {
                            this.$store.state.DirsFileList[i] = { 'index': i, 'data': this.$store.state.DirsFileList[i], "FileType": false }
                        }
                    })
                    axios({
                        url: this.$store.state.api + "/OpenDir",
                        method: 'post',
                    }).then(res => {
                        let h = Object.values(res.data.su)
                        for (let i = 0; i < this.$store.state.DirsFileList.length; i++) {
                            for (let j = 0; j <= h.length; j++) {
                                if (this.$store.state.DirsFileList[i].data == h[j]) {
                                    this.$store.state.DirsFileList[i].FileType = '文件夹'
                                    break
                                }
                            }
                        }

                    })

                    axios({
                        url: this.$store.state.api + "/filesypess",
                        method: "get",
                        params: {
                            'filesypessPath': this.$store.state.DirPath
                        }
                    }).then(res => {
                        this.$store.state.otherDirsType = res.data.data
                        let h = Object.values(res.data.filesypessPathlistTypes)
                        for (let i = 0; i < h.length; i++) {
                            this.$store.state.DirsFileList[h[i].index].FileType = h[i].filesypessPathlistType
                        }
                    })
                }
            })
        }


    }
}
</script>
<style scoped></style>