<template>
    <div >
     <div v-if="orders.length > 0" >
      <post-item v-for="order in orders" :key="order.id" :order='order' @update='update'></post-item>
     </div>
    <h2 v-else style="clolr: red">
      Заказов нет, зайдите позжe=)
  </h2>
  </div>
  
</template>

<script>
import PostItem from './PostItem.vue'
export default {
  components: { PostItem },   
    props:{
        orders:{
            type: Array,
            requered: true,
        }
    },
    methods: {
        update() {
            this.$emit('upd')
        }
    },
}

</script>

<style scoped>
h2{
    text-align: center;
    padding-top: 200px;
}
</style>