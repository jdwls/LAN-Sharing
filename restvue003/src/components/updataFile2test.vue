<template>
    <div>
        <label for="selectionDirs">
            <input type="file" @change="selectionDirs" id="selectionDirs" directory multiple webkitdirectory ref="updataDirs" v-show="0">
            <span class="buttonbulrs" >选择目录</span>
            <span>{{ viewNumbers() }}</span>
        </label>
        <span @click="updataDirs()" class="buttonbulrs" v-if="filedir.length != 0">上传目录</span>
        <el-table :data="filedir" border style="width: 100%" v-if="filedir.length!=0" class="tableheight" lazy> 
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

export default{
    name:"updataFile2test",
    data(){
        return{
            filedir:[],
            dropflie:null
        }
    },
    methods:{
        selectionDirs(){
            this.filedir = this.$refs.updataDirs.files
            console.log( this.filedir);
            let file=[]
            for (let i = 0; i < this.filedir.length; i++) {
                file[i] = { 'name': this.filedir[i].webkitRelativePath, 
                'size': this.filedir[i].size,
                 'index': i }
            }
            this.filedir=file
        },
        dropfiles(name){
            this.filedir = this.filedir.filter(function (i) {
                if(i.name != name){   
                    return i.name != name
                }
                
                
            })
            this.dropflie = []
            this.dropflie.push(name)
        },
        async updataDirs(){
            let uploadedBytesnold=0
            for(let i=0;i<this.filedir.length;i++){
                let fromdata = new FormData()
                fromdata.append('file', this.$refs.updataDirs.files[i])
                if(this.dropflie==null){
                    await axios({
                        url: this.$store.state.api + '/uploaders',
                        method: "post",
                        data: fromdata,
                        onUploadProgress: progressEvent => {
                            let persent = (progressEvent.loaded / progressEvent.total * 100 | 0)
                            let uploadedBytes = progressEvent.loaded;
                            let uploadedBytesnew=uploadedBytes
                            let speeds=uploadedBytesnew-uploadedBytesnold
                            this.$store.state.FilesTyoes = '进度条'
                
                            this.$store.state.files[i]=
                            {
                            'name':this.$refs.updataDirs.files[i].name,
                            'size':this.$refs.updataDirs.files[i].size,
                            'id':i,
                            'progress':persent,
                            'speed':speeds,
                        }
      },                   
                    })
                }
            }
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
        })
        },
        viewNumbers(){
            if (this.filedir != 0)
                return this.filedir.length + '个文件'
            return '请选择目录'
        }
    }
}
</script>
<style scoped>
.buttonbulrs {
    background-color: rgb(21, 194, 197);
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
.tableheight{
    height: 320px;
}
</style>