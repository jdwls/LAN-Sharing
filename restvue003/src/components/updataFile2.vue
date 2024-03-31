<template>
  <div>
    <el-row>
      <el-col :span="4"> <vue-upload-component ref="upload" :post-action="$store.state.api + '/uploaders'" directory
          multiple v-model="files" @click="fiel()" @input-file="inputFile" :thread="5" :data="additionalData">
          <el-button>上传目录</el-button>
        </vue-upload-component></el-col>
      <el-col :span="4"><el-button @click="startUpload">开始上传</el-button></el-col>
      <el-col :span="4"><el-button @click="clearFiles(files)">取消选择</el-button></el-col>
    </el-row>

    <div v-for="i in $store.state.files" :key="i">
      <el-row>
        <el-col :span="4">文件名: {{ i.name }}</el-col>
        <el-col :span="4">大小:{{ SuLvZhuangHuang(i.size) }}</el-col>
      </el-row>
    </div>

  </div>
</template>
<script>
import axios from 'axios';
import { ElNotification } from 'element-plus'
import VueUploadComponent from 'vue-upload-component'
// import progressEl from '@/components/progressEl.vue'
export default {
  name: "updataFile2",
  components: {
    'vue-upload-component': VueUploadComponent
  },
  data() {
    return {
      uploadedCount: 0,
      totalFiles: 0,
      totalSize: 0,
      uploadPercentage: 10,
      files: [],
      additionalData: {
        uploadpath: this.$store.state.DirPath
      }

    }
  },
  methods: {
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
    inputFile(newl) {
      // for(let i=0;i<this.$store.state.files.length;i++)
      // if( this.$store.state.files[i].size !==0){
      //  console.log(this.$store.state.files[i].response);
      // }l

      console.log(this.$store.state.files);
      this.$store.state.files = this.files

      if (newl.error != '') {
        ElNotification({
          title: '错误',
          message: newl.error,
          duration: 0,
        })
      }
      if (newl.success == true) {
        ElNotification({
          title: '成功',
          message: newl.progress,
          duration: 3000,
        })

        axios({
          url: this.$store.state.api + '/DirsFileList',
          method: "post",
          params: {
            'DirsFileList': this.$store.state.DirPath
          },
        }).then(res => {
          console.log(res.data.data);
          this.$store.state.DirsFileList = res.data.data
          for (let i = 0; i < this.$store.state.DirsFileList.length; i++) {
            this.$store.state.DirsFileList[i] = { 'index': i, 'data': this.$store.state.DirsFileList[i], "FileType": false }
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
          }
        })
      }



    },
    startUpload() {
      for (let i = 0; i < this.$store.state.files.length; i++)
        if (this.$store.state.files[i].size !== 0) {
          this.$refs.upload.active = true
          this.$store.state.FilesTyoes = '进度条'
          this.$store.state.files[i].progress = Number(this.$store.state.files[i].progress)

        }
      console.log(this.files);


    },
    fiel() {
      for (let i = 0; i < this.$store.state.files.length; i++)
        if (this.$store.state.files[i].size !== 0) {
          this.$store.state.files[i].size = Number(this.$store.state.files[i].size)

        }

    },
    clearFiles(files) {
      if (this.files.length != 0) {
        this.$refs.upload.remove(files)
        this.$store.state.files = []
      }

    },



  }

}
</script>
