// import axios from 'axios'
import axios from 'axios'
import { createStore } from 'vuex'

export const store = createStore({
  state () {
    return {
     api:'http://192.168.2.26:2525',
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
     VideoPlayercontrols:true,
     ViewButtonOfficEword:''
    }
  },
  actions:{
    DirsFileList(){
      let DirsFileList=[]
      axios({
        url: this.state.api + '/' + 'DirsFileList',
        method: "post",
        params: {
            'DirsFileList': 'no'
        }
      }).then(res => {
        DirsFileList = res.data.data
        for (let i = 0; i < DirsFileList.length; i++) {
            DirsFileList[i] = { 'index': i, 'data': DirsFileList[i], "FileType": false }
        }
        this.commit('DirsFileList',DirsFileList)
      })
      
      
      
      
    },
    openDirs(){
      axios({
        url: this.state.api + "/OpenDir",
        method: 'post',
    }).then(res => {
        let h = Object.values(res.data.su)
        for (let i = 0; i < this.state.DirsFileList.length; i++) {
            for (let j = 0; j <= h.length; j++) {
                if (this.state.DirsFileList[i].data == h[j]) {
                    this.state.DirsFileList[i].FileType = '文件夹'
                    break
                }
            }
        }

    })
    },
    ViewButton(){
      
        axios({
          url:this.state.api+'/fileypess',
          method:'get',
          params:{
              'ViewButtonOfficEword':this.state.ViewButtonOfficEword
          }
      }).then(res=>{
          this.state.FilesTyoes=res.data.data
          console.log(res.data.data);
          
          
          
      })
      this.state.VideoPlayercontrols=true
      this.state.dialogVisible=true
      this.state.OfficEword=this.state.ViewButtonOfficEword
    },
    filesypess(){
      axios({
        url:this.state.api+"/filesypess",
        method:"get",
        params:{
    'filesypessPath':this.state.DirPath
      }
      }).then(res=>{
      this. state.otherDirsType=res.data.data
      let h=Object.values(res.data.filesypessPathlistTypes)
      for(let i=0;i<h.length;i++){
          this.state.DirsFileList[h[i].index].FileType=h[i].filesypessPathlistType
      }
      })     
    },
      },
mutations:{
  DirsFileList(state,newDate){
    state.DirsFileList=newDate
  },
  ViewButtonOfficEword(state,newDate){
    state.ViewButtonOfficEword=newDate
    console.log(newDate);
    
  }
}
})