<template>
    <div class="exercise-info" @click="goToExercise">
      <div class="exercise-image">
        <img src="/stock/bodyweight/ab-crunch.jpg" :alt="exerciseName" />
      </div>
      <div class="exercise-text">
        <p class="exercise-name">{{ exerciseName }}</p>
        <p class="exercise-description">{{ description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ExerciseInformation",
    props: {
      exerciseName: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        default: "No description available.",
      },
      imageSrc: {
        type: String,
        required: true,
      },
      exerciseLink: {
        type: String,
        required: true,
      },
    },
    methods: {
      goToExercise() {
        this.$router.push(this.exerciseLink);
      },
    },
  };
  </script>
  

  <style scoped>
  .exercise-info {
    display: flex;
    align-items: center;
    cursor: pointer;
    border-radius: 24px;
    height: 110px;
    overflow: hidden; /* Ensures the image is clipped by the borders */
    margin: 4px 18px;
    transition: background-color 0.3s ease;
    background-color: #1d1d1d;
  }
  
  .exercise-info:hover {
    background-color: #2a2a2a;
  }
  
  .exercise-image {
    flex: 0 0 110px; /* Set a fixed width for the image */
    height: 110px; /* Ensure the image height matches the component */
    overflow: hidden;
    border-radius: 24px 0 0 24px; /* Match parent border radius on the left */
  }
  
  .exercise-image img {
    width: 100%; /* Scale the image to fill the container */
    height: 100%; /* Ensure no overflow */
    object-fit: cover; /* Crop the image to maintain aspect ratio */
  }
  
  .exercise-text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 8px 16px; /* Space around the text */
    flex: 1; /* Take up remaining space */
  }
  
  .exercise-name {
    font-size: 1em;
    font-weight: bold;
    margin: 0;
  }
  
  .exercise-description {
    font-size: 0.9em;
    color: #666;
    margin: 4px 0 0;
  }
  </style>
  