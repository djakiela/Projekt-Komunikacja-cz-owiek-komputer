<template>
  <div id="app">
    <Header />
    <router-view />
    <TestDeletePage />
    <TestIDComponent />
  </div>
</template>

<script>
import Header from "./components/common/HeaderPage.vue";
//import TestDeletePage from "./components/Test/TestDeletePage.vue";
//import TestIDComponent from "./components/Test/TestIDComponent.vue";

export default {
  name: "App",
  components: {
    Header,
    //TestDeletePage,
    //TestIDComponent,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.min.css";
@import "@fortawesome/fontawesome-free/css/all.css";
</style>
