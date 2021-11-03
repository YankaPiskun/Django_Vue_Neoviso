<template>
  <div>
    <post-employee :employees="employees"/>
  </div>
</template>

<script>
import axios from "axios";
import PostEmployee from "@/components/PostEmployee.vue";

export default {
  components: { PostEmployee },

  data() {
    return {
      employees: [],
    };
  },
  methods: {
    GetEmployee() {
      axios
        .get("http://127.0.0.1:8000/employee/")
        .then((response) => (this.employees = response.data))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    this.GetEmployee();
  },
};
</script>

<style>
.loader {
  font-size: 25px;
  text-align: center;
}
</style>
