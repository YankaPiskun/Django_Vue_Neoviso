<template>
  <div>
      <div class="order" >
         <div>
            <div><strong>Заказ номер:</strong> {{ order.id }}</div>
           <div><strong>Имя клиента: </strong> {{ order.clients_name}}</div>
           <div><strong>Фамилия клиента: </strong> {{ order.clients_surname}}</div>
           <div><strong>Марка авто: </strong> {{ order.car}}</div>
           <div><strong>Сотрудник: </strong> {{ order.employee}}</div>
           <div><strong>Услуга: </strong> {{ order.service}}</div>
         </div>
         <div class="order__btn">
            <ui-button class="btn" @click="deleteOrder">Удалить</ui-button>
            <ui-button class="btn" @click="$router.push(`/OrderVue/${order.id}`)">Редактировать</ui-button>
         </div>
     </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
   props:{
      order:{
         type: Object,
         requered: true,
      }
   },
   methods: {
      deleteOrder(){
         this.$emit('update')
        axios.delete('http://127.0.0.1:8000/orders/' + this.order.id)
        .then((response) => {
         console.log(response)
         },
         (error) => {
         })
         
      },
     
       
   },
}
</script>

<style scoped>

.order {

   clear: both;
    margin: 30px 34%;
    background-color:rgb(240, 234, 234);
    padding-left: 10px;
    text-align: center;
    transition: 1s;
    border-style:solid;
    padding-bottom: 10px;
}

.order:hover{
    transform: scale(1.2);
    border-radius:20px;
    
}
   
</style>