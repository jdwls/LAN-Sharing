import { createStore } from 'vuex'

export const store = createStore({
  state () {
    return {
     api:'http://127.0.0.1:2525',
     i:1,
     DirPath:'',
     dialogVisible:false,
     FilesTyoes:'',//获取文件类型，
     DirsFileList:[],
     uploadPercentage:0,
     files:[],
     downZhi:'',
     OfficEword:'',
     otherDirsType:[],
     VideoPlayercontrols:true
    }
  }
})