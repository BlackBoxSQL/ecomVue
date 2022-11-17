<template>
    <h1>Soon</h1>
    <div v-for="come in coming" v-bind:key="come.id">
      <img class="poster" :src="come.poster" />
    </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
export default {
  name: "Soon",
  data() {
    return {
      coming: [""],
    };
  },
  methods: {
    dateFormat(v) {
      return moment(v).format("Do MMMM, YYYY");
    },
    getComingSoon() {
      axios
        .get(`api/v1/coming-soon/`)
        .then((response) => {
          console.log(response);
          this.coming = response.data;
        })
        .catch((error) => {
          console.log(JSON.stringify(error));
        });
    },
  },
  created() {
    this.getComingSoon();
  },
};
</script>
