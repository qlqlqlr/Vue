<template>
    <div class="container">
        <h1>가수 목록</h1>
      <SingerDetail />
    </div>
</template>

<script setup>
  import SingerDetail from './singers/SingerDetail.vue'
</script>

<style scoped>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        
    }
    .imagestyle {
        width: 200px;
    }

</style>
