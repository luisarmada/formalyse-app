<script setup>
import { ref } from "vue";
import { invoke } from "@tauri-apps/api/core";

const greetMsg = ref("");
const name = ref("");
const webcamUrl = ref("http://localhost:5000/video"); // Flask backend video URL

async function greet() {
  // Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
  greetMsg.value = await invoke("greet", { name: name.value });
}
</script>

<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
  </head>
  <div id="app">
    
    <main class="scrollable-container">
      <router-view v-slot="{ Component }">
        <component :is="Component" @toggleNavbar="toggleNavbar" />
      </router-view>
    </main>

    <NavBar v-if="isNavbarEnabled" />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data() {
    return {
      isNavbarEnabled: true, // Default navbar state
    };
  },
  methods: {
    toggleNavbar(enabled) {
      this.isNavbarEnabled = enabled;
    },
  },
};
</script>

<style>
body, html, #app {
  margin: 0;
  padding: 0;
}

:root {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;

  color: #ffffff;
  background-color: #111111; /*161618*/

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
  overflow: hidden;
}

#app {
  overflow: hidden; /* Prevent full app scrolling */
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.scrollable-container {
  flex: 1; /* Ensures the main content scrolls independently */
  overflow-y: auto;
  overflow-x: hidden;
  width: 100%;
  left: 0;

  margin: 0;
  padding-bottom: 50px; /* Reserve space for navbar */
  -ms-overflow-style: none; /* Internet Explorer 10+ */
  scrollbar-width: none; /* Firefox */
}

.scrollable-container::-webkit-scrollbar {
  display: none; /* Hides scrollbar */
}
</style>

