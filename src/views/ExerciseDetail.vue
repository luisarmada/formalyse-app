<template>
  <div>
    <!-- Loading state -->
    <div v-if="loading" class="loading-container">Loading...</div>

    <!-- Main content -->
    <div v-else-if="exercise" class="exercise-detail">
      <div class="image-header">
        <img :src="imageSrc" :alt="exercise.name" class="header-image" />
        <div id="header">
          <BackButton />
        </div>
      </div>

      <div class="exercise-content">
        <h1>{{ exercise.name }}</h1>

        <!-- Tags -->
        <div class="tags">
          <ExerciseTag
            v-for="(tag, index) in exercise.tags"
            :key="index"
            :tag="tag"
          />
        </div>

        <!-- Section Category -->
        <SectionCategory
          headerText="Form & Technique Tips"
          redirect-text="See All"
          redirectTo="/programs"
        />

        <div class="demonstration-img-container">
          <img :src="demonstrationSrc" />
        </div>

        <div class="instruction-container">
          <ExerciseInstruction
          v-for="(instruction, index) in exercise.instructions"
          :key = index
          :instruction = instruction
          :count = index
        />
        </div>
        
        <SectionCategory
          headerText="Common Form Mistakes"
          redirect-text="See All"
          redirectTo="/programs"
        />

        

        <!-- Live Analysis Button -->
        <div v-if="hasLiveAnalysis" class="analysis-button-container">
          <button class="analysis-button" @click="startLiveAnalysis">
            Start Live Analysis
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { exercises } from "../data/exerciseData.js"; // Centralized data for fallback
import ExerciseTag from "../components/ExerciseTag.vue";
import SectionCategory from "../components/SectionCategory.vue";
import BackButton from "../components/BackButton.vue";
import ExerciseInstruction from "../components/ExerciseInstruction.vue";

export default {
  name: "ExerciseDetail",
  components: {
    SectionCategory,
    ExerciseTag,
    BackButton,
    ExerciseInstruction,
  },
  data() {
    return {
      exercise: null, // Holds the current exercise data
      loading: true, // Tracks loading state
    };
  },
  computed: {
    imageSrc() {
      // Compute the image path only when exercise is defined
      return this.exercise
        ? `/stock/exercises/${this.exercise.slug}/display.jpg`
        : "";
    },
    demonstrationSrc() {
      return this.exercise
        ? `/stock/exercises/${this.exercise.slug}/demonstration.gif`
        : "";
    },
    hasLiveAnalysis() {
      // Check if the exercise has the "Live Analysis" tag
      return this.exercise?.tags.includes("Live Analysis");
    },
  },
  mounted() {
    this.$emit("toggleNavbar", false); // Assuming this hides the navbar

    // Attempt to load exercise from route state or centralized data
    const slug = this.$route.params.slug;
    if (this.$route.state?.exercise) {
      this.exercise = this.$route.state.exercise;
    } else {
      this.exercise = exercises.find((ex) => ex.slug === slug);
    }

    // Redirect if exercise is not found
    if (!this.exercise) {
      console.error(`Exercise with slug "${slug}" not found.`);
      this.$router.push("/");
    }

    // Mark loading as complete
    this.loading = false;
  },
  methods: {
    startLiveAnalysis() {
      alert(`Starting live analysis for ${this.exercise.name}`); // Placeholder for live analysis logic
      this.$router.push({
        path: `/live-analysis`,
        state: {
        }
      });
    },
  },
};
</script>

<style scoped>
/* Page styles */
.exercise-detail {
  margin: 0;
  padding: 0;
}

/* Loading container styles */
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 1.2em;
  font-weight: bold;
  color: #666;
}

/* Image header styles */
.image-header {
  position: relative;
  width: 100%;
  height: 250px;
  overflow: hidden;
}

.header-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  color: white;
  z-index: 10;
}

/* Content section */
.exercise-content {
  margin: 0px 24px;
}

.exercise-content h1 {
  font-size: 1.8em;
  margin-top: 32px;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.demonstration-img-container {
  width: 100%; 
  height: 200px; 
  display: flex;
  align-items: center; 
  justify-content: center; 
  background-color: white; /* Set the background to white */
  overflow: hidden; /* Ensure the image does not overflow */
  border-radius: 24px;
  margin-bottom: 12px;
}

.demonstration-img-container img {
  max-width: 100%; 
  max-height: 100%; 
  object-fit: contain; 
  background-color: white; 
}


.instruction-container{
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Analysis button styles */
.analysis-button-container {
  position: fixed;
  bottom: 18px;
  left: 18px;
  right: 18px;
  height: 60px;
  display: flex;
  justify-content: center;
  z-index: 1000;
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
