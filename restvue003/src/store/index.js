// import axios from 'axios'
import axios from "axios";
import { createStore } from "vuex";

export const store = createStore({
  state() {
    return {
      api: "http://127.0.0.1:2525",
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
      await axios({
        url: this.state.api + "/" + "DirsFileList",
        method: "post",
        params: {
          DirsFileList: this.state.DirPath,
        },
      })
        .then((res) => {
          this.state.DirsFileList = Object.values(res.data.items);
        })
        .catch((err) => {
          console.error("获取目录文件列表失败:", err);
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
    OptionDir(){
  axios({
      url: this.state.api + "/OptionDir",
      method: "post",
    }).then((res) => {
      this.state.DirPath = res.data.data;
      if (res.data.type == "成功选择目录") {
        window.location.reload();
      }
    });
  },
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
