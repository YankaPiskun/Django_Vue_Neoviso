<template>
  <div>
    <div v-if="services.length > 0">
      <service-item 
        v-for="service in services"
        :key="service.id"
        :service="service"
      />
    </div>
    <h2 v-else style="color: red">
      Услуг нет
    </h2>
  </div>
</template>

<script>
import ServiceItem from './ServiceItem.vue';
export default {
  components: { ServiceItem },
  props: {
    services: {
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
