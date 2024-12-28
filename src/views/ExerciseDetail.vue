<template>
    <div class="exercise-detail" v-if="exercise">
        <div class="image-header">
            <img :src="imageSrc" :alt="exercise.name" class="header-image" />
            <div id="header">
                <BackButton />
            </div>
            
        </div>

        <div class="exercise-content">
            <h1>{{ exercise.name }}</h1>

            <!-- Render tags iteratively -->
            <div class="tags">
                <ExerciseTag v-for="(tag, index) in exercise.tags" :key="index" :tag="tag" />
            </div>

            <!-- <p>{{ exercise.description }}</p> -->

            <SectionCategory 
            headerText="Form & Technique Tips" 
            redirect-text="See All"
            redirectTo="/programs" 
            />

            <!-- Conditional Button -->
            <div v-if="hasLiveAnalysis" class="analysis-button-container">
                <button class="analysis-button" @click="startLiveAnalysis">
                    Start Live Analysis
                </button>
            </div>
        </div>
    </div>
  </template>
  
  
<script>
import { exercises } from "../data/exerciseData.js"; // Centralized data for fallback
import ExerciseTag from "../components/ExerciseTag.vue";
import SectionCategory from "../components/SectionCategory.vue";
import BackButton from "../components/BackButton.vue";
  
  export default {
    name: "ExerciseDetail",
    components: {
        SectionCategory,
        ExerciseTag,
        BackButton,
    },
    data() {
      return {
        exercise: this.$route.state || null,
      };
    },
    computed: {
        imageSrc() {
            return `/stock/exercises/${this.exercise.slug}/display.jpg`;
        },
        hasLiveAnalysis() {
            return this.exercise.tags.includes("Live Analysis");
        },
    },
    mounted() {
        this.$emit('toggleNavbar', false);
        if (!this.exercise) {
        // Fallback if state is not available (direct navigation)
        const slug = this.$route.params.slug;
        this.exercise = exercises.find((ex) => ex.slug === slug);

        // If exercise not found, redirect to home
        if (!this.exercise) {
            this.$router.push("/");
        }
        }
    },
    methods: {
        startLiveAnalysis() {
            alert(`Starting live analysis for ${this.exercise.name}`); // Placeholder for live analysis logic
        },
    }
  };
  </script>

  <style scoped>
  .exercise-detail {
    margin: 0; /* Reset margin for the entire page */
    padding: 0; /* Reset padding for the entire page */
  }
  
  /* Image header styles */
  .image-header {
    position: relative;
    width: 100%;
    height: 250px; /* Adjust height as needed */
    overflow: hidden; /* Ensure the image doesn't overflow */
  }
  
  .header-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; /* Ensures the image covers the area proportionally */
  }
  
  /* Header on top of the image */
  #header {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    align-items: center;
    padding: 0px;
    margin-top: 24px;
    color: white; /* Ensure text is visible on dark images */
    z-index: 10; /* Ensure the header appears above the image */
  }
  
  .back-button {
    font-size: 2.2em;
    color: #ffffffaa;
  }
  
  /* Content section */
  .exercise-content {
    margin: 0px 24px;
  }
  
  .exercise-content h1 {
    font-size: 1.8em;
    margin-top: 32px;
  }
  
  .exercise-content p {
    font-size: 1em;
    line-height: 1.5;
  }

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.analysis-button-container {
    /* margin: 0px 18px; */
    position: fixed;
    bottom: 18px;
    left: 18px;
    right: 18px;
    height: 60px;
    display: flex;
    justify-content: center;
    z-index: 1000; /* Ensure it stays above other elements */
    padding: 0;
}

.analysis-button {
    font-family: Inter, Avenir, Helvetica, Arial, sans-serif;

    width: 100%;
    padding: 12px 24px;
    background-color: var(--primary-darker-color);
    color: white;
    font-size: 1.05em;
    font-weight: 600;
    border: none;
    border-radius: 60px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.analysis-button:hover {
  background-color: #4aa79d;
}
</style>
  