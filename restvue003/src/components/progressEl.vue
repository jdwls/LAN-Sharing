<<<<<<< HEAD
<template>
    <div v-for="i in $store.state.files " :key="i.id">
    <span>文件名字：{{i.name}}</span>
    <span> 文件大小{{SuLvZhuangHuang(i.size)}} </span>
    <span>速度:{{ SuLvZhuangHuang(i.speed) }}</span>

    <el-progress :percentage="Number(i.progress)"  :text-inside="true" :stroke-width="18"></el-progress> 
    </div>
</template>

<script>


export default{
    name:"progressEl",
    data() {
        return {
            size:""
        }
    },
    computed:{
       
    },
    methods:{
        SuLvZhuangHuang(i){
    if (i < 1024) {
return i.toFixed(2) + ' B/s';
} else if (i < 1024 * 1024) {
return (i / 1024).toFixed(2) + ' KB/s';
} else if (i < 1024 * 1024 * 1024) {
return (i / (1024 * 1024)).toFixed(2) + ' MB/s';
} else {
return (i / (1024 * 1024 * 1024)).toFixed(2) + ' GB/s';
}
}
        
    //     Size(size) {
    //      return size
    // },
  
    }

}
=======
<template>
    <div v-for="i in $store.state.files " :key="i.id">
    <span>文件名字：{{i.name}}</span>
    <span> 文件大小{{SuLvZhuangHuang(i.size)}} </span>
    <span>速度:{{ SuLvZhuangHuang(i.speed) }}</span>

    <el-progress :percentage="Number(i.progress)"  :text-inside="true" :stroke-width="18"></el-progress> 
    </div>
</template>

<script>


export default{
    name:"progressEl",
    data() {
        return {
            size:""
        }
    },
    computed:{
       
    },
    methods:{
        SuLvZhuangHuang(i){
    if (i < 1024) {
return i.toFixed(2) + ' B/s';
} else if (i < 1024 * 1024) {
return (i / 1024).toFixed(2) + ' KB/s';
} else if (i < 1024 * 1024 * 1024) {
return (i / (1024 * 1024)).toFixed(2) + ' MB/s';
} else {
return (i / (1024 * 1024 * 1024)).toFixed(2) + ' GB/s';
}
}
        
    //     Size(size) {
    //      return size
    // },
  
    }

}
>>>>>>> 87f22de17 (tshi)
</script>