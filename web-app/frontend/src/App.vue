<template>
  <div>
    <nav-bar />
    <div>
      <div class="main">
        <router-view />
      </div>
    </div>
    <foot-bar />
  </div>
</template>

<script>
export default {};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.main {
  min-height: 610px;
}
</style>
