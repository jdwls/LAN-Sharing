<template>
    <div>
        <label for="inputfile">
            <input type="file" @change="testop()" ref="yu" Multiple id="inputfile" v-show="0" />
            <span @change="testop()" class="spanxx">上传文件</span>
        </label>
        <span>{{ filesize() }}</span>
        <button @change="scyu()">上传文件</button>
        <el-table :data="file" border style="width: 100%" v-if="file.length != 0" class="pp">
            <el-table-column prop="name" label="Name" width="180"></el-table-column>
            <el-table-column prop="size" label="size" width="180"></el-table-column>
            <el-table-column label="drop" width="180">
                <template #default="scope">
                    <el-button @click=" files(scope.row.i, scope.row.name)">删除文件</el-button>

                </template>
            </el-table-column>
        </el-table>


    </div>
</template>

<script>
// import axios from 'axios';

export default {
    name: "updataFile1test",
    data() {
        return {
            file: [],
            filelist: []
        }
    },
    methods: {
        filesize() {
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
        async testop() {
            this.filelist = this.$refs.yu.files
            this.file = Array.from(this.filelist).map((file, index) => ({ name: file.name, size: file.size, i: index }));
            // let file = []
            // for (let i = 0; i < this.filelist.length; i++) {
            //     file[i] = { 'name': this.filelist[i].name, 'size': this.SuLvZhuangHuang(this.filelist[i].size), 'index': i }
            // }
            // this.$refs.yu.value = ''
            // for (let j = 0; j < this.filelist.length; j++) {
            //     console.log(this.filelist.files[j]);
            // }
        },
        files(index, name) {
            this.file = this.file.slice(1, index)
            // this.filelist = this.filelist.delete.index
            this.file = Array.from(this.filelist).map((file, index) => ({ name: file.name, size: file.size, i: index }));
            console.log(name);

            // this.filelist = this.filelist.splice(1, index)

        },
        scyu() {
            const formData = new FormData();
            formData.append('file', this.filelist);
            // axios({
            //     url: this.$store.state.api + '/uploader',
            //     method: 'POST',
            //     data: formData,
            //     headers: {
            //         'Content-Type': 'multipart/form-data'
            //     }
            // })
        }
    }

}
</script>

<style scoped>
.pp {
    height: 320px;
    overflow-y: auto;
}

.spanxx {
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
</style>