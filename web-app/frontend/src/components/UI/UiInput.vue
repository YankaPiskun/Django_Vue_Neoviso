<template>
    <input :value="modelValue" @input="updateInput" type="text" class="input">
</template>

<script>
export default {
    name: 'ui-input',
    props: {
        modelValue: [String, Number]
    },
    methods: {
        updateInput(){
            this.$emit('update:modelValue', event.target.value)
        }
        
    },
}
</script>

<style>
.input{
        width: 100%;
        
        padding: 10px 15px;
        margin-top: 15px;
        transition: 1s;
}
.input:hover{
    transform: scale(1.1);
    border-radius:20px;
}
</style>