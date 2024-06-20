<template>
  <div>
    <h1>Test User</h1>
    <div v-if="user">
      <p>ID użytkownika: {{ userId }}</p>
      <p>Nazwa użytkownika: {{ username }}</p>
      <p>Email: {{ email }}</p>
    </div>
    <div v-else>
      <p>Nie zalogowano użytkownika.</p>
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "TestUserPage",
  setup() {
    const store = useStore();
    const user = computed(() => store.state.user);

    return {
      user,
      userId: computed(() => user.value?.id || ""),
      username: computed(() => user.value?.username || ""),
      email: computed(() => user.value?.email || ""),
    };
  },
};
</script>

<style scoped></style>
