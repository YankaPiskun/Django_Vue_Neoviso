<template>
  <div>

      <post-order :orders='orders' @upd='upd' v-if="!isOrderLoading"></post-order>
      <div v-else class="loader">
          Идёт загрузка c сервера...
      </div>

  </div>
</template>

<script>
import PostOrder from '@/components/PostOrder.vue';
import axios from 'axios'


export default {
  components: { PostOrder},
    
    data(){
        return {
            orders: [],
            isOrderLoading:false,
        }

    }, 
    methods: {
        createOrder(order){
          this.orders.push(order)
          
        },
    
        async upd(){
            try{
            this.isOrderLoading = true;
            setTimeout( async ()=>{
                const response = await axios.get('http://127.0.0.1:8000/orders/');
                this.orders = response.data;
                this.isOrderLoading = false
            }, 1000 )
            } catch (e){
                alert('Ошибка')
            }
        },

        
            
    },

    mounted() {
        this.upd()
    },
    
}
</script>

<style>
 .loader{
     font-size: 25px;
     text-align: center;
 }
 
</style>