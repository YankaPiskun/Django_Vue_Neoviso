<template>
  <div class="order">
    <div>
      <div><strong>Заказ номер:</strong> {{ order.id }}</div>
      <div><strong>Имя клиента: </strong> {{ order.clients_name }}</div>
      <div><strong>Фамилия клиента: </strong> {{ order.clients_surname }}</div>
      <div><strong>Марка авто: </strong> {{ order.car }}</div>
      <div><strong>Сотрудник: </strong> {{ order.employee }}</div>
      <div><strong>Услуга: </strong> {{ order.service }}</div>
    </div>
    <div class="order__btn">
      <ui-button class="btn" @click="$emit('remove', order)">Удалить</ui-button>
      <ui-button class="btn" @click="$router.push(`/OrderVue/${order.id}`)"
        >Редактировать</ui-button
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    order: {
      type: Object,
      requered: true,
    },
  },
};
</script>

<style scoped>
.order {
  clear: both;
  margin: 30px 34%;
  background-color: rgb(240, 234, 234);
  padding-left: 10px;
  text-align: center;
  transition: 1s;
  border-style: solid;
  padding-bottom: 10px;
}

.order:hover {
  transform: scale(1.2);
  border-radius: 20px;
}
</style>
