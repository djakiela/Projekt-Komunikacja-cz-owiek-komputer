<template>
  <div class="recipe-list">
    <div class="header">
      <h1>Lista Przepisów - Śniadanie</h1>
      <button @click="goBack" class="btn btn-secondary">Powrót</button>
    </div>
    <ul>
      <li v-for="(recipe, index) in recipes" :key="index">
        <span class="recipe-index">{{ index + 1 }}.</span>
        <router-link :to="`/recipe/${recipe.id}`" class="recipe-title">
          {{ recipe.title }}
        </router-link>
        <div class="buttons">
          <button
            class="shopping-list-button"
            @click="generateShoppingList(recipe)"
            title="Pobierz listę zakupów"
          >
            <i class="fas fa-list"></i>
          </button>
        </div>
      </li>
    </ul>
    <AlertRecipe
      v-if="showAlert"
      :message="alertMessage"
      @confirm="deleteRecipe"
      @cancel="showAlert = false"
    />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import AlertRecipe from "../common/AlertRecipe.vue";

export default {
  components: {
    AlertRecipe,
  },
  setup() {
    const recipes = ref([]);
    const router = useRouter();
    const showAlert = ref(false);
    const alertMessage = ref("");
    const actionToConfirm = ref(null);

    const fetchRecipes = async () => {
      try {
        const recipeIds = [1, 2];
        const fetchedRecipes = [];

        for (const id of recipeIds) {
          const token = localStorage.getItem("token");
          const response = await fetch(`http://localhost:8000/recipe/${id}`, {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          });

          if (response.ok) {
            const recipe = await response.json();
            fetchedRecipes.push(recipe);
          } else {
            console.error(`Failed to fetch recipe with ID: ${id}`);
          }
        }

        recipes.value = fetchedRecipes;
      } catch (error) {
        console.error("Error fetching recipes:", error);
      }
    };

    const generateShoppingList = (recipe) => {
      const ingredients = recipe.ingredients
        .map(
          (ingredient, index) =>
            `${index + 1}. ${ingredient.name}: ${ingredient.quantity}`
        )
        .join("\n");
      const blob = new Blob([ingredients], {
        type: "text/plain;charset=utf-8",
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `${recipe.title}.txt`;
      a.click();
      URL.revokeObjectURL(url);
    };

    const goBack = () => {
      router.push("/");
    };

    onMounted(fetchRecipes);

    return {
      recipes,
      showAlert,
      alertMessage,
      actionToConfirm,
      generateShoppingList,
      goBack,
    };
  },
};
</script>

<style scoped>
.recipe-list {
  max-width: 800px;
  margin: 0 auto;
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

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #4caf50;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.recipe-index {
  font-weight: bold;
  margin-right: 1rem;
  color: #4caf50;
}

.recipe-title {
  flex-grow: 1;
  color: #000;
  text-decoration: none;
  font-size: 1.25rem;
}

.recipe-title:hover {
  text-decoration: underline;
}

.buttons {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.shopping-list-button,
.delete-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.5rem;
  position: relative;
}

.shopping-list-button:hover i,
.delete-button:hover i {
  color: #ffeb3b;
}

.delete-button i {
  color: #ff4d4f;
}
</style>
