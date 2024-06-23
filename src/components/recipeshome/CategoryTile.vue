<template>
  <div class="category-tile">
    <router-link :to="link">
      <div class="image-container">
        <img :src="image" :alt="title" />
      </div>
      <h2>{{ title }}</h2>
      <p>{{ description }}</p>
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
    description: {
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
  width: 220px;
  margin: 10px;
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
  border-radius: 15px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.category-tile:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.image-container {
  width: 220px;
  height: 220px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.category-tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.category-tile h2 {
  margin-top: 10px;
  font-size: 1.2rem;
  color: #333;
}

.category-tile p {
  margin-top: 5px;
  font-size: 0.9rem;
  color: #777;
}

.category-tile a {
  text-decoration: none;
  color: inherit;
}

.category-tile a:hover {
  color: inherit;
}
</style>
