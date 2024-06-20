<template>
  <div class="recipe-list">
    <div class="header">
      <h1>Lista Przepisów</h1>
      <button @click="goBack" class="btn btn-secondary">Powrót</button>
    </div>
    <ul>
      <li v-for="(recipe, index) in recipes" :key="index">
        <span class="recipe-index">{{ index + 1 }}.</span>
        <router-link :to="`/recipe/${recipe.id}`" class="recipe-title">{{
          recipe.title
        }}</router-link>
        <div class="buttons">
          <button
            class="shopping-list-button"
            @click="generateShoppingList(recipe)"
            title="Pobierz listę zakupów"
          >
            <i class="fas fa-list"></i>
          </button>
          <button
            class="delete-button"
            @click="confirmDelete(recipe)"
            title="Usuń przepis"
          >
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted, isProxy, toRaw } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const recipes = ref([]);
    const router = useRouter();

    const fetchRecipes = async () => {
      try {
        const token = localStorage.getItem("token");
        console.log("Fetching recipes with token:", token);
        const response = await fetch("http://localhost:8000/recipe", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });
        recipes.value = await response.json();
        console.log("Fetched recipes:", recipes.value);
      } catch (error) {
        console.error("Błąd podczas pobierania listy przepisów:", error);
      }
    };

    const confirmDelete = async (recipe) => {
      console.log("Recipe before processing:", recipe);
      let rawRecipe = recipe;
      if (isProxy(recipe)) {
        rawRecipe = toRaw(recipe);
        console.log("Recipe was a proxy. Converted to raw:", rawRecipe);
      }
      console.log("Confirming delete for recipe:", rawRecipe);
      if (rawRecipe && rawRecipe.id) {
        await deleteRecipe(rawRecipe.id);
      } else {
        console.error("Invalid recipe:", rawRecipe);
      }
    };

    const deleteRecipe = async (recipeId) => {
      console.log("Deleting recipe with ID:", recipeId);
      try {
        const token = localStorage.getItem("token");
        const response = await fetch(
          `http://localhost:8000/recipe/${recipeId}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );
        if (response.ok) {
          console.log("Recipe deleted successfully");
          recipes.value = recipes.value.filter((r) => r.id !== recipeId);
        } else {
          const errorData = await response.json();
          console.error("Błąd podczas usuwania przepisu:", errorData);
        }
      } catch (error) {
        console.error("Błąd podczas usuwania przepisu:", error);
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
      confirmDelete,
      deleteRecipe,
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
