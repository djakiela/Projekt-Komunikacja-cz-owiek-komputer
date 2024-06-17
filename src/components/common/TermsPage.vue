<template>
  <div class="terms-page">
    <h1>Regulamin</h1>
    <p>Tutaj znajdzie się treść regulaminu serwisu.</p>
    <button @click="goBack" class="btn btn-secondary">
      Powrót do rejestracji
    </button>
  </div>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  name: "TermsPage",
  setup() {
    const router = useRouter();

    const goBack = () => {
      router.push("/register");
    };

    return {
      goBack,
    };
  },
};
</script>

<style scoped>
.terms-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  border-radius: 0.5rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
}

.terms-page h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.terms-page p {
  font-size: 1rem;
  line-height: 1.5;
}

.btn {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  margin-top: 1rem;
}

.btn-secondary {
  background-color: #388e3c;
}

.btn:hover {
  background-color: #388e3c;
}

.btn-secondary:hover {
  background-color: #2e7d32;
}
</style>
