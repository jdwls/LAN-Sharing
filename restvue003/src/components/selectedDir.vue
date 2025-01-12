<template>
    <div>
        <el-button @click="selectDir">选择根目录</el-button>
    </div>
</template>

<script>
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export default {
    name: 'SelectedDir',
    methods: {
        async selectDir() {
            try {
                const api = this.$store.state.api;
                const response = await axios.post(`${api}/selectedDir`);
                const dirname = response.data.data;

                await this.showConfirmation(dirname);
                if (dirname) {
                    this.$store.state.DirPath = await this.handleDirSelection(dirname, api);
                }
            } catch (error) {
                ElMessage({ type: 'error', message: '出错了: ' + error.message });
            }
        },

        async showConfirmation(dirname) {
            return ElMessageBox.confirm(dirname, '警告', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            });
        },

        async handleDirSelection(dirname, api) {
            try {
                const response = await axios.get(`${api}/SucceedselectedDir`, {
                    params: { dirname }
                });
                const dirPath = response.data.data;
                this.$store.state.DirPath = dirPath;
                console.log("选择的目录路径:", dirPath);
                const dirsFileList = await this.fetchDirsFileList(dirPath, api);
                this.$store.state.DirsFileList = dirsFileList;

                return dirPath;
            } catch (error) {
                ElMessage({ type: 'error', message: '处理目录选择时出错: ' + error.message });
            }
        },

        async fetchDirsFileList(dirPath, api) {
            try {
                const response = await axios.post(`${api}/DirsFileList`, {
                    params: { DirsFileList: dirPath }
                });
                return this.processDirsFileList(response.data.data, api);
            } catch (error) {
                ElMessage({ type: 'error', message: '获取目录文件列表时出错: ' + error.message });
            }
        },

        async processDirsFileList(dirsFileList, api) {
            const updatedList = dirsFileList.map((item, index) => ({
                index,
                data: item,
                FileType: false,
            }));

            try {
                const openDirResponse = await axios.post(`${api}/OpenDir`);
                const folders = Object.values(openDirResponse.data.su);

                updatedList.forEach(dir => {
                    if (folders.includes(dir.data)) {
                        dir.FileType = '文件夹';
                    }
                });

                const fileTypesResponse = await axios.get(`${api}/filesypess`, {
                    params: { filesypessPath: this.$store.state.DirPath }
                });

                const fileTypes = Object.values(fileTypesResponse.data.filesypessPathlistTypes);
                fileTypes.forEach(type => {
                    updatedList[type.index].FileType = type.filesypessPathlistType;
                });

                return updatedList;
            } catch (error) {
                ElMessage({ type: 'error', message: '处理文件类型时出错: ' + error.message });
            }
        }
    }
}
</script>
