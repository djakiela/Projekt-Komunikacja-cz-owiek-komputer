<template>
  <div class="recipe-details">
    <h1>{{ recipe.title }}</h1>
    <p>{{ recipe.description }}</p>
    <h3>Składniki</h3>
    <ul>
      <li v-for="(ingredient, index) in recipe.ingredients" :key="index">
        {{ ingredient.name }} - {{ ingredient.quantity }}
      </li>
    </ul>
    <button @click="editRecipe" class="btn btn-primary">Edytuj Przepis</button>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

export default {
  setup() {
    const recipe = ref(null);
    const route = useRoute();
    const router = useRouter();

    const fetchRecipe = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/recipe/${route.params.id}`
        );
        recipe.value = await response.json();
      } catch (error) {
        console.error("Błąd podczas pobierania szczegółów przepisu:", error);
      }
    };

    const editRecipe = () => {
      router.push(`/edit-recipe/${recipe.value.id}`);
    };

    onMounted(fetchRecipe);

    return {
      recipe,
      editRecipe,
    };
  },
};
</script>

<style scoped>
.recipe-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.btn {
  background-color: #3273dc;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn:hover {
  background-color: #275ba8;
}
</style>
