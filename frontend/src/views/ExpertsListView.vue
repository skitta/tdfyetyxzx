<script setup lang="ts">
import ExpertThing, { Expert } from "@components/ExpertThing.vue"
import imgUrl from "@assets/vue.svg"

const experts: Expert[] = [
    {
        name: '赵建美',
        avatarSrc: imgUrl,
        tags: ['副院长', '主任医师'],
        info: "川崎病、先天性心脏病",
        link: 'http://www.baidu.com'
    },
    {
        name: '赵建美',
        avatarSrc: imgUrl,
        tags: ['副院长', '主任医师'],
        info: "川崎病、先天性心脏病",
        link: 'http://www.baidu.com'
    }
];

const expertGroups = [
    {
        groupName: '儿童心血管',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    },
    {
        groupName: '儿童神经',
        experts: experts
    }
]
</script>

<template> 
    <n-space vertical size="large">
        <n-list bordered v-for="eg in expertGroups">
            <template #header>
                <n-text strong>{{ eg.groupName }}</n-text>
            </template>
            <n-list-item v-for="e in eg.experts">
                <template #suffix>
                    <n-button quaternary type="info">挂号</n-button>
                </template>
                <ExpertThing :expert="e" />
            </n-list-item>
        </n-list>
    </n-space>
</template>

<style scoped>
</style>
