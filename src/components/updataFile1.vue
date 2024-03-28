<<<<<<< HEAD
<template>
    <div>
        <el-upload
    v-model:file-list="fileList"
    :action="$store.state.api+'/uploader'"
    multiple
    
  >
    <el-button type="primary">上传文件夹</el-button>
    <template #tip>
      <div class="el-upload__tip">
      </div>
    </template>
  </el-upload>
    </div>
</template>
<script>
export default{
    name:"updataFile1.vue",
}
=======
<template>
    <div>
        <el-upload
    v-model:file-list="fileList"
    :action="$store.state.api+'/uploader'"
    multiple
    
  >
    <el-button type="primary">上传文件夹</el-button>
    <template #tip>
      <div class="el-upload__tip">
      </div>
    </template>
  </el-upload>
    </div>
</template>
<script>
export default{
    name:"updataFile1.vue",
}
>>>>>>> 87f22de17 (tshi)
</script>