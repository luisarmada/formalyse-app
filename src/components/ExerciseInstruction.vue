<template>
  <div class="exercise-info" >
      <div class="exercise-text">
      
        <p class="exercise-name">{{ count + 1 }}. {{ instruction }}</p>

      </div>
  </div>
</template>  

<script>
import ExerciseTag from './ExerciseTag.vue';

export default {
name: "ExerciseInformation",
components: {
  ExerciseTag
},
props: {
  instruction: {
    type: String,
    default: "No instruction available.",
  },
  count: {
    type: Number,
    required: true,
  }
},
};
</script>


<style scoped>
.exercise-info {
  display: flex;
  align-items: center;
  cursor: pointer;
  border-radius: 32px;
  height: 110px;
  overflow: hidden; /* Ensures the image is clipped by the borders */
  transition: background-color 0.3s ease;
  background-color: var(--button-background-color);
}

.exercise-info:hover {
  background-color: var(--button-hover-color);
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
  gap: 6px;
  flex-direction: column;
  justify-content: center;
  padding: 0px 16px; /* Space around the text */
  flex: 1; /* Take up remaining space */
}

.exercise-name {
  font-size: 1em;
  margin: 0;
}
</style>
