<template>
  <div class="register-form">
    <h1>Rejestracja</h1>
    <form @submit.prevent="register" class="form-container">
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Powtórz hasło:</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          required
        />
      </div>
      <div class="form-group checkbox-group">
        <input type="checkbox" id="terms" v-model="acceptTerms" required />
        <label for="terms">
          Akceptuję postanowienia
          <router-link to="/terms">Regulaminu</router-link>
        </label>
      </div>
      <div class="button-group">
        <button type="submit" class="btn btn-primary">Zarejestruj</button>
        <button @click.prevent="goBack" class="btn btn-secondary">
          Powrót
        </button>
      </div>
      <p class="login-link">
        Masz już konto? <router-link to="/login">Zaloguj się</router-link>
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
import { ref } from "vue";
import AlertPage from "../common/AlertPage.vue";

export default {
  components: {
    AlertPage,
  },
  setup() {
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const confirmPassword = ref("");
    const acceptTerms = ref(false);
    const showAlert = ref(false);
    const alertMessage = ref("");
    const router = useRouter();

    const register = async () => {
      if (password.value !== confirmPassword.value) {
        alertMessage.value = "Hasła nie są zgodne.";
        showAlert.value = true;
        return;
      }

      try {
        const response = await fetch("http://localhost:8000/user", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            email: email.value,
            password: password.value,
          }),
        });

        if (response.ok) {
          alertMessage.value = "Rejestracja zakończona sukcesem!";
          showAlert.value = true;
        } else {
          const errorData = await response.json();
          alertMessage.value = `Rejestracja nie powiodła się: ${errorData.detail}`;
          showAlert.value = true;
        }
      } catch (error) {
        console.error("Błąd podczas rejestracji:", error);
        alertMessage.value = "Rejestracja nie powiodła się.";
        showAlert.value = true;
      }
    };

    const handleAlertClose = () => {
      if (alertMessage.value === "Rejestracja zakończona sukcesem!") {
        router.push("/login");
      }
      showAlert.value = false;
    };

    const goBack = () => {
      router.push("/");
    };

    return {
      username,
      email,
      password,
      confirmPassword,
      acceptTerms,
      showAlert,
      alertMessage,
      register,
      handleAlertClose,
      goBack,
    };
  },
};
</script>

<style scoped>
.register-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.register-form h1 {
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
.form-group input[type="email"],
.form-group input[type="password"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.checkbox-group {
  display: flex;
  align-items: center;
}

.checkbox-group input[type="checkbox"] {
  margin-right: 0.5rem;
}

.checkbox-group label {
  margin-bottom: 0;
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

.login-link {
  margin-top: 1rem;
  text-align: center;
  color: #333;
}

.login-link a {
  color: #4caf50;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
