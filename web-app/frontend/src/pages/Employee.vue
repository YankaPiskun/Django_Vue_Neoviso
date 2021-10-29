<template>
    <div class="employee">
        <h1 class="top_title">
            Наши сотрудники
        </h1>
            <div class="employees_photo">
                
                <div class="piskun">
                    <img src="../static/Пискун.jpg" alt="">
                        <p>Пискун Ян <br> Александрович</p>
                </div>
                <div class="piskun">
                    <img src="../static/Демиденко.jpg" alt="">
                    <p>Демиденко Валерий <br> Олегович</p>
                </div>
                <div class="piskun">
                    <img src="../static/Гаврилов.jpg" alt="">
                    <p>Гаврилов Иван <br> Александрович</p>
                </div>
                <div class="piskun">
                    <img src="../static/Белый.jpg" alt="">
                    <p>Белый Кирилл <br> Александрович</p>
                </div>
                <div class="piskun">
                    <img src="../static/Скурчаев.jpg" alt="">
                    <p>Скурчаев Егор <br> Олегович</p>
                </div>
                
            </div>
    </div>
</template>

<script>
    export default {
        name:'employee'
    }
</script>

<style scoped>
.employee{
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