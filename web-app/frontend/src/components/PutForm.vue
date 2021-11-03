<template>
  <div class="block_form">
    <form @submit.prevent class="form">
      <h1>Редактирование заказа</h1>
      <ui-input
        v-model="order.clients_name"
        type="text"
        placeholder="Введите имя"
      ></ui-input>
      <ui-input
        v-model="order.clients_surname"
        type="text"
        placeholder="Введите фамилию"
      ></ui-input>
      <ui-select
        v-model="order.car"
        :options="selectCar" 
        class="input" 
      />
      <ui-select
        v-model="order.employee"
        :options="selectEmployee"
        class="input"
      />
      <ui-select
        v-model="order.service"
        :options="selectService"
        class="input"
      />
      <ui-button class="btn" @click="createOrder">Создать</ui-button>
      <ui-button class="btn" @click="$router.push('/OrderVue')"
        >Перейти к заказам</ui-button
      >
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      order: {
        clients_name: "",
        clients_surname: "",
        car: "",
        employee: "",
        service: "",
      },
      selectCar: [
        { value: 1, name: "Audi" },
        { value: 2, name: "BMW" },
        { value: 3, name: "Ferrari" },
        { value: 4, name: "Ford" },
        { value: 5, name: "Kia" },
        { value: 6, name: "Volvo" },
        { value: 7, name: "Tesla" },
      ],
      selectEmployee: [
        { value: 1, name: "Гаврилов" },
        { value: 2, name: "Пискун" },
        { value: 3, name: "Белый" },
        { value: 4, name: "Скурчаев" },
        { value: 5, name: "Демиденко" },
      ],
      selectService: [
        { value: 1, name: "Покраска" },
        { value: 2, name: "Замена запчастей" },
        { value: 3, name: "Починка запчастей" },
        { value: 4, name: "Технический осмотр" },
        { value: 5, name: "Замена зеркал и стёкол" },
      ],
    };
  },
    methods: {
      createOrder(){
            axios.put('http://127.0.0.1:8000/create/' + this.$route.params.id + '/', {
                clients_name: this.order.clients_name,
                clients_surname: this.order.clients_surname,
                car: this.order.car,
                employee: this.order.employee,
                service: this.order.service
            })
            .then(response => {
                this.order = {
                clients_name:'',
                clients_surname: '',
                car:'',
                employee:'',
                service:'',
            }})
            .catch(error => console.log(error))
      }
    },

}
</script>

<style scoped>
     .form{
      width: 500px;
      margin-left: 530px;
      margin-top: 60px;
    }
</style>