<template>
  <select v-model="modelValue" @change="changeOption">
    <option disabled value=""> Выбирете из списка</option>
    <option v-for="option in options" :key="option.value" :value="option.value">
      {{ option.name }}
    </option>
  </select>
</template>

<script>
export default {
  name: "ui-select",
  props: {
    modelValue: {
      type: String
    },
    options: {
      type: Array,
      default: () => [],
    },
  },

  methods: {
    changeOption(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style scope>
.input {
  width: 100%;
  border: 1px solid grey;
  padding: 10px 15px;
  margin-top: 15px;
}
</style>
