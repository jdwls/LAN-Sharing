<template>
    <div>
        <el-button 
            :disabled="isDisabled" 
            @click="topleveldirectory" 
            class="tets">
            返回上级目录
            <span v-if="countdown > 0">({{ countdown }}s)</span>
        </el-button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            isDisabled: false,
            countdown: 0,
            timer: null
        };
    },
    methods: {
        async topleveldirectory() {
            if (this.isDisabled) return;
            // 立即禁用按钮
            this.startCountdown();
            
            try {
                await this.TopLevelDirectory();
            } catch (error) {
                console.error('操作失败:', error);
            }
        },

        async TopLevelDirectory() {
            console.log(this.$store.state.DirPath);
            try {
                const res = await axios.get(this.$store.state.api + '/TopLevelDirectory', 
                {
                    params: { 
                        TopLevelDirectoryPathName: this.$store.state.DirPath 
                    }
                });
                
                if(res.data.type === '成功') {
                    this.$store.state.DirPath = res.data.data;
                    await Promise.all([
                        this.$store.dispatch('DirsFileList'),
                        this.$store.dispatch('openDirs'),
                        // this.$store.dispatch('filesypess')
                    ]);
                }
            } catch (error) {
                console.error('目录操作失败:', error);
            }
        },

        // async getDirs() {
        //     const res = await axios.get(this.$store.state.api + '/getDirs');
        //     return res.data.data;
        // },

        startCountdown() {
            this.isDisabled = true;
            this.countdown = 5;
            
            this.timer = setInterval(() => {
                this.countdown--;
                
                if (this.countdown <= 0) {
                    clearInterval(this.timer);
                    this.isDisabled = false;
                }
            }, 1000);
        }
    },
    beforeUnmount() {
        if (this.timer) {
            clearInterval(this.timer);
        }
    }
};
</script>

<style scoped>
/* 禁用状态样式 */
.el-button.is-disabled {
    cursor: not-allowed;
    opacity: 0.7;
}
</style>