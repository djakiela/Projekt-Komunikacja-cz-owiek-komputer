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
import BreakfastPage from "./components/recipeshome/BreakfastPage.vue";
import CakesPage from "./components/recipeshome/CakesPage.vue";
import DinnerPage from "./components/recipeshome/DinnerPage.vue";
import GrillPage from "./components/recipeshome/GrillPage.vue";
import LunchPage from "./components/recipeshome/LunchPage.vue";
import PastaPage from "./components/recipeshome/PastaPage.vue";
import PolishPage from "./components/recipeshome/PolishPage.vue";
import SaladsPage from "./components/recipeshome/SaladsPage.vue";
import SoupsPage from "./components/recipeshome/SoupsPage.vue";
import WorldPage from "./components/recipeshome/WorldPage.vue";
import AdminAddRecipePage from "./components/admin/AdminAddRecipe.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/add-recipe", component: AddRecipePage },
  { path: "/edit-recipe/:id", component: EditRecipePage },
  { path: "/recipes", name: "RecipeList", component: RecipeList },
  {
    path: "/recipe/:id",
    name: "RecipeDetails",
    component: RecipeDetails,
    props: true,
  },
  { path: "/edit-profile", component: EditProfilePage },
  { path: "/terms", component: TermsPage },
  { path: "/test-user", component: TestUserPage },
  { path: "/breakfast", component: BreakfastPage },
  { path: "/cakes", component: CakesPage },
  { path: "/dinner", component: DinnerPage },
  { path: "/grill", component: GrillPage },
  { path: "/lunch", component: LunchPage },
  { path: "/pasta", component: PastaPage },
  { path: "/polish", component: PolishPage },
  { path: "/salads", component: SaladsPage },
  { path: "/soups", component: SoupsPage },
  { path: "/world", component: WorldPage },
  { path: "/admin/add-recipe", component: AdminAddRecipePage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
