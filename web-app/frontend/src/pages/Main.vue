<template>
  <div class="main">
    <h1 class="main_title">Renovation with love</h1>
    <div class="btn_main">
      <ui-button class="btn" @click="$router.push('/Create')">
        Оформить заказ</ui-button
      >
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.main {
  background-image: url(../static/index.jpg);
  background-size: contain;
  width: 100%;
  height: 850px;
}
.main_title {
  font-family: PlayfairDisplay-Bold;
  font-size: 109px;
  color: black;
  padding-top: 10px;
  text-align: center;
}
.btn_main {
  padding-top: 590px;
  padding-left: 660px;
}
</style>
