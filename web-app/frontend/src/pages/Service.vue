<template>
    <div class="service">
        <h1 class="top_title">
            Наши Услуги
        </h1>
            <div class="employees_photo">

                <div class="piskun">
                    <img src="../static/Покраска.jpg" alt="">
                        <p>Покраска Автомобиля</p>
                </div>
                <div class="piskun">
                    <img src="../static/Запчасти.jpg" alt="">
                    <p>Замена Запчастей</p>
                </div>
                <div class="piskun">
                    <img src="../static/Починка.jpg" alt="">
                    <p>Починка Запчастей</p>
                </div>
                <div class="piskun">
                    <img src="../static/Осмотр.jpg" alt="">
                    <p>Технический Осмотр</p>
                </div>
                <div class="piskun">
                    <img src="../static/Зеркала.jpg" alt="">
                    <p>Замена Зеркал и Стёкол</p>
                </div>

            </div>
    </div>
</template>

<script>
    export default {
        name:'service'
        
    }
</script>

<style scoped>
.service{
    background-image: url(../static/bg_two.png);
    height: 600px; 
}
.employees_photo{
    display: flex;
    padding-left: 20px;
    padding-top: 40px;
}
.piskun{
    padding-left: 20px;
}
.piskun p{
    padding-top: 20px;
    text-align: center;
    font-size: 20px;
}

.employees_photo img{
    height: 200px;
    width: 230px;
    border-radius:20px;
    transition: 1s;
    margin-left: 40px;
    
}

.employees_photo img:hover{
    transform: scale(1.2);
}
.top_title {
    font-family: PlayfairDisplay-Bold;
    font-size: 109px;
    color: black;
    padding-top: 10px;
    text-align: center; 
}

</style>