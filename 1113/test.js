const sayT1 = () => {
    console.log('T1이 최고야')
}

const sayDongHyeon = () => {
    console.log('징동 DOWN!')
}

// 다른 파일에서 쓰려면 
// export 키워드로 내보내줘야 한다.
// 일반 자바스크립트 파일에서는 다음과 같이 작성해야한다.
module.exports = { sayT1, sayDongHyeon }