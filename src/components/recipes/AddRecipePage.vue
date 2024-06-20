<template>
  <div class="add-recipe">
    <div class="header">
      <h1>Dodaj Przepis</h1>
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
        <label for="description">Opis:</label>
        <textarea
          id="description"
          v-model="description"
          class="description-input"
          required
        ></textarea>
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
    const description = ref("");
    const ingredients = ref([{ name: "", quantity: "" }]);
    const router = useRouter();

    const addIngredient = () => {
      ingredients.value.push({ name: "", quantity: "" });
    };

    const removeIngredient = (index) => {
      if (ingredients.value.length > 1) {
        ingredients.value.splice(index, 1);
      }
    };

    const addRecipe = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:8000/recipe/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            title: title.value,
            description: description.value,
            ingredients: ingredients.value,
          }),
        });

        if (response.ok) {
          alert("Przepis dodany pomyślnie!");
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
      description,
      ingredients,
      addIngredient,
      removeIngredient,
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
.description-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.title-input:focus,
.description-input:focus {
  outline: none;
}

.ingredient-item {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.ingredient-item input[type="text"] {
  flex-grow: 2;
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

.btn-primary:focus {
  outline: none;
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

.btn-secondary:focus {
  outline: none;
}

.btn-success {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-success:hover {
  background-color: #388e3c;
}

.btn-success:focus {
  outline: none;
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

.btn-danger:focus {
  outline: none;
}
</style>
