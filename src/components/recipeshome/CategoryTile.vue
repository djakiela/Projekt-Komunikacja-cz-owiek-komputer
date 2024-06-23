<template>
  <div class="category-tile">
    <router-link :to="link">
      <div class="image-container">
        <img :src="image" :alt="title" />
      </div>
      <h2>{{ title }}</h2>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "CategoryTile",
  props: {
    title: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      required: true,
    },
    link: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.category-tile {
  width: 200px;
  margin: 10px;
  text-align: center;
  transition: transform 0.3s;
}

.category-tile:hover {
  transform: scale(1.1);
}

.image-container {
  width: 200px;
  height: 200px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.category-tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.category-tile h2 {
  margin-top: 10px;
  font-size: 18px;
  color: #333;
}

.category-tile a {
  text-decoration: none;
  color: inherit;
}

.category-tile a:hover {
  color: inherit;
}
</style>
