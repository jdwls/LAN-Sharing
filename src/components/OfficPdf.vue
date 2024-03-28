<<<<<<< HEAD
<template>
    <vue-office-pdf 
        :src="pdf()"
       
    />
</template>

<script>
//引入VueOfficePdf组件
import VueOfficePdf from '@vue-office/pdf'
import '@vue-office/excel/lib/index.css'

export default {
    name:'OfficPdf',
    components: {
        VueOfficePdf
    },
    methods: {
        pdf(){
            return this.$store.state.api+'/office?dw='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
        }
    }
}
=======
<template>
    <vue-office-pdf 
        :src="pdf()"
       
    />
</template>

<script>
//引入VueOfficePdf组件
import VueOfficePdf from '@vue-office/pdf'
import '@vue-office/excel/lib/index.css'

export default {
    name:'OfficPdf',
    components: {
        VueOfficePdf
    },
    methods: {
        pdf(){
            return this.$store.state.api+'/office?dw='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
        }
    }
}
>>>>>>> 87f22de17 (tshi)
</script>