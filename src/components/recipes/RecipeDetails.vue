<template>
  <div class="recipe-details">
    <div class="header">
      <h1 v-if="recipe">{{ recipe.title }}</h1>
      <button @click="goBack" class="btn btn-secondary">Powrót</button>
    </div>
    <div class="description" v-if="recipe">
      <p>{{ recipe.description }}</p>
    </div>
    <h3 v-if="recipe">Składniki</h3>
    <ul v-if="recipe" class="ingredients-list">
      <li v-for="(ingredient, index) in recipe.ingredients" :key="index">
        {{ ingredient.name }} - {{ ingredient.quantity }}
      </li>
    </ul>
    <button v-if="recipe" @click="editRecipe" class="btn btn-primary">
      Edytuj Przepis
    </button>
    <p v-else>Ładowanie danych przepisu...</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";

export default {
  setup() {
    const recipe = ref(null);
    const error = ref(null);
    const route = useRoute();
    const router = useRouter();
    const store = useStore();
    const recipeId = ref(null);

    const fetchRecipe = async () => {
      try {
        recipeId.value = route.params.id;
        console.log("Fetching recipe with ID:", recipeId.value);

        const token = store.getters.token;
        console.log("Token from store:", token);

        if (!recipeId.value) {
          error.value = "Recipe ID is required";
          console.error("Recipe ID is required");
          return;
        }

        if (!token) {
          error.value = "No token found in store";
          console.error("No token found in store");
          return;
        }

        const response = await fetch(
          `http://localhost:8000/recipe/${recipeId.value}`,
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
          console.error("Error fetching recipe:", errorData.detail);
        }
      } catch (error) {
        error.value = `Error fetching recipe: ${error.message}`;
        console.error("Błąd podczas pobierania szczegółów przepisu:", error);
      }
    };

    const editRecipe = () => {
      router.push(`/edit-recipe/${recipe.value.id}`);
    };

    const goBack = () => {
      router.push("/recipes");
    };

    onMounted(fetchRecipe);

    return {
      recipe,
      error,
      editRecipe,
      goBack,
    };
  },
};
</script>

<style scoped>
.recipe-details {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.description {
  margin-bottom: 1.5rem;
  font-size: 1.2rem;
}

.ingredients-list {
  list-style-type: none;
  padding: 0;
}

.ingredients-list li {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
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

.btn-secondary {
  background-color: #6c757d;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-secondary:hover {
  background-color: #5a6268;
}

.btn-primary {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  margin-top: 1rem;
}

.btn-primary:hover {
  background-color: #388e3c;
}
</style>
