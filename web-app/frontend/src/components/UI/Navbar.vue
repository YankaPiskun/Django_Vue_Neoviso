<template>
  <div class="navbar">
    <div
      class="d-flex flex-column flex-md-row align-items-center p-3 px-md-2 bg-white border-bottom shadow-sm"
      style="width:100%"
    >
      <h5 class="my-0 mr-md-auto font-weight-normal">Пискун компани</h5>
      <nav class="my-2 my-md-0 mr-md-3">
        <router-link class="p-2 text-dark" to="/">Главная</router-link>
        <router-link class="p-2 text-dark" to="/about">О нас</router-link>
        <router-link class="p-2 text-dark" to="/employee"
          >Наши сотрудники</router-link
        >
        <router-link class="p-2 text-dark" to="/service">
          Наши услуги</router-link
        >
        <router-link class="p-2 text-dark" to="/OrderVue"
          >Наши заказы</router-link
        >
        <router-link class="p-2 text-dark" to="/create"
          >Оформить заказ</router-link
        >
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "nav-bar",
};
</script>

<style scoped></style>
