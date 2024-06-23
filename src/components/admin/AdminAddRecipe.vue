<template>
  <div class="add-recipe">
    <div class="header">
      <h1>Dodaj Przepis (Admin)</h1>
      <button @click="goBack" class="btn btn-secondary">Powrót</button>
    </div>
    <form @submit.prevent="addRecipe">
      <div class="form-group">
        <label for="title">Tytuł:</label>
        <input
          type="text"
          id="title"
          v-model="title"
          class="title-input"
          required
        />
      </div>
      <div class="form-group">
        <label for="category">Kategoria:</label>
        <select
          id="category"
          v-model="category"
          class="category-select"
          required
        >
          <option value="Śniadanie">Śniadanie</option>
          <option value="Ciasta">Ciasta</option>
          <option value="Kolacja">Kolacja</option>
          <option value="Grill">Grill</option>
          <option value="Obiad">Obiad</option>
          <option value="Makarony">Makarony</option>
          <option value="Polska kuchnia">Polska kuchnia</option>
          <option value="Sałatki">Sałatki</option>
          <option value="Zupy">Zupy</option>
          <option value="Kuchnie świata">Kuchnie świata</option>
        </select>
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
          <button type="button" class="btn btn-success" @click="addIngredient">
            Dodaj składnik
          </button>
          <button
            type="button"
            v-if="ingredients.length > 1"
            class="btn btn-danger"
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
            placeholder="Opis kroku"
            required
          ></textarea>
          <button type="button" class="btn btn-success" @click="addStep">
            Dodaj krok
          </button>
          <button
            type="button"
            v-if="steps.length > 1"
            class="btn btn-danger"
            @click="removeStep(index)"
          >
            Usuń
          </button>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Dodaj Przepis</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const title = ref("");
    const category = ref("");
    const ingredients = ref([{ name: "", quantity: "" }]);
    const steps = ref([{ description: "" }]);
    const router = useRouter();

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

    const addRecipe = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:8000/recipe/admin", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            title: title.value,
            category: category.value,
            ingredients: ingredients.value,
            steps: steps.value,
          }),
        });

        if (response.ok) {
          router.push("/recipes");
        } else {
          const errorData = await response.json();
          alert(`Nie udało się dodać przepisu: ${errorData.detail}`);
        }
      } catch (error) {
        console.error("Błąd podczas dodawania przepisu:", error);
        alert("Wystąpił błąd podczas dodawania przepisu.");
      }
    };

    const goBack = () => {
      router.push("/");
    };

    return {
      title,
      category,
      ingredients,
      steps,
      addIngredient,
      removeIngredient,
      addStep,
      removeStep,
      addRecipe,
      goBack,
    };
  },
};
</script>

<style scoped>
.add-recipe {
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
.category-select,
.ingredient-item input[type="text"],
.step-item textarea {
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

.btn-success {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-danger {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}
</style>
