<template>
    <h1>Movies</h1>
    <div v-for="movie in movies" v-bind:key="movie.id" >
      <p class="text-xl text-primary">{{ movie.name }}</p>
      <img class="poster" :src="movie.poster" />
      <p>{{ dateFormat(movie.release) }}</p>
      <p>duration: {{ movie.duration }}</p>
      <div class="flex">
        <div class="text-primary text-sm" v-for="genre in movie.genres" v-bind:key="genre.id">
          <p>&nbsp; &nbsp;{{ genre.name }}</p>
        </div>
      </div>
      <div class="flex">
        <div class="text-primary text-sm" v-for="actor in movie.actors" v-bind:key="actor.id">
          <p>&nbsp; &nbsp;{{ actor.name }}</p>
        </div>
        <div class="text-primary" v-for="actor in movie.actors" v-bind:key="actor.id">
          <img class="avatar" :src="actor.profile_image" />
        </div>
      </div>
      <div class="flex">
        <div class="text-primary text-sm" v-for="direct in movie.director" v-bind:key="direct.id">
          <p>&nbsp; &nbsp;{{ direct.name }}</p>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
export default {
  name: "Movies",
  data() {
    return {
      movies: [""],
    };
  },
  methods: {
    dateFormat(v) {
      return moment(v).format("Do MMMM, YYYY");
    },
    getData() {
      axios
        .get(`api/v1/movies/`)
        .then((response) => {
          console.log(response);
          this.movies = response.data;
        })
        .catch((error) => {
          console.log(JSON.stringify(error));
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>
