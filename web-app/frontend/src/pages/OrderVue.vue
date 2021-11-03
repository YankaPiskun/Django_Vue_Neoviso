<template>
  <div>
    <post-order :orders="orders" @remove="removeOrder" />
  </div>
</template>

<script>
import PostOrder from "@/components/PostOrder.vue";
import axios from "axios";

export default {
  components: { PostOrder },

  data() {
    return {
      orders: [],
    };
  },
  methods: {
    GetOrders() {
      axios
        .get("http://127.0.0.1:8000/orders/")
        .then((response) => (this.orders = response.data))
        .catch((error) => console.log(error));
    },
    removeOrder(order) {
        axios.delete("http://127.0.0.1:8000/orders/" + order.id);
        this.orders = this.orders.filter(o => o.id !== order.id);
    },
  },
  mounted() {
    this.GetOrders();
  },
};
</script>

<style>
</style>
