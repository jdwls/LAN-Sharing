<<<<<<< HEAD
<template>
    <div>
       <el-image :src="imageSeesrc()" 
       @load="tess(e)"></el-image>
    </div>
</template>

<script>
export default{
    name:"imageSee",
    methods:{
        imageSeesrc(){
            return this.$store.state.api+'/imageSee?imageSeeName='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
        },
        tess(e){
            console.log(e);
        }
    }
}
=======
<template>
    <div>
       <el-image :src="imageSeesrc()" 
       @load="tess(e)"></el-image>
    </div>
</template>

<script>
export default{
    name:"imageSee",
    methods:{
        imageSeesrc(){
            return this.$store.state.api+'/imageSee?imageSeeName='+this.$store.state.DirPath+'/'+this.$store.state.OfficEword
        },
        tess(e){
            console.log(e);
        }
    }
}
>>>>>>> 87f22de17 (tshi)
</script>