<template>
    <button class="back-button" @click="goBack">
      <span class="material-icons back-icon">arrow_back</span>
    </button>
  </template>
  
  <script>
  export default {
    name: "BackButton",
    methods: {
        goBack() {
            window.history.back(); // Go back to the previous page
        },
    },
  };
  </script>
  
  <style scoped>
  .back-button {
    display: flex;
    align-items: center;
    font-weight: bold;
    border: none;
    border-radius: 24px;
    cursor: pointer;
    background-color: transparent;
  }

  .back-icon {
    color: #ffffffaa;
    font-size: 0.9em;
    margin-top: 2px;
  }
  </style>
  