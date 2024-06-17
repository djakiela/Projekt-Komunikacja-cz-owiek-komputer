<template>
  <div v-if="visible" class="alert-overlay">
    <div class="alert-box">
      <p>{{ message }}</p>
      <button @click="closeAlert">OK</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      visible: true,
    };
  },
  methods: {
    closeAlert() {
      this.visible = false;
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.alert-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.alert-box {
  background-color: white;
  padding: 1rem 2rem;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
  text-align: center;
}

.alert-box p {
  margin-bottom: 1rem;
}

.alert-box button {
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.alert-box button:hover {
  background-color: #45a049;
}
</style>
