<template>
  <div class="InputStyle">
    <el-form :model="form" label-width="auto" style="width: 45%">
      <el-form-item label="用户名:">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="密码:">
        <el-input v-model="form.password" show-password></el-input>
      </el-form-item>
      <el-button type="primary" @click="submitForm()">登录</el-button>
    </el-form>
  </div>
</template>

<script>
import { ElMessageBox } from "element-plus";
// import CryptoJS from 'crypto-js';
import axios from "axios";
import { KeyMain } from "@/components/Common/KeyMain.js";
export default {
  name: "LogLn",
  data() {
    return {
      form: {
        name: "",
        password: "",
      },
    };
  },
  methods: {
    submitForm() {
      const UsesCheck = /^[A-Za-z0-9_]{6,12}$/;
      const passwordCheck =
        /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,16}$/;
      if (this.form.name == "" && this.form.password == "") {
        ElMessageBox.alert("用户名和密码不能为空", "为空检测", {
          showConfirmButton: true,
          confirmButtonText: "确认",
        })
          .then(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          })
          .catch(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          });
      }
      if (this.form.name.match(UsesCheck) == null) {
        ElMessageBox.alert(
          "用户名只能包含大小写字母、数字和下划线，且长度在6到12个字符之间",
          "用户名错误",
          {
            showConfirmButton: true,
            confirmButtonText: "确认",
          }
        )
          .then(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          })
          .catch(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          });
      }
      if (this.form.password.match(passwordCheck) == null) {
        ElMessageBox.alert(
          "一个大写字母、一个小写字母、一个数字和一个特殊字符，且长度至少为8个字符",
          "密码错误",
          {
            showConfirmButton: true,
            confirmButtonText: "确认",
          }
        )
          .then(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          })
          .catch(() => {
            this.form.name = "";
            this.form.password = "";
            return 0;
          });
      }
      if (
        this.form.password.match(passwordCheck) != null &&
        this.form.name.match(UsesCheck) != null &&
        this.form.name != "" &&
        this.form.password != ""
      ) {
        axios({
          url: this.$store.state.api + "/login",
          method: "get",
          params: {
            name: this.form.name,
            MD5AESBehind: KeyMain(this.form.password),
            Time: Date.now(),
          },
        }).then((res) => {
         if (res.data.message == "登录成功") {
            ElMessageBox.alert(res.data.message, "登录状态", {
              showConfirmButton: true,
              confirmButtonText: "确认",
            })
              .then(() => {
                this.form.name = "";
                this.form.password = "";
                this.$store.state.dialogVisible= false;
              })
              .catch(() => {
                this.form.name = "";
                this.form.password = "";
                this.$store.state.dialogVisible= false;
              });
          } else {
            ElMessageBox.alert(res.data.message, "登录状态", {
              showConfirmButton: true,
              confirmButtonText: "确认",
            })
              .then(() => {
               return 0;
              })
              .catch(() => {
                return 0;
              });
          }
          })
        .catch((error) => {
          console.error("登录请求失败:", error);
        });
      }
    },
  },
};
</script>
<style scoped>
/* .Uses{
   
} */
span {
  padding-right: 1%;
}
.InputStyle {
  padding-bottom: 2%;
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
