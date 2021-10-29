<template>
    <div>
        <h1> Заказ номер {{ $route.params.id}} </h1>
        <put-form></put-form>
        
    </div>
</template>

<script>
import PutForm from '../components/PutForm.vue'
    export default {
  components: { PutForm },
        
    }
</script>

<style scoped>
    h1{
        text-align: center;
    }
</style>