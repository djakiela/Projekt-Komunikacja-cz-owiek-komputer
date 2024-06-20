<template>
  <div>
    <h1>Test ID Fetching</h1>
    <input v-model="recipeId" placeholder="Enter recipe ID" />
    <button @click="fetchRecipe">Fetch Recipe</button>
    <div v-if="recipe">
      <h2>{{ recipe.title }}</h2>
      <p>{{ recipe.description }}</p>
      <ul>
        <li v-for="(ingredient, index) in recipe.ingredients" :key="index">
          {{ ingredient.name }} - {{ ingredient.quantity }}
        </li>
      </ul>
    </div>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

export default {
  setup() {
    const recipeId = ref("");
    const recipe = ref(null);
    const error = ref(null);
    const store = useStore();

    const fetchRecipe = async () => {
      try {
        const token = store.getters.token;
        console.log("Fetching recipe with ID:", recipeId.value);

        if (!recipeId.value) {
          error.value = "Recipe ID is required";
          return;
        }

        if (!token) {
          error.value = "No token found";
          return;
        }

        const response = await fetch(
          `http://localhost:8000/recipe/test/${recipeId.value}`,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.ok) {
          recipe.value = await response.json();
          error.value = null;
          console.log("Fetched recipe:", recipe.value);
        } else {
          const errorData = await response.json();
          error.value = `Error fetching recipe: ${errorData.detail}`;
          recipe.value = null;
        }
      } catch (err) {
        error.value = `Error fetching recipe: ${err.message}`;
        recipe.value = null;
      }
    };

    return {
      recipeId,
      recipe,
      error,
      fetchRecipe,
    };
  },
};
</script>
