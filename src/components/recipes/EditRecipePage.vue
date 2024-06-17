<template>
  <div class="edit-recipe">
    <h1>Edytuj Przepis</h1>
    <form @submit.prevent="editRecipe">
      <div class="form-group">
        <label for="title">Tytuł:</label>
        <input type="text" id="title" v-model="title" required />
      </div>
      <div class="form-group">
        <label for="description">Opis:</label>
        <textarea id="description" v-model="description" required></textarea>
      </div>
      <div class="form-group">
        <label>Składniki:</label>
        <div
          v-for="(ingredient, index) in ingredients"
          :key="index"
          class="ingredient"
        >
          <input
            type="text"
            v-model="ingredient.name"
            placeholder="Nazwa"
            required
          />
          <input
            type="text"
            v-model="ingredient.quantity"
            placeholder="Ilość"
            required
          />
        </div>
        <button type="button" @click="addIngredient">Dodaj składnik</button>
      </div>
      <button type="submit" class="btn btn-primary">Zapisz Zmiany</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

export default {
  setup() {
    const title = ref("");
    const description = ref("");
    const ingredients = ref([]);
    const router = useRouter();
    const route = useRoute();

    const fetchRecipe = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/recipe/${route.params.id}`
        );
        const data = await response.json();
        title.value = data.title;
        description.value = data.description;
        ingredients.value = data.ingredients;
      } catch (error) {
        console.error("Błąd podczas pobierania szczegółów przepisu:", error);
      }
    };

    const editRecipe = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/recipe/${route.params.id}`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              title: title.value,
              description: description.value,
              ingredients: ingredients.value,
            }),
          }
        );

        if (response.ok) {
          alert("Zmiany zapisane pomyślnie!");
          router.push("/");
        } else {
          alert("Nie udało się zapisać zmian.");
        }
      } catch (error) {
        console.error("Błąd podczas zapisywania zmian:", error);
        alert("Nie udało się zapisać zmian.");
      }
    };

    const addIngredient = () => {
      ingredients.value.push({ name: "", quantity: "" });
    };

    onMounted(fetchRecipe);

    return {
      title,
      description,
      ingredients,
      addIngredient,
      editRecipe,
    };
  },
};
</script>

<style scoped>
.edit-recipe {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.ingredient {
  display: flex;
  gap: 0.5rem;
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
