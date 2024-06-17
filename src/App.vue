<template>
  <div id="app">
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "./components/common/HeaderPage.vue";

export default {
  name: "App",
  components: {
    Header,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.min.css";
@import "@fortawesome/fontawesome-free/css/all.css";
</style>
