import { createRouter, createWebHistory } from "vue-router";
import Soon from "../views/Soon.vue";
import Movies from "../views/Movies.vue";

const routes = [
  {
    path: "/soon",
    name: "Soon",
    component: Soon,
  },
  {
    path: "/movies",
    name: "Movies",
    component: Movies,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
