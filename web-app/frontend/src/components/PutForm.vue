<template>
  <div>
      <div>
          <form @submit.prevent class="form">
              <h1>Редактирование</h1>
              <ui-input v-model="order.clients_name" type="text" placeholder="Введите имя"></ui-input>
              <ui-input v-model="order.clients_surname" type="text" placeholder="Введите фамилию"></ui-input>
              <ui-select v-model.number="order.car" class="input">
                <option disabled value="">Выбирете марку авто</option>
                <option value=1>Audi</option>
                <option value=2>BMW</option>
                <option value=3>Ferrari</option>
                <option value=4>Ford</option>
                <option value=5>Kia</option>
                <option value=6>Volvo</option>
                <option value=7>Tesla</option>
              </ui-select>
              <ui-select v-model.number="order.employee" class="input">
                <option disabled value="">Выберете сотрудника</option>
                <option value=1>Гаврилов</option>
                <option value=2>Пискун</option>
                <option value=3>Белый</option>
                <option value=4>Скурчаев</option>
                <option value=5>Демиденко</option>
              </ui-select>
              <ui-select v-model.number="order.service" class="input">
                <option disabled value="">Выберете услугу</option>
                <option value=1>Покраска</option>
                <option value=4>Технический осмотр</option>
                <option value=3>Починка запчастей</option>
                <option value=2>Замена запчастей</option>
                <option value=5>Замена зеркал и стёкол</option>
              </ui-select>
            <ui-button class="btn" @click="createOrder">Редактировать</ui-button>
            <ui-button class="btn" @click="$router.push('/OrderVue')">Перейти к заказам</ui-button>
          </form>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  
    data(){
        return{
            order: {
                clients_name:'',
                clients_surname: '',
                car:'',
                employee:'',
                service:'',
            }
        }
    },
    methods: {
      createOrder(){
            axios.put('http://127.0.0.1:8000/orders/create/' + this.$route.params.id, {
                clients_name: this.order.clients_name,
                clients_surname: this.order.clients_surname,
                car: this.order.car,
                employee: this.order.employee,
                service: this.order.service
            })
            .then(response => {})
            .catch(error => console.log(error))
            this.order = {
                clients_name:'',
                clients_surname: '',
                car:'',
                employee:'',
                service:'',
            }
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