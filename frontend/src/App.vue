<script setup lang="ts">
import ExpertsListView from '@/views/ExpertsListView.vue'
</script>

<template>
  <n-layout>
    <n-layout-header bordered>
      <n-h2>儿童医学中心专家组</n-h2>
    </n-layout-header>

    <n-layout-content>
      <ExpertsListView />
    </n-layout-content>

    <n-layout-footer bordered>wei</n-layout-footer>
  </n-layout>
</template>

<style scoped>
.n-layout-header,
.n-layout-content,
.n-layout-footer {
  background: #f1f1f1;
}

.n-layout-header {
  height: 64px;
  padding-top: 20px;
  text-align: center;
  width: 100vw;
  position: fixed;
  top: 0;
  z-index: 10;
}

.n-layout-footer {
  height: 64px;
  padding-top: 12px;
  text-align: center;
}

.n-layout-content {
  margin-top: 64px;
}
</style>
