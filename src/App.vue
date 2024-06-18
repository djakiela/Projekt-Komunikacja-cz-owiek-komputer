<template>
  <div id="app">
    <Header />
    <router-view />
    <TestDeletePage />
  </div>
</template>

<script>
import Header from "./components/common/HeaderPage.vue";
//import TestDeletePage from "./components/Test/TestDeletePage.vue";

export default {
  name: "App",
  components: {
    Header,
    //TestDeletePage,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.min.css";
@import "@fortawesome/fontawesome-free/css/all.css";
</style>
