<template>
    <div class="exercise-info" @click="goToExercise">
        <div class="exercise-image">
            <img :src="imageSrc" :alt="exerciseName" />
        </div>
        <div class="exercise-text">
        
            <p class="exercise-name">{{ exerciseName }}</p>

            <!-- Render tags iteratively -->
            <div class="tags">
                <ExerciseTag v-for="(tag, index) in limitedTags" :key="index" :tag="tag" />
            </div>

            <!-- <p class="exercise-description">{{ description }}</p> -->
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
    exerciseName: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      default: "No description available.",
    },
    slug: {
      type: String,
      required: true, // The slug is used to dynamically generate imageSrc
    },
    tags: {
      type: Array,
      default: () => [], // Tags array
    },
    exerciseLink: {
      type: String,
      required: true, // Link to the ExerciseDetail page
    },
  },
  computed: {
    imageSrc() {
      // Dynamically construct the image path
      return `/stock/exercises/${this.slug}/display.jpg`;
    },
    limitedTags() {
      // Return only the first 2 tags
      return this.tags.slice(0, 2);
    },
  },
  methods: {
    goToExercise() {
      this.$router.push({
        path: `/exercise/${this.slug}`,
        state: {
          exerciseName: this.exerciseName,
          description: this.description,
          imageSrc: this.imageSrc,
          tags: this.tags,
        },
      });
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
    font-size: 1.05em;
    font-weight: bold;
    margin: 0;
  }
  
  .exercise-description {
    font-size: 0.9em;
    color: #666;
    margin: 4px 0 0;
  }

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
</style>
  