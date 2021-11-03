<template>
  <div class="employee">
      <div><strong>Сотрудник номер:</strong> {{ employee.id }}</div>
      <div><strong>Имя: </strong> {{ employee.name }}</div>
      <div><strong>Фамилия: </strong> {{ employee.surname }}</div>
      <div><strong>Отчество: </strong> {{ employee.middlename }}</div>
  </div>
</template>

<script>
export default {
  props: {
    employee: {
      type: Object,
      requered: true,
    },
  },
};
</script>

<style scoped>
.employee {
  clear: both;
  margin: 30px 34%;
  background-color: rgb(240, 234, 234);
  padding-left: 10px;
  text-align: center;
  transition: 1s;
  border-style: solid;
  padding-bottom: 10px;
}

.employee:hover {
  transform: scale(1.2);
  border-radius: 20px;
}
</style>
