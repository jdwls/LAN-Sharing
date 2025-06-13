<template>
    <div>
        <el-form :model="stteing" label-width='6vw' class="forms">
            <el-form-item label="头像更改:">
                <el-upload class="avatar-uploader" 
                    ref="IconUpload"
                    @change=IconUpload()
                    :show-file-list="false" 
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload">
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>

            </el-form-item>
            <el-form-item label="修改密码:">
                <el-input v-model="stteing.ChangePassword"></el-input>
            </el-form-item>
            <el-form-item label="第二次密码">
                <el-input v-model="stteing.TwoChangePassword"></el-input>
            </el-form-item>
            <div class="Authority">
                <el-form-item label="权限选择：">
                    <el-select v-model="stteing.Authority" placeholder="请选择权限" class="AuthorityS">
                        <el-option label="用户" value="Ures"></el-option>
                        <el-option label="管理员" value="Admin"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="选择用户：">
                    <el-select v-model="stteing.AdminAndUresName" placeholder="请选择对应用户的权限" class="AuthorityS">
                        <el-option :label=item :value=item v-for="(item, index) in stteingData.AdminAndUres"
                            :key=index></el-option>
                    </el-select>
                </el-form-item>
            </div>
            <el-form-item label="文件上传的线程:">
                <el-select v-model="stteing.UpadaFileNumbers" placeholder="请选择权限">
                    <el-option :label="item" :value="item" v-for="(item, index) in stteingData.UpadaFileNumbers"
                        :key="index"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即创建</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
export default {
    name: "steeingView",
    data() {
        return {
            stteing: {
                ChangePassword: "",
                TwoChangePassword: "",
                Authority: '',
                AdminAndUresName: '',
                UpadaFileNumbers: ''
            },
            stteingData: {
                AdminAndUres: ['A', 'B', 'C'],
                UpadaFileNumbers: [1, 2, 3, 4, 5]
            },
            imageUrl:''

        }
    },
    methods: {
        onSubmit() {
            console.log(this.stteing.AdminAndUresName);
        },
        handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
        beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isJPG && isLt2M;
      },
      IconUpload(){
        console.log(this.$refs.IconUpload);
        
      }
    }
}
</script>
<style scoped>
.el-form {
    width: 30vw;
}

.forms {
    margin: 0 auto;
}

.Authority {
    display: flex;
    justify-content: space-between
}

.AuthorityS {
    width: 9vw;
}
</style>
<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>