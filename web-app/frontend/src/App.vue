<template>
<div>
    <nav-bar></nav-bar>
  <div class="app">
      <div class="main">
      <router-view></router-view>
      </div>
  </div>
  <foot-bar></foot-bar>
  </div>
</template>

<script>
export default {

}
</script>

<style>
   *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    .app{
        
        
    }
    .main{
        min-height: 610px;
    }
    
</style>