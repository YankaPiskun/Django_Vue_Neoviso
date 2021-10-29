<template>
  <select :value='modelValue' @input="updateSelect"><slot></slot></select>
</template>

<script>
export default {
    name: 'ui-select',
    props: { 
      modelValue:[String, Number]
    },
    methods: {
        updateSelect(){
            this.$emit('update:modelValue', event.target.value)
        }
        
    },
}
</script>

<style scope>
.input{
      width: 100%;
      border: 1px solid grey;
      padding: 10px 15px;
      margin-top: 15px;
}
</style>