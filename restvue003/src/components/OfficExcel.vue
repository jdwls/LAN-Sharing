<template>
    <vue-office-excel
        :src="excel()"
        style="height: 100vh;"
    />
</template>

<script>
//引入VueOfficeExcel组件
import VueOfficeExcel from '@vue-office/excel'
//引入相关样式
import '@vue-office/excel/lib/index.css'

export default {
    name:'OfficExcel',
    components: {
        VueOfficeExcel
    },
    methods: {
        excel(){
            return this.$store.state.api+'/office?dw='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
        }
    }
}
</script>