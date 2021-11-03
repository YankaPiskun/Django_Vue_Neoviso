<template>
  <div>
    <post-service :services="services" />
  </div>
</template>

<script>
import axios from "axios";
import PostService from "@/components/PostService.vue";

export default {
  components: { PostService },

  data() {
    return {
      services: [],
    };
  },
  methods: {
    GetService() {
      axios
        .get("http://127.0.0.1:8000/service/")
        .then((response) => (this.services = response.data))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    this.GetService();
  },
};
</script>

<style></style>
