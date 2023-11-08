<template>
    <div>
      <p>{{ myMsg }}</p>
      <p>{{ dynamicProps }}</p>
      <ParentGrandChild 
        :my-msg="myMsg"
        @update-name="updateName"
      />
      <button @click="$emit('someEvent')">클릭</button>
      <button @click="buttonClick">클릭</button>
      <button @click="emitArgs">추가 인자 전달</button>
    </div>
  </template>
  
  <script setup>
    import ParentGrandChild from "@/components/ParentGrandChild.vue"



    // 1. 문자열 배열 선언 방식
    // defineProps(['myMsg'])

    // 2. 객체 선언 방식
    // defineProps({
    //   myMsg: String,
    // })

    // props 데이터를 script 에서 사용하려면
    const props = defineProps({
      myMsg: String,
      dynamicProps: String,
    })
    
    // // 3. 다양한 객체 선언 방식 
    // defineProps({
    //   msMsg: {
    //     type: String,
    //     required: true,
    //   }
    // })

    
    const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

    const buttonClick = function () {
      emit('someEvent')
    }

    const emitArgs = function () {
      emit('emitArgs', 1, 2, 3)
    }


    const updateName = function () {
      emit('updateName')
    }
    console.log(props.myMsg)
  </script>
  
  <style  scoped>
  
  </style>