<template>
    <div class="user-selection-container">
        <div class="user-selection-content">
            <!-- <v-icon large color="grey lighten-1" class="mb-4">mdi-account-multiple</v-icon> -->
            <h2 class="headline grey--text text--lighten-1">请在左侧选择用户</h2>
            <p class="subtitle-1 grey--text text--lighten-2 mt-2">或创建新的对话</p>
        </div>
    </div>
</template>
<style scoped>
.user-selection-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    background-color: #f5f5f5;
    font-size: 2vw;
}

.user-selection-content {
    text-align: center;
    max-width: 120vw;
    padding: 8vw;
}
</style>
