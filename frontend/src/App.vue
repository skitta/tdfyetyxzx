<script setup lang="ts">
import ExpertsListView from '@views/ExpertsListView.vue'
</script>

<template>
  <n-layout>
    <n-layout-header bordered>
      <n-h4>专家列表</n-h4>
    </n-layout-header>

    <n-layout-content>
      <Suspense><ExpertsListView /></Suspense>
    </n-layout-content>

    <n-layout-footer>
      <n-divider>
        <small style="color: #888888;">南通大学附属医院</small>
      </n-divider>
    </n-layout-footer>
  </n-layout>
</template>

<style scoped>
.n-layout,
.n-layout-header,
.n-layout-content,
.n-layout-footer {
  background: #f1f1f1;
}

.n-layout-header {
  height: 48px;
  padding-top: 12px;
  text-align: center;
  width: 100vw;
  position: fixed;
  top: 0;
  z-index: 10;
}

.n-layout-content {
  margin-top: 48px;
}

.n-layout-footer {
  height: 46px;
  padding: 10px;
}

.n-h4 {
  margin: 0;
}

.n-divider {
  margin: 0;
}
</style>
