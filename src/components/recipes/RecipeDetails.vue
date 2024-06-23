<template>
  <div class="recipe-details">
    <div class="header">
      <h1 v-if="recipe">{{ recipe.title }}</h1>
      <div class="buttons">
        <button @click="goBack" class="btn btn-secondary">Powrót</button>
        <button
          @click="confirmDelete"
          class="delete-button"
          title="Usuń przepis"
        >
          <i class="fas fa-trash"></i>
        </button>
      </div>
    </div>
    <div class="description" v-if="recipe">
      <h3>Kroki</h3>
      <ol>
        <li v-for="(step, index) in recipe.steps" :key="index">
          {{ step.description }}
        </li>
      </ol>
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
    <alert-recipe
      v-if="showAlert"
      :message="alertMessage"
      @confirm="deleteRecipe"
      @cancel="showAlert = false"
    />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import AlertRecipe from "../common/AlertRecipe.vue";

export default {
  components: {
    AlertRecipe,
  },
  setup() {
    const recipe = ref(null);
    const error = ref(null);
    const route = useRoute();
    const router = useRouter();
    const store = useStore();
    const recipeId = ref(null);
    const showAlert = ref(false);
    const alertMessage = ref("");

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

    const confirmDelete = () => {
      alertMessage.value = "Czy na pewno usunąć przepis?";
      showAlert.value = true;
    };

    const deleteRecipe = async () => {
      try {
        const token = store.getters.token;
        const response = await fetch(
          `http://localhost:8000/recipe/${recipeId.value}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.ok) {
          router.push("/recipes");
        } else {
          const errorData = await response.json();
          alert(`Nie udało się usunąć przepisu: ${errorData.detail}`);
        }
      } catch (error) {
        console.error("Błąd podczas usuwania przepisu:", error);
        alert("Wystąpił błąd podczas usuwania przepisu.");
      }
    };

    onMounted(fetchRecipe);

    return {
      recipe,
      error,
      editRecipe,
      goBack,
      confirmDelete,
      deleteRecipe,
      showAlert,
      alertMessage,
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

.buttons {
  display: flex;
  gap: 0.5rem;
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

.btn-danger {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-danger:hover {
  background-color: #d32f2f;
}

.delete-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.5rem;
  position: relative;
  color: #000;
}

.delete-button:hover i {
  color: #ff4d4f;
}
</style>
