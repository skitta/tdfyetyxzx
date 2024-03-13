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
        const tempResult: majorExperts = {
            major: item.section,
            experts: [{
                name: item.doctor.name,
                avatarSrc: item.doctor.avatar,
                tags: [
                    item.doctor.doctor_title,
                ],
                info: item.info,
                link: item.doctor.link,
            }]
        }
        if (item.doctor.teacher_title) {
                tempResult.experts[0].tags.push(item.doctor.teacher_title)
            }
        if (item.doctor.teacher_office) {
            tempResult.experts[0].tags.push(item.doctor.teacher_office)
        }

        const foundIndex = result.findIndex((resultItem) => resultItem.major === item.section);

        if (foundIndex === -1) {
            result.push(tempResult);
        } else {
            result[foundIndex].experts.push(tempResult.experts[0]);
        }
    });
    console.log(result);
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
