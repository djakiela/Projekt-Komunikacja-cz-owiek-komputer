<template>
  <div class="recipes-home">
    <div class="categories">
      <CategoryTile
        v-for="category in categories"
        :key="category.name"
        :title="category.name"
        :description="category.description"
        :image="category.image"
        :link="category.link"
      />
    </div>
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
          description: "Zacznij dzień od zdrowego i pysznego śniadania.",
          image: require("@/components/recipeshome/photos/breakfast.png"),
          link: "/breakfast",
        },
        {
          name: "Ciasta",
          description: "Przepisy na słodkie i pyszne ciasta na każdą okazję.",
          image: require("@/components/recipeshome/photos/cakes.jpg"),
          link: "/cakes",
        },
        {
          name: "Kolacja",
          description: "Pyszne przepisy na wieczorny posiłek.",
          image: require("@/components/recipeshome/photos/dinner.jpg"),
          link: "/dinner",
        },
        {
          name: "Grill",
          description: "Przepisy na grilla dla każdego smakosza.",
          image: require("@/components/recipeshome/photos/grill.jpg"),
          link: "/grill",
        },
        {
          name: "Obiad",
          description: "Pomysły na sycący i smaczny obiad.",
          image: require("@/components/recipeshome/photos/lunch.jpeg"),
          link: "/lunch",
        },
        {
          name: "Makarony",
          description: "Przepisy na różnorodne dania z makaronem.",
          image: require("@/components/recipeshome/photos/pasta.jpg"),
          link: "/pasta",
        },
        {
          name: "Polska kuchnia",
          description: "Tradycyjne przepisy kuchni polskiej.",
          image: require("@/components/recipeshome/photos/polish.jpg"),
          link: "/polish",
        },
        {
          name: "Sałatki",
          description: "Przepisy na zdrowe i kolorowe sałatki.",
          image: require("@/components/recipeshome/photos/salads.jpg"),
          link: "/salads",
        },
        {
          name: "Zupy",
          description: "Rozgrzewające przepisy na zupy.",
          image: require("@/components/recipeshome/photos/soups.jpeg"),
          link: "/soups",
        },
        {
          name: "Kuchnie świata",
          description: "Poznaj smaki z całego świata.",
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
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
</style>
