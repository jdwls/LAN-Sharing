<template>
    <div>
        <div class="juzhong">
            <label for="inputfile">
                <input type="file" @change="selectFile()" ref="yu" Multiple v-show=0 id="inputfile" />
                <span class="buttonbrlue">选择文件</span>
            </label>
            <span>{{ viewNumbers() }}</span>
            <button @click="upadtaFiles()" class="buttonyellow" v-if="file.length != 0">上传文件</button>
        </div>
        <el-table :data="file" border style="width: 100%" v-if="file.length != 0" class="tableheight">
            <el-table-column prop="name" label="Name" width="180"></el-table-column>
            <el-table-column prop="size" label="size" width="180"></el-table-column>
            <el-table-column label="drop" width="180">
                <template #default="scope">
                    <el-button @click=" dropfiles(scope.row.name)">删除文件</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: "updataFile1test",
    data() {
        return {
            file: [],
            dropflie: null,
            filelist: null
        }
    },
    methods: {
        viewNumbers() {
            if (this.file != 0)
                return this.file.length + '个文件'
            return '请选择目录'
        },
        SuLvZhuangHuang(i) {
            if (i < 1024) {
                return i.toFixed(2) + ' B/s';
            } else if (i < 1024 * 1024) {
                return (i / 1024).toFixed(2) + ' KB/s';
            } else if (i < 1024 * 1024 * 1024) {
                return (i / (1024 * 1024)).toFixed(2) + ' MB/s';
            } else {
                return (i / (1024 * 1024 * 1024)).toFixed(2) + ' GB/s';
            }
        },
        selectFile() {
            this.filelist = this.$refs.yu.files
            console.log(this.filelist);
            let file = []
            for (let i = 0; i < this.filelist.length; i++) {
                file[i] = { 'name': this.filelist[i].name, 'size': this.SuLvZhuangHuang(this.filelist[i].size), 'index': i }
            }
            this.file = file
        },
        dropfiles(name) {
            this.file = this.file.filter(function (i) {
                return i.name != name
            })
            this.dropflie = []
            this.dropflie.push(name)
        },
        upadtaFiles() {
            for (let i = 0; i < this.filelist.length; i++) {
                if (this.dropflie == null) {
                    let fromdata = new FormData()
                    fromdata.append('file', this.filelist[i])
                    axios({
                        url: this.$store.state.api + '/uploader',
                        method: "post",
                        data: fromdata
                    })
                } else {
                    if (!this.dropflie.includes(this.filelist[i].name)) {
                        let fromdata = new FormData()
                        fromdata.append('file', this.filelist[i])
                        axios({
                            url: this.$store.state.api + '/uploader',
                            method: "post",
                            data: fromdata
                        })
                    }
                }
            }
        }
    }

}
</script>
<style scoped>
.tableheight {
    height: 320px;
    overflow-y: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.buttonbrlue {
    background-color: rgb(64, 158, 255);
    border: none;
    color: white;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    opacity: 0.8;
}

.juzhong {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.buttonyellow {
    background-color: rgb(239, 210, 22);
    border: none;
    color: white;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    opacity: 0.8;
}
</style>