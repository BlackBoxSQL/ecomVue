<template>
  <router-view></router-view>
  <h1>Movies</h1>
  <div v-for="movie in movies" v-bind:key="movie.id">
    <p class="text-xl text-primary">{{ movie.title }}</p>
    <img class="poster" :src="movie.poster" />
    <p>{{ dateFormat(movie.release_date) }}</p>
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
        <img class="avatar" :src="actor.profile" />
      </div>
    </div>
    <div class="flex">
      <div class="text-primary text-sm" v-for="director in movie.directors" v-bind:key="director.id">
        <p>&nbsp; &nbsp;{{ director.name }}</p>
      </div>
    </div>
  </div>
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
  name: "Movies",
  data() {
    return {
      movies: [""],
    };
  },
  methods: {
    dateFormat(v) {
      return moment(v).format("DD MMMM, YYYY");
    },
    getMovies() {
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
    this.getMovies();
  },
};
</script>
