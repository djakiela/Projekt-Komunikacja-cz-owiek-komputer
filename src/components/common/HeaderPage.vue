<template>
  <header class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item brand-title">
        Książka Kucharska Online
      </router-link>
      <router-link v-if="isLoggedIn" to="/recipes" class="navbar-item">
        <i class="fas fa-book"></i> Moje Przepisy
      </router-link>
      <router-link v-if="isLoggedIn" to="/add-recipe" class="navbar-item">
        <i class="fas fa-plus"></i> Dodaj Przepis
      </router-link>
    </div>
    <div class="navbar-end">
      <div
        class="navbar-item user-icon"
        @mouseenter="showDropdown"
        @mouseleave="hideDropdown"
      >
        <a class="navbar-link">
          <i class="fas fa-user"></i>
        </a>
        <div class="navbar-dropdown is-right" v-show="isDropdownActive">
          <router-link v-if="!isLoggedIn" to="/login" class="navbar-item">
            Logowanie
          </router-link>
          <router-link v-if="!isLoggedIn" to="/register" class="navbar-item">
            Rejestracja
          </router-link>
          <router-link v-if="isLoggedIn" to="/edit-profile" class="navbar-item">
            Edytuj Profil
          </router-link>
          <a v-if="isLoggedIn" class="navbar-item" @click="logout"> Wyloguj </a>
        </div>
      </div>
    </div>
    <AlertPage v-if="showAlert" :message="alertMessage" @close="closeAlert" />
  </header>
</template>

<script>
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { ref, computed, onMounted } from "vue";
import AlertPage from "./AlertPage.vue";

export default {
  components: { AlertPage },
  setup() {
    const store = useStore();
    const router = useRouter();
    const isDropdownActive = ref(false);
    const showAlert = ref(false);
    const alertMessage = ref("");

    const currentUser = computed(() => store.state.user);
    const isLoggedIn = computed(() => !!store.state.user);

    const showDropdown = () => {
      isDropdownActive.value = true;
    };

    const hideDropdown = () => {
      isDropdownActive.value = false;
    };

    const closeAlert = () => {
      showAlert.value = false;
    };

    const logout = async () => {
      try {
        const response = await fetch("http://localhost:8000/user/logout", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error("Nie udało się wylogować.");
        }

        store.commit("setUser", null);
        showAlert.value = true;
        alertMessage.value = "Pomyślnie wylogowano.";
        setTimeout(() => {
          closeAlert();
          router.push("/");
        }, 3000);
      } catch (error) {
        console.error("Błąd podczas wylogowywania:", error);
      }
    };

    const fetchCurrentUser = async () => {
      const token = localStorage.getItem("token");
      if (token) {
        try {
          const response = await fetch("http://localhost:8000/auth/me", {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          if (response.ok) {
            const data = await response.json();
            store.commit("setUser", data);
          } else {
            console.error("Nie udało się pobrać danych użytkownika.");
          }
        } catch (error) {
          console.error("Błąd podczas pobierania danych użytkownika:", error);
        }
      }
    };

    onMounted(() => {
      fetchCurrentUser();
    });

    return {
      isDropdownActive,
      currentUser,
      isLoggedIn,
      showDropdown,
      hideDropdown,
      logout,
      showAlert,
      alertMessage,
      closeAlert,
    };
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #4caf50;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.navbar-item {
  margin-right: 1rem;
  color: white;
  text-decoration: none;
}

.navbar-item:hover {
  color: #ffeb3b;
}

.brand-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
}

.navbar-end {
  display: flex;
  align-items: center;
}

.user-icon {
  position: relative;
}

.navbar-link {
  cursor: pointer;
  color: white;
}

.navbar-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  border-radius: 4px;
  display: none;
}

.navbar-dropdown.is-right {
  right: 0;
}

.navbar-item {
  padding: 0.5rem 1rem;
  white-space: nowrap;
  color: black;
}

.user-icon:hover .navbar-dropdown {
  display: block;
}

.navbar-dropdown .navbar-item:hover {
  color: black;
  font-weight: bold;
}
</style>
