<template>
    <div>
      <div id="header">
        <router-link to="/" class="nav-link" active-class="active">
          <span class="material-icons back-button">arrow_back</span>
        </router-link>
        <h1>Settings</h1>
      </div>
  
      <div class="settings-content">
        <div class="theme-toggle">
          <label class="switch">
            <input type="checkbox" v-model="isDarkMode" @change="toggleTheme" />
            <span class="slider"></span>
          </label>
          <p>{{ isDarkMode ? "Dark Mode" : "Light Mode" }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SettingsPage",
    data() {
      return {
        isDarkMode: true, // Default mode
      };
    },
    mounted() {
      this.$emit("toggleNavbar", false);
  
      // Load the saved theme on component load
      this.isDarkMode = document.documentElement.className === "dark-mode";
    },
    methods: {
      toggleTheme() {
        // Switch between dark and light modes
        const theme = this.isDarkMode ? "dark-mode" : "light-mode";
        document.documentElement.className = theme;
  
        // Save the selected theme to localStorage
        localStorage.setItem("theme", theme);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Header styling */
  #header {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-top: 24px;
    margin-left: 18px;
    height: 50px;
  }
  
  .back-button {
    font-size: 2.2em;
    margin-top: 4px;
  }
  
  h1 {
    font-size: 1.8em;
  }
  
  /* Settings content */
  .settings-content {
    margin: 24px;
  }
  
  /* Switch slider styles */
  .switch {
    position: relative;
    display: inline-block;
    width: 50px;
    height: 25px;
  }
  
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    border-radius: 25px;
    cursor: pointer;
    transition: 0.4s;
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 17px;
    width: 17px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    border-radius: 50%;
    transition: 0.4s;
  }
  
  input:checked + .slider {
    background-color: #76dbd1;
  }
  
  input:checked + .slider:before {
    transform: translateX(24px);
  }
  
  /* Text styling for theme toggle */
  .theme-toggle {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
  }
  
  .theme-toggle p {
    font-size: 1em;
    font-weight: 500;
  }
  </style>
  