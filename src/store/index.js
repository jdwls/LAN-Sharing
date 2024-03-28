<<<<<<< HEAD
import { createStore } from 'vuex'

export const store = createStore({
  state () {
    return {
     api:'http://192.168.2.100:2525',
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
=======
import { createStore } from 'vuex'

export const store = createStore({
  state () {
    return {
     api:'http://192.168.3.200:2525',
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
>>>>>>> 87f22de17 (tshi)
})