<template>
  <div class="service">
      <div><strong>Услуга номер:</strong> {{ service.id }}</div>
      <div><strong>Услуга:</strong> {{ service.turn }}</div>
  </div>
</template>

<script>
export default {
  props: {
    service: {
      type: Object,
      requered: true,
    },
  },
};
</script>

<style scoped>
.service {
  clear: both;
  margin: 30px 34%;
  background-color: rgb(240, 234, 234);
  padding-left: 10px;
  text-align: center;
  transition: 1s;
  border-style: solid;
  padding-bottom: 10px;
}

.service:hover {
  transform: scale(1.2);
  border-radius: 20px;
}
</style>
