<template>
    <div v-if="exercise" class="body-highlighter">
      <!-- Base body template -->
      <img :src="getImagePath('EmptyBody')" alt="Empty Body" class="base-body" />
  
      <!-- Highlighted muscles -->
      <img
        v-for="(muscle, index) in exercise.muscleGroups"
        :key="index"
        :src="getImagePath(muscle)"
        :alt="muscle"
        class="muscle-overlay"
      />
    </div>
    <p v-else>Loading...</p>
  </template>
  
  <script>
  import { exercises } from '../data/exerciseData'; // Import exercise data
  
  export default {
    name: "BodyHighlighter",
    props: {
      slug: {
        type: String,
        required: true, // Expects an exercise slug
      },
    },
    data() {
      return {
        exercise: null, // Will store the matched exercise
      };
    },
    mounted() {
      this.fetchExercise(); // Fetch exercise when component mounts
    },
    methods: {
      fetchExercise() {
        this.exercise = exercises.find((ex) => ex.slug === this.slug);
      },
      getImagePath(muscle) {
        return `/body-highlights/${muscle}.png`; // Adjust path if needed
      },
    },
  };
  </script>
  
<style scoped>
.body-highlighter {
    position: relative;
    width: 300px; /* Adjust as needed */
    margin: auto;
    z-index: 0; /* Ensure it stays below elements like the navbar */
}

.base-body {
    width: 100%;
    position: relative;
    z-index: 1; /* Base body layer */
}

.muscle-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 2; /* Overlay layer */
    pointer-events: none; /* Prevent mouse interaction */
}
</style>
  
  