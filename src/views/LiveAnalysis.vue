
<template>
  <div class="page-container">
    <!-- Video Container with Loading Text -->
    <div class="video-wrapper">
      <div v-if="!cameraActive" class="loading-overlay">
        Loading...
      </div>
      <img v-if="cameraActive" :src="webcamUrl" alt="Webcam Feed" class="webcam-stream" />
    </div>

    <!-- Analysis Buttons -->
    <div class="analysis-button-container">
      <button class="analysis-button" @click="goBack">
        <div class="back-button">
          <span class="material-icons arrow-icon">arrow_back</span>
          <p>Back</p>
        </div>
      </button>
      <button class="analysis-button">
        <div class="finish-button">
          <p>Finish</p>
          <span class="material-icons arrow-icon">arrow_forward</span>
        </div>
      </button>
    </div>
  </div>
</template>


<script>
// import { exercises } from "../data/exerciseData.js"; // Centralized data for fallback

export default {
  name: 'LiveAnalysis',
  data() {
    return {
      webcamUrl: "",
      cameraActive: false,
      exercise: null,
    };
  },
  async mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', false);

    // // find exercise
    // const slug = this.$route.params.slug;
    // if (this.$route.state?.exercise) {
    //   this.exercise = this.$route.state.exercise;
    // } else {
    //   this.exercise = exercises.find((ex) => ex.slug === slug);
    // }

    // Fetch request to activate the camera
    try {

      // Fetch request to activate the camera
      const response = await fetch("http://127.0.0.1:5000/start_camera", {
        method: "POST",
      });

      if (response.ok) {
        const data = await response.json();
        if (data.status === "success") {
          // this.webcamUrl = `http://127.0.0.1:8000/video?time=${Date.now()}`;
          this.cameraActive = true; // Activate camera flag
          this.webcamUrl = `http://127.0.0.1:5000/video?time=${Date.now()}`;
        }
      }
    } catch (error) {
      // Handle any errors during the fetch
      this.cameraActive = false;
    }
  },
  async beforeUnmount() {
    // Deactivate the camera on the backend
    try {
      // Deactivate the camera when leaving the page
      await fetch("http://127.0.0.1:5000/stop_camera", {
        method: "POST",
      });
    } catch (error) {
      // Handle any errors during the fetch
    } finally {
      this.cameraActive = false; // Reset camera activation flag
      this.webcamUrl = "";
    }
  },
  methods: {
    goBack() {
        window.history.back(); // Go back to the previous page
    },
  }
};
</script>

<style scoped>
/* Prevent scrolling on the page */
body {
  overflow: hidden;
}

/* Page container for consistent layout */
.page-container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Full viewport height */
  background-color: var(--background-color); /* Optional background color for the whole page */
  overflow: hidden;
}

/* Wrapper for the video feed */
.video-wrapper {
  position: relative;
  width: 100%;
  max-width: 800px; /* Optional: Set a max width */
  height: 350px; /* Fixed height */
  background-color: black; /* Black background */
  border-radius: 0px;
  overflow: hidden; /* Ensure video stays within bounds */
}

/* Webcam stream */
.webcam-stream {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Maintain aspect ratio */
  border-radius: 0px;
}

/* Loading overlay */
.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5em;
  font-weight: bold;
  background-color: black;
  z-index: 1;
  overflow: hidden;
}

/* Button container */
.analysis-button-container {
  position: fixed;
  bottom: 18px;
  left: 18px;
  right: 18px;
  height: 60px;
  display: flex;
  justify-content: center;
  gap: 12px;
  z-index: 1000;
  overflow: hidden;
}

/* Button styles */
.analysis-button {
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
  width: 100%;
  padding: 0px 40px;
  background-color: var(--button-background-color);
  color: white;
  font-size: 1em;
  font-weight: 500;
  border: none;
  border-radius: 60px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.analysis-button:hover {
  background-color: var(--button-hover-color);
}

.analysis-button div {
  display: flex;
  flex-direction: row;
  height: 100%;
  gap: 12px;
  align-items: center;
  justify-content: center;
  margin-top: 1px;
}

.arrow-icon {
  color: var(--icon-button-color);
  margin-top: 4px;
  font-size: 0.9em;
}

.back-button {
  margin-right: 12px;
  font-size: 1.05em;
}

.finish-button {
  margin-left: 12px;
  font-size: 1.05em;
  margin-top: -1px;
}
</style>
