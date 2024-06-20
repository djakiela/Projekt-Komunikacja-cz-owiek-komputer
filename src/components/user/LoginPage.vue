<template>
  <div class="login-form">
    <h1>Logowanie</h1>
    <form @submit.prevent="login" class="form-container">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="button-group">
        <button type="submit" class="btn btn-primary">Zaloguj</button>
        <button @click.prevent="goBack" class="btn btn-secondary">
          Powrót
        </button>
      </div>
      <p class="register-link">
        Nie masz konta?
        <router-link to="/register">Zarejestruj się</router-link>
      </p>
    </form>
    <AlertPage
      v-if="showAlert"
      :message="alertMessage"
      @close="handleAlertClose"
    />
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";
import AlertPage from "../common/AlertPage.vue";

export default {
  components: {
    AlertPage,
  },
  setup() {
    const username = ref("");
    const password = ref("");
    const showAlert = ref(false);
    const alertMessage = ref("");
    const router = useRouter();
    const store = useStore();

    const login = async () => {
      try {
        const response = await fetch("http://localhost:8000/auth/token", {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: new URLSearchParams({
            username: username.value,
            password: password.value,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          const token = data.access_token;
          store.commit("setToken", token);

          const userResponse = await fetch("http://localhost:8000/auth/me", {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          });

          if (userResponse.ok) {
            const userData = await userResponse.json();
            store.commit("setUser", userData);
            router.push("/");
          } else {
            throw new Error("Nie udało się pobrać danych użytkownika.");
          }
        } else {
          const errorData = await response.json();
          alertMessage.value = `Logowanie nie powiodło się: ${errorData.detail}`;
          showAlert.value = true;
        }
      } catch (error) {
        console.error("Błąd podczas logowania:", error);
        alertMessage.value = "Logowanie nie powiodło się.";
        showAlert.value = true;
      }
    };

    const handleAlertClose = () => {
      showAlert.value = false;
    };

    const goBack = () => {
      router.push("/");
    };

    return {
      username,
      password,
      showAlert,
      alertMessage,
      login,
      handleAlertClose,
      goBack,
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
  color: #4caf50;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input[type="text"],
.form-group input[type="password"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.button-group {
  display: flex;
  justify-content: space-between;
}

.btn {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
}

.btn-secondary {
  background-color: #4caf50;
}

.btn:hover {
  background-color: #45a049;
}

.btn-secondary:hover {
  background-color: #45a049;
}

.register-link {
  margin-top: 1rem;
  text-align: center;
  color: #333;
}

.register-link a {
  color: #4caf50;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>
