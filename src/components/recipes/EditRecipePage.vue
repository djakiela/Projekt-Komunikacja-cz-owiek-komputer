<template>
  <div class="edit-recipe">
    <div class="header">
      <h1>Edytuj Przepis</h1>
      <button @click="goBack" class="btn btn-secondary">Powrót</button>
    </div>
    <form @submit.prevent="editRecipe">
      <div class="form-group">
        <label for="title">Tytuł:</label>
        <input type="text" id="title" v-model="title" required />
      </div>
      <div class="form-group">
        <label>Składniki:</label>
        <div
          v-for="(ingredient, index) in ingredients"
          :key="index"
          class="ingredient-item"
        >
          <input
            type="text"
            v-model="ingredient.name"
            placeholder="Nazwa składnika"
            required
          />
          <input
            type="text"
            v-model="ingredient.quantity"
            placeholder="Ilość"
            required
          />
          <button
            type="button"
            class="btn btn-success btn-small"
            @click="addIngredient"
          >
            Dodaj składnik
          </button>
          <button
            type="button"
            v-if="ingredients.length > 1"
            class="btn btn-danger btn-small"
            @click="removeIngredient(index)"
          >
            Usuń
          </button>
        </div>
      </div>
      <div class="form-group">
        <label>Kroki:</label>
        <div v-for="(step, index) in steps" :key="index" class="step-item">
          <textarea
            v-model="step.description"
            @input="adjustTextareaHeight($event)"
            placeholder="Opis kroku"
            required
          ></textarea>
          <button
            type="button"
            class="btn btn-success btn-small"
            @click="addStep"
          >
            Dodaj krok
          </button>
          <button
            type="button"
            v-if="steps.length > 1"
            class="btn btn-danger btn-small"
            @click="removeStep(index)"
          >
            Usuń
          </button>
        </div>
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
    const ingredients = ref([{ name: "", quantity: "" }]);
    const steps = ref([{ description: "" }]);
    const router = useRouter();
    const route = useRoute();

    const fetchRecipe = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch(
          `http://localhost:8000/recipe/${route.params.id}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        const data = await response.json();
        title.value = data.title;
        description.value = data.description;
        ingredients.value = data.ingredients;
        steps.value = data.steps;
      } catch (error) {
        console.error("Błąd podczas pobierania szczegółów przepisu:", error);
      }
    };

    const addIngredient = () => {
      ingredients.value.push({ name: "", quantity: "" });
    };

    const removeIngredient = (index) => {
      if (ingredients.value.length > 1) {
        ingredients.value.splice(index, 1);
      }
    };

    const addStep = () => {
      steps.value.push({ description: "" });
    };

    const removeStep = (index) => {
      if (steps.value.length > 1) {
        steps.value.splice(index, 1);
      }
    };

    const editRecipe = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch(
          `http://localhost:8000/recipe/${route.params.id}`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({
              title: title.value,
              description: description.value,
              ingredients: ingredients.value,
              steps: steps.value,
            }),
          }
        );

        if (response.ok) {
          router.push("/recipes");
        } else {
          alert("Nie udało się zapisać zmian.");
        }
      } catch (error) {
        console.error("Błąd podczas zapisywania zmian:", error);
        alert("Nie udało się zapisać zmian.");
      }
    };

    const goBack = () => {
      router.push("/recipes");
    };

    const adjustTextareaHeight = (event) => {
      const textarea = event.target;
      textarea.style.height = "auto";
      textarea.style.height = `${textarea.scrollHeight}px`;
    };

    onMounted(fetchRecipe);

    return {
      title,
      description,
      ingredients,
      steps,
      addIngredient,
      removeIngredient,
      addStep,
      removeStep,
      editRecipe,
      goBack,
      adjustTextareaHeight,
    };
  },
};
</script>

<style scoped>
.edit-recipe {
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
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.title-input,
.description-input,
.step-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.ingredient-item,
.step-item {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  align-items: center;
}

.ingredient-item input[type="text"],
.step-item textarea {
  flex-grow: 2;
  height: 2.5rem;
}

.step-item textarea {
  height: auto;
  min-height: 2rem;
  padding: 0.25rem;
  resize: none;
}

.ingredient-item input[type="text"]:nth-child(2) {
  flex-grow: 1;
}

.btn-primary {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #388e3c;
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

.btn-success {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.875rem;
}

.btn-success:hover {
  background-color: #388e3c;
}

.btn-danger {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.875rem;
}

.btn-danger:hover {
  background-color: #d32f2f;
}
</style>
