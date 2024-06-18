import { createStore } from "vuex";

const store = createStore({
  state: {
    user: null,
    token: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
    },
  },
  actions: {
    login({ commit }, { user, token }) {
      commit("setUser", user);
      commit("setToken", token);
    },
    logout({ commit }) {
      commit("setUser", null);
      commit("setToken", null);
      localStorage.removeItem("token");
    },
  },
  getters: {
    user: (state) => state.user,
    token: (state) => state.token,
  },
});

export default store;
