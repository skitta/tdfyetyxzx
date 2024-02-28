<script setup lang="ts">
import ExpertThing, { Expert } from "@components/ExpertThing.vue";
//import imgUrl from "@assets/vue.svg";
import { getExperts } from "@api/experts";
import { computed } from "vue";

interface majorExperts {
    major: string,
    experts: Expert[]
}

const expertsdb = await getExperts();

const getMajorExperts = computed<majorExperts[]>(() => {
    const result: majorExperts[] = [];
    expertsdb.forEach((item) => {
        item.major.forEach((majorItem) => {
            const tempResult: majorExperts = {
                major: majorItem,
                experts: [{
                    name: item.name,
                    avatarSrc: item.avatar,
                    tags: [
                        item.doctor_title,
                        //item.doctor_office,
                        item.degree,
                        item.teacher_title,
                        //item.teacher_office
                    ],
                    info: `擅长诊治儿童${item.field}`,
                    link: item.link
                }]
            }
            const foundIndex = result.findIndex((resultItem) => resultItem.major === majorItem);

            if (foundIndex === -1) {
                result.push(tempResult)
            } else {
                result[foundIndex].experts.push(tempResult.experts[0])
            }
        });
    });
    return result;
});

</script>

<template>
    <n-space vertical size="large">
        <n-list bordered v-for="eg in getMajorExperts">
            <template #header>
                <n-text strong>{{ eg.major }}</n-text>
            </template>
            <n-list-item v-for="e in eg.experts">
                <template #suffix>
                    <n-button
                        quaternary
                        type="info"
                        tag="a"
                        :href="e.link"
                    >挂号</n-button>
                </template>
                <ExpertThing :expert="e" />
            </n-list-item>
        </n-list>
    </n-space>
</template>

<style scoped>
</style>
