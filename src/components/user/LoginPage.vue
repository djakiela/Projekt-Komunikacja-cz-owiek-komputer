<template>
  <div class="login-form">
    <h1>Logowanie</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="btn btn-primary">Zaloguj</button>
    </form>
    <AlertPage v-if="showAlert" :message="alertMessage" @close="closeAlert" />
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";
import AlertPage from "../common/AlertPage.vue";

export default {
  components: { AlertPage },
  setup() {
    const username = ref("");
    const password = ref("");
    const showAlert = ref(false);
    const alertMessage = ref("");
    const store = useStore();
    const router = useRouter();

    const closeAlert = () => {
      showAlert.value = false;
    };

    const login = async () => {
      try {
        const response = await fetch("http://localhost:8000/user/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          console.log("Dane otrzymane po zalogowaniu:", data);
          store.commit("setUser", data); // Ustawiamy pełne dane użytkownika
          router.push("/test-user");
        } else {
          showAlert.value = true;
          alertMessage.value = "Logowanie nie powiodło się. Spróbuj ponownie.";
        }
      } catch (error) {
        console.error("Błąd podczas logowania:", error);
        showAlert.value = true;
        alertMessage.value = "Błąd podczas logowania. Spróbuj ponownie.";
      }
    };

    return {
      username,
      password,
      login,
      showAlert,
      alertMessage,
      closeAlert,
    };
  },
};
</script>

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.login-form h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #4caf50; /* Zielony kolor */
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.btn {
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
</style>
