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
      <n-avatar :src="expert.avatarSrc" size="large" />
    </template>
    <template #header>{{ expert.name }}</template>
    <template #description>
      <n-space size="small">
        <n-tag v-for="t in expert.tags" :bordered="false" type="info" size="small">
          {{ t }}
        </n-tag>
      </n-space>
    </template>
    {{ expert.info }}
  </n-thing>
</template>
