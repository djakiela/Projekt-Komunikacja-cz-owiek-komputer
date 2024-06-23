<template>
  <div class="home-page">
    <h1>Witamy w Książce Kucharskiej Online</h1>
    <p>
      Znajdź przepisy na każdą okazję. Wybierz kategorię poniżej, aby rozpocząć:
    </p>
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

.home-page h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.home-page p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 20px;
}
</style>
