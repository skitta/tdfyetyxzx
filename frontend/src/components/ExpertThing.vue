<script setup lang="ts">
export interface Expert {
  avatarSrc: string,
  name: string,
  tags: string[],
  info: string,
  link?: string,
}

defineProps<{
  expert: Expert
}>()
</script>

<template>
  <n-thing>
    <template #avatar>
      <n-avatar v-if="expert.avatarSrc !== null"
        lazy
        :src="expert.avatarSrc"
        size="large"
        fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
      />
      <n-avatar v-else
        lazy
        size="large"
      > {{ expert.name.charAt(0) }} </n-avatar>
    </template>
    <template #header>{{ expert.name }}</template>
    <template #description>
      <n-space size="small">
        <n-tag v-for="t in expert.tags" :bordered="false" type="info" size="small">
          {{ t }}
        </n-tag>
      </n-space>
    </template>
    <n-ellipsis :line-clamp="2" expand-trigger="click" :tooltip="false">
      {{ expert.info }}
    </n-ellipsis>
  </n-thing>
</template>

<style scoped>
.n-avatar {
  height: 56px;
}
</style>
