<template>
    <div>
        <vue-office-docx
        :src="docx()"
        @rendered="rendered"
        
    />
    </div>
</template>
<script>
import VueOfficeDocx from '@vue-office/docx'
import '@vue-office/docx/lib/index.css'
export default{
    name:'OfficEword',
    components: {
        VueOfficeDocx
  },
  data(){
    return{
    }
  },
  methods:{
    rendered(){
        console.log("渲染完成");
    },
    docx(){
        return this.$store.state.api+'/office?dw='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
    },
    
   
  }
}
</script>