<template>
    <div class="create">
        <post-form @upd='upd'></post-form>
    </div>
</template>

<script>
import PostForm from '@/components/PostForm.vue';
    export default {
        components: { PostForm },
        
    }
</script>

<style scoped>
    .create{
        display: flex;
    }
</style>