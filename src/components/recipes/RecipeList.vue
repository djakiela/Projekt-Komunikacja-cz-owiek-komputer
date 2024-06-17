<template>
  <div class="recipe-list">
    <h1>Lista Przepisów</h1>
    <ul>
      <li v-for="(recipe, index) in recipes" :key="index">
        <router-link :to="`/recipe/${recipe.id}`">{{
          recipe.title
        }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const recipes = ref([]);

    const fetchRecipes = async () => {
      try {
        const response = await fetch("http://localhost:8000/recipe");
        recipes.value = await response.json();
      } catch (error) {
        console.error("Błąd podczas pobierania listy przepisów:", error);
      }
    };

    onMounted(fetchRecipes);

    return {
      recipes,
    };
  },
};
</script>

<style scoped>
.recipe-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 0.5rem;
}

a {
  color: #3273dc;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
