<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
        <h2>{{ userId }}번 유저의 페이지입니다.</h2>
        <button @click="goHome">홈으로!</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()

const goHome = function () {
    // router.push({ name: 'home' })
    router.replace({ name: 'home'})
}


</script>

<style scoped>

</style>