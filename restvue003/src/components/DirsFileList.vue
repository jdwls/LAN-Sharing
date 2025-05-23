<template>
  <div class="container">
    <div class="table-pagination-wrapper">
      <el-table
        :data="currentPageData"
        style="width: auto"
        border
        max-height="75vh"
        class="centered-table"
      >
        <el-table-column :label="luj">
          <el-table-column>
            <template #header>
              <el-input
                class="header"
                v-model="search"
                placeholder="输入关键字搜索"
                width="300"
              ></el-input>
              <el-button class="search" @click="handleSearch">搜索</el-button>
            </template>
            <el-table-column prop="data" label="文件名" width="360vw" sortable>
            </el-table-column>
            <el-table-column label="下载" width="120vw">
              <template #default="scope">
                <downloadFlie :down="scope.row.data"></downloadFlie>
              </template>
            </el-table-column>
            <el-table-column label="删除" width="120vw">
              <template #default="scope">
                <dropFiles :dropFiles="scope.row.data"> </dropFiles>
              </template>
            </el-table-column>
            <el-table-column label="打开文件" width="120vw">
              <template #default="scope">
                <openDir
                  v-if="scope.row.type == '打开目录'"
                  :openDir="scope.row.data"
                ></openDir>
              </template>
            </el-table-column>
            <el-table-column label="查看文件" width="120vw">
              <template #default="scope">
                <ViewButton
                  v-if="scope.row.type == '查看文件'"
                  :ViewButtonOfficEword="scope.row.data"
                ></ViewButton>
              </template>
            </el-table-column>
          </el-table-column>
        </el-table-column>
      </el-table>
      <el-pagination
        class="centered-pagination"
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage1"
        :page-sizes="[10, 50, 100, 1000]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="filteredData.length"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import downloadFlie from "@/components/downloadFlie.vue";
import dropFiles from "@/components/dropFiles.vue";
import openDir from "@/components/openDir.vue";
import ViewButton from "@/components/ViewButton.vue";

export default {
  name: "DirsFileList",
  data() {
    return {
      currentPage1: 1,
      pageSize: 10,
      search: "",
      appliedSearch: "", // 新增的搜索状态
    };
  },
  components: {
    downloadFlie,
    dropFiles,
    openDir,
    ViewButton,
  },
  computed: {
    // 过滤后的数据
    filteredData() {
      const keyword = this.appliedSearch.toLowerCase();
      if (!keyword) return this.$store.state.DirsFileList;

      return this.$store.state.DirsFileList.filter((item) =>
        item.data.toLowerCase().includes(keyword)
      );
    },
    // 当前页数据
    currentPageData() {
      const start = (this.currentPage1 - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.filteredData.slice(start, end);
    },
    luj() {
      return `路径：（${this.$store.state.DirPath}）`;
    },
  },
  mounted() {
    this.$store.dispatch("DirsFileList");
    this.$store.dispatch("openDirs");
  },
  methods: {
    handleSizeChange(val) {
      this.pageSize = val;
      this.currentPage1 = 1; // 重置到第一页
    },
    handleCurrentChange(val) {
      this.currentPage1 = val;
    },
    handleSearch() {
      this.appliedSearch = this.search; // 应用搜索条件
      this.currentPage1 = 1; // 重置到第一页
    },
  },
};
</script>

<style scoped>
/* 保持原有样式不变 */
.container {
  display: flex;
  justify-content: center;
}

.table-pagination-wrapper {
  width: 100%;
  max-width: 1200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.centered-table {
  margin: 0 auto;
  width: auto !important;
  transition: all 0.3s ease;
}

.centered-pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  width: 100%;
}

@media (max-width: 768px) {
  .container {
    padding: 10px;
  }

  .centered-table {
    width: 100% !important;
  }

  .centered-pagination ::v-deep .el-pagination__jump {
    display: none !important;
  }
}

.header {
  width: 50%;
}

.search {
  margin-left: 1%;
}
</style>
