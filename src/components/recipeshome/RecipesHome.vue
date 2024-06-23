<template>
  <div class="recipes-home">
    <CategoryTile
      v-for="category in categories"
      :key="category.name"
      :title="category.name"
      :image="category.image"
      :link="category.link"
    />
  </div>
</template>

<script>
import CategoryTile from "@/components/recipeshome/CategoryTile.vue";

export default {
  name: "RecipesHome",
  components: {
    CategoryTile,
  },
  data() {
    return {
      categories: [
        {
          name: "Śniadanie",
          image: require("@/components/recipeshome/photos/breakfast.png"),
          link: "/breakfast",
        },
        {
          name: "Ciasta",
          image: require("@/components/recipeshome/photos/cakes.jpg"),
          link: "/cakes",
        },
        {
          name: "Kolacja",
          image: require("@/components/recipeshome/photos/dinner.jpg"),
          link: "/dinner",
        },
        {
          name: "Grill",
          image: require("@/components/recipeshome/photos/grill.jpg"),
          link: "/grill",
        },
        {
          name: "Obiad",
          image: require("@/components/recipeshome/photos/lunch.jpeg"),
          link: "/lunch",
        },
        {
          name: "Makarony",
          image: require("@/components/recipeshome/photos/pasta.jpg"),
          link: "/pasta",
        },
        {
          name: "Polska kuchnia",
          image: require("@/components/recipeshome/photos/polish.jpg"),
          link: "/polish",
        },
        {
          name: "Sałatki",
          image: require("@/components/recipeshome/photos/salads.jpg"),
          link: "/salads",
        },
        {
          name: "Zupy",
          image: require("@/components/recipeshome/photos/soups.jpeg"),
          link: "/soups",
        },
        {
          name: "Kuchnie świata",
          image: require("@/components/recipeshome/photos/world.jpg"),
          link: "/world",
        },
      ],
    };
  },
};
</script>

<style scoped>
.recipes-home {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 20px;
}
</style>
