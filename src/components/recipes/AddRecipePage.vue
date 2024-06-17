<template>
  <div class="add-recipe">
    <h1>Dodaj Przepis</h1>
    <form @submit.prevent="addRecipe">
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
        </div>
        <button type="button" @click="addIngredient">Dodaj składnik</button>
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

    const addRecipe = async () => {
      try {
        const response = await fetch("http://localhost:8000/recipe", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
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
          alert("Nie udało się dodać przepisu.");
        }
      } catch (error) {
        console.error("Błąd podczas dodawania przepisu:", error);
        alert("Wystąpił błąd podczas dodawania przepisu.");
      }
    };

    return {
      title,
      description,
      ingredients,
      addIngredient,
      addRecipe,
    };
  },
};
</script>

<style scoped>
.add-recipe {
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

.ingredient-item {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
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
