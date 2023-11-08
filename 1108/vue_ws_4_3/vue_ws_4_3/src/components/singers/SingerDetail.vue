<template>
    <div class="container">
      <h1>가수 이름</h1>
      <img class="imagestyle" src="@/assets/singer.jpg" alt="singer">
      <p>가수 소개글</p>
    </div>
</template>

<script setup>
 
</script>

<style scoped>
    .container {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid black;
        flex-direction: column;
        padding: 20px;
    }
    .imagestyle {
        margin: 15px;
        width: 200px;
        border-radius: 100px;
    }

</style>
