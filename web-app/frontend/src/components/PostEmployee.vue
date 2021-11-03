<template>
  <div>
    <div v-if="employees.length > 0">
      <employee-item 
        v-for="employee in employees"
        :key="employee.id"
        :employee="employee"
      />
    </div>
    <h2 v-else style="color: red">
      Сотрудников нет
    </h2>
  </div>
</template>

<script>
import EmployeeItem from './EmployeeItem.vue';
export default {
  components: { EmployeeItem },
  props: {
    employees: {
      type: Array,
      requered: true,
    },
  },
};
</script>

<style scoped>
h2 {
  text-align: center;
  padding-top: 200px;
}
</style>
