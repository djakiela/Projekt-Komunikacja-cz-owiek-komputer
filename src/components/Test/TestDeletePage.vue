<template>
  <div>
    <button @click="testDeleteRecipe">Test Delete Recipe</button>
  </div>
</template>

<script>
export default {
  setup() {
    const testDeleteRecipe = async () => {
      const recipeId = 1;
      console.log("Deleting recipe with ID:", recipeId);
      try {
        const token = localStorage.getItem("token");
        console.log("Token:", token);
        if (!token) {
          console.error("No token found in localStorage");
          return;
        }
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
        } else {
          const errorData = await response.json();
          console.error("Błąd podczas usuwania przepisu:", errorData);
        }
      } catch (error) {
        console.error("Błąd podczas usuwania przepisu:", error);
      }
    };

    return {
      testDeleteRecipe,
    };
  },
};
</script>
