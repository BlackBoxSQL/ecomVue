import { createRouter, createWebHistory } from "vue-router";
import Soon from "../views/Soon.vue";

const routes = [
  {
    path: "/soon",
    name: "Soon",
    component: Soon,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
