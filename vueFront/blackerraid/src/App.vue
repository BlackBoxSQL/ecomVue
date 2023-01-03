<template>
  <router-link to="/soon" class="text-primary">soon</router-link><br />
  <router-link to="/movies" class="text-primary">movies</router-link><br />
  <router-link to="/" class="text-primary">home</router-link><br />
  <h1>inTheater</h1>
  <div v-for="inTheater in inTheaters" :key="inTheater.id">
    <p>movie name: {{ inTheater.name.name }}</p>
    <p>hall location: {{ inTheater.theater.location.name }}</p>
    <p>hall name: {{ inTheater.theater.name }}</p>
    <p>show date: {{ dateFormat(inTheater.show_date) }}</p>
    <p>time: {{ inTheater.show_time }}</p>
  </div>
  <router-view />
</template>

<style>
.poster {
  width: 129px;
  height: 172px;
  border-radius: 15px;
  margin-left: 8px;
  margin-bottom: 8px;
}
.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.ninja {
  display: flex;
}
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
