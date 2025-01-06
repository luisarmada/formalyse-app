// src/router/index.js
import { createRouter, createWebHashHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import FriendsPage from '../views/FriendsPage.vue';
import ProgressPage from '../views/ProgressPage.vue';
import ProgramsPage from '../views/ProgramsPage.vue';
import SettingsPage from '../views/SettingsPage.vue';
import ExerciseDetail from '../views/ExerciseDetail.vue';
import AccountPage from '../views/AccountPage.vue';
import ExerciseSearch from '../views/ExerciseSearch.vue';
import LiveAnalysis from '../views/LiveAnalysis.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/friends', component: FriendsPage },
  { path: '/progress', component: ProgressPage },
  { path: '/programs', component: ProgramsPage },
  { path: '/settings', component: SettingsPage },
  { path: "/exercise/:slug", component: ExerciseDetail },
  { path: '/account', component: AccountPage },
  { path: '/exercise-search', component: ExerciseSearch },
  { path: '/live-analysis/:slug', component: LiveAnalysis },
];

const router = createRouter({
  history: createWebHashHistory(), // Use hash mode for better compatibility with Tauri
  routes,
});

export default router;
