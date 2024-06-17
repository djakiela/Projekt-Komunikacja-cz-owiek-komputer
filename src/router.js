import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/common/HomePage.vue";
import LoginPage from "./components/user/LoginPage.vue";
import RegisterPage from "./components/user/RegisterPage.vue";
import AddRecipePage from "./components/recipes/AddRecipePage.vue";
import EditRecipePage from "./components/recipes/EditRecipePage.vue";
import RecipeList from "./components/recipes/RecipeList.vue";
import RecipeDetails from "./components/recipes/RecipeDetails.vue";
import EditProfilePage from "./components/user/EditPage.vue";
import TermsPage from "./components/common/TermsPage.vue";
import TestUserPage from "./components/Test/TestUserPage.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/add-recipe", component: AddRecipePage },
  { path: "/edit-recipe/:id", component: EditRecipePage },
  { path: "/recipes", component: RecipeList },
  { path: "/recipe/:id", component: RecipeDetails },
  { path: "/edit-profile", component: EditProfilePage },
  { path: "/terms", component: TermsPage },
  { path: "/test-user", component: TestUserPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
