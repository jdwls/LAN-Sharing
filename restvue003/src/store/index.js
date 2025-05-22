// import axios from 'axios'
import axios from "axios";
import { createStore } from "vuex";

export const store = createStore({
  state() {
    return {
      api: "http://0.0.0.0:2525",
      i: 1,
      DirPath: "",
      dialogVisible: false,
      FilesTyoes: "", //获取文件类型，
      DirsFileList: [],
      uploadPercentage: 0,
      files: [],
      downZhi: "",
      OfficEword: "",
      otherDirsType: [],
      VideoPlayercontrols: true,
      ViewButtonOfficEword: "",
      upadaFileNumberSum: 0,
    };
  },
  actions: {
    async DirsFileList() {
      // let DirsFileList = [];
      await axios({
        url: this.state.api + "/" + "DirsFileList",
        method: "post",
        params: {
          DirsFileList: this.state.DirPath,
        },
      }).then((res) => {
      this.state.DirsFileList = Object.values(res.data.items)
      });
      
    },
    async openDirs() {
      await axios({
        url: this.state.api + "/OpenDir",
        method: "post",
      }).then((res) => {
        let h = Object.values(res.data.su);
        for (let i = 0; i < this.state.DirsFileList.length; i++) {
          for (let j = 0; j <= h.length; j++) {
            if (this.state.DirsFileList[i].data == h[j]) {
              this.state.DirsFileList[i].FileType = "文件夹";
              break;
            }
          }
        }
      });
    },
    async ViewButton() {
      await axios({
        url: this.state.api + "/fileypess",
        method: "get",
        params: {
          ViewButtonOfficEword: this.state.ViewButtonOfficEword,
        },
      }).then((res) => {
        this.state.FilesTyoes = res.data.data;
        console.log(res.data.data);
      });
      this.state.VideoPlayercontrols = true;
      this.state.dialogVisible = true;
      this.state.OfficEword = this.state.ViewButtonOfficEword;
    },
    // async filesypess(){
    // await  axios({
    //     url:this.state.api+"/filesypess",
    //     method:"get",
    //     params:{
    // 'filesypessPath':this.state.DirPath
    //   }
    //   }).then(res=>{
    //   this.state.otherDirsType=res.data.data
    //   let h=Object.values(res.data.filesypessPathlistTypes)
    //   console.log(h);
    //         console.log(this.state.DirsFileList);
    //   for(let i=0;i<h.length;i++){
    //       // console.log( '1',this.state.DirsFileList[h[i].index].FileType,'12',res.data.filesypessPathlistTypes,'123',h);
    //        this.state.DirsFileList[h[i].index].FileType='查看文件'
    //   }

    //   })
    // },
  },
  mutations: {
    DirsFileList(state, newDate) {
      state.DirsFileList = newDate;
    },
    ViewButtonOfficEword(state, newDate) {
      state.ViewButtonOfficEword = newDate;
      console.log(newDate);
    },
  },
});
