<template>
  <div class="home-page">
    <h1>Witamy w Książce Kucharskiej Online</h1>
    <RecipesHome />
  </div>
</template>

<script>
import RecipesHome from "@/components/recipeshome/RecipesHome.vue";

export default {
  name: "HomePage",
  components: {
    RecipesHome,
  },
};
</script>

<style scoped>
.home-page {
  text-align: center;
  padding: 20px;
}
</style>
