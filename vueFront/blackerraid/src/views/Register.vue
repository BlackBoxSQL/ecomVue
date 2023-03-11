<template>
  <router-link to="/soon" class="text-primary">soon</router-link><br />
  <router-link to="/movies" class="text-primary">movies</router-link><br />
  <router-link to="/" class="text-primary">home</router-link><br />
  <h1>Register here!</h1>
  <router-view />
</template>
<style>

</style>

<script>
import axios from "axios";
import moment from "moment";
export default {
  data() {
    return {
      inTheaters: [""],
    };
  },
  methods: {
    dateFormat(v) {
      return moment(v).format("Do MMMM, YYYY");
    },
    getInTheater() {
      axios
        .get(`api/v1/in-theater/`)
        .then((response) => {
          console.log(response);
          this.inTheaters = response.data;
        })
        .catch((error) => {
          console.log(JSON.stringify(error));
        });
    },
  },
  created() {
    this.getInTheater();
  },
};
</script>
