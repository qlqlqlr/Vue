<template>
    <div class="header">
        <h1>랜덤한 강아지</h1>
        <button @click="getRandomDogData" class="custom-button">새로운 강아지 가져오기</button>
        
    </div>

    <div v-if="dogIsEmpty" class="dog-container">
        <div v-for="dog in dogs" :key='dog.id' class="dog-box">
            <img :src="dog.url" alt="" class="dog-box img">
            <div v-if="dog.detail" class="dog-info">
                <p><strong>이름 :</strong> {{ dog.detail.name }}</p>
                <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
                <p><strong>높이:</strong> {{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
                <p><strong>수명:</strong> {{ dog.detail.life_span }}</p>
                <p><strong>성격:</strong> {{ dog.detail.temperament }}</p>
                <p><strong>무게:</strong> {{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
            </div>
        </div>
    </div>

    <div v-else>
        아직 데이터를 받아오지 않았따 
    </div>


</template>
    
<script setup>
    import { computed } from 'vue'

    const emit = defineEmits(['getDogData'])

    const getRandomDogData = () => {
        emit('getDogData')
    }

    const props = defineProps({
        dogs: Array
    })

    const dogIsEmpty = computed(() => {
        return props.dogs.length > 0 ? true : false
    })

</script>

<style scoped>
    .header {
        display: flex;
        justify-content: space-between;
    }

    .custom-button {
        background-color: darkolivegreen;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .custom-button:hover {
        background-color: darkkhaki;
    }

    .dog-container {
        background-color: darkolivegreen;
        border: 1px solid black;
    }

    .dog-box {
        background-color: darkkhaki;
        border: 1px solid black;
        border-radius: 10px;
        margin: 10px;
        display: flex;
    }

    .dog-box img {
        margin-top: 25px;
        width: 200px;
        height: 200px;
        object-fit: fill;
        border-radius: 10px;
    }
    .dog-info {
        margin: 10px;
        margin-left: 10px;
        padding: 10px;
        background-color: lightgoldenrodyellow; /* 배경색을 회색 계통으로 설정합니다. */
        border: 1px solid #ccc; /* 테두리 추가 */
        border-radius: 5px;
    }

   
</style>