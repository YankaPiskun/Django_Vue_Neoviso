<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "ui-button",
};
</script>

<style scoped>
.btn {
  background-color: white;
  padding: 15px 25px;
  border: 2px solid grey;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-right: 10px;
  transition: 1s;
}
.btn:hover {
  transform: scale(1.2);
  border-radius: 20px;
}
</style>
