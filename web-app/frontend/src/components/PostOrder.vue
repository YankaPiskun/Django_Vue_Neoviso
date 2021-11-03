<template>
  <div>
    <div v-if="orders.length > 0">
      <post-item
        v-for="order in orders"
        :order="order"
        :key="order.id"
        @remove="$emit('remove', order)"
      />
    </div>
    <h2 v-else style="color: red">
      Заказов нет, зайдите позжe=)
    </h2>
  </div>
</template>

<script>
import PostItem from "./PostItem.vue";
export default {
  components: { PostItem },
  props: {
    orders: {
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
