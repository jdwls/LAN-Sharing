import axios from "axios";
import { createStore } from "vuex";

export const store = createStore({
  state() {
    return {
      api: "http://192.168.3.75:2525",
      Online_Numbers: [],
      disconnectNumber: [],
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
      ButtonAuthority: [
        { LoginButton: false },
        { LogupButton: false },
        { steeingButton: false },
        { HeadIcon: false },
        { LanShareView: false },
        { DirsFileList: false },
        { LogOutButton: false },
      ],
      Urselist:[],
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
    OptionDir() {
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
    Tokers() {
      let message = axios({
        url: this.state.api + "/Toker",
        method: "get",
        params: {
          Time: localStorage.getItem("Time"),
          Name: localStorage.getItem("UresName"),
        },
      })
        .then((res) => {
          if (
            res.data[1].message == "登录成功" &&
            localStorage.getItem("Authority") == "Ures"
          ) {
            this.state.ButtonAuthority = [
              { LoginButton: false },
              { LogupButton: false },
              { steeingButton: false },
              { HeadIcon: true },
              { LanShareView: true },
              { DirsFileList: true },
              { LogOutButton: true },
            ];
          } else if (
            res.data[1].message == "登录成功" &&
            localStorage.getItem("Authority") == "Admin"
          ) {
            this.state.ButtonAuthority = [
              { LoginButton: false },
              { LogupButton: true },
              { steeingButton: true },
              { HeadIcon: true },
              { LanShareView: true },
              { DirsFileList: true },
              { LogOutButton: true },
            ];
          } else {
            localStorage.removeItem("Authority");
            localStorage.removeItem("Time");
            localStorage.removeItem("UresName");
            this.state.ButtonAuthority = [
              { LoginButton: true },
              { LogupButton: false },
              { steeingButton: false },
              { HeadIcon: false },
              { LanShareView: false },
              { DirsFileList: false },
              { LogOutButton: false },
            ];
          }
          return res.data[1].message;
        })
        .catch((err) => {
          console.log(err);
        });
      return message;
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
