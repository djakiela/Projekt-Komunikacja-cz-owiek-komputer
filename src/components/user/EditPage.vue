<template>
  <div class="edit-profile">
    <form @submit.prevent="editUsername" class="form-section">
      <h2>Zmień nazwę użytkownika</h2>
      <div class="form-group">
        <label for="username">Nazwa użytkownika:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">Zapisz Zmiany</button>
      </div>
    </form>
    <form @submit.prevent="editPassword" class="form-section">
      <h2>Zmień hasło</h2>
      <div class="form-group">
        <label for="password">Nowe hasło:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">Zapisz Zmiany</button>
        <button @click="goBack" type="button" class="btn btn-secondary">
          Powrót
        </button>
      </div>
    </form>
    <AlertPage v-if="showAlert" :message="alertMessage" @close="closeAlert" />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
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

    const userId = store.getters.user?.id;

    const fetchUserProfile = async () => {
      try {
        const response = await fetch(`http://localhost:8000/user/${userId}`);
        const data = await response.json();
        username.value = data.username;
      } catch (error) {
        console.error("Błąd podczas pobierania danych użytkownika:", error);
      }
    };

    const editUsername = async () => {
      try {
        const response = await fetch(`http://localhost:8000/user/${userId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
          }),
        });

        if (response.ok) {
          alertMessage.value = "Nazwa użytkownika zmieniona pomyślnie!";
          showAlert.value = true;
        } else {
          alertMessage.value = "Nie udało się zmienić nazwy użytkownika.";
          showAlert.value = true;
        }
      } catch (error) {
        console.error("Błąd podczas zmiany nazwy użytkownika:", error);
        alertMessage.value = "Nie udało się zmienić nazwy użytkownika.";
        showAlert.value = true;
      }
    };

    const editPassword = async () => {
      try {
        const response = await fetch(`http://localhost:8000/user/${userId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            password: password.value,
          }),
        });

        if (response.ok) {
          alertMessage.value = "Hasło zmienione pomyślnie!";
          showAlert.value = true;
        } else {
          alertMessage.value = "Nie udało się zmienić hasła.";
          showAlert.value = true;
        }
      } catch (error) {
        console.error("Błąd podczas zmiany hasła:", error);
        alertMessage.value = "Nie udało się zmienić hasła.";
        showAlert.value = true;
      }
    };

    const closeAlert = () => {
      showAlert.value = false;
    };

    const goBack = () => {
      router.push("/");
    };

    onMounted(fetchUserProfile);

    return {
      username,
      password,
      editUsername,
      editPassword,
      showAlert,
      alertMessage,
      closeAlert,
      goBack,
    };
  },
};
</script>

<style scoped>
.edit-profile {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background-color: white;
  border-radius: 0.5rem;
}

.form-section {
  margin-bottom: 2rem;
}

.form-section h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #4caf50;
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

.form-actions {
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

.btn-primary:hover {
  background-color: #388e3c;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>
