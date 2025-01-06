
<template>
  <div class="page-container">
    <!-- Video Container with Loading Text -->
    <div class="video-wrapper">
      <div v-if="!cameraActive" class="loading-overlay">
        Loading...
      </div>
      <img v-if="cameraActive" :src="webcamUrl" alt="Webcam Feed" class="webcam-stream" />
    </div>  

    <div class="analysis-text-container" v-if="exercise">

       <!-- Slider for Range of Motion -->
       <div class="range-of-motion-slider">
        <input
          type="range"
          id="range"
          min="0"
          max="100"
          ref="rangeSlider"
          v-model="rangeOfMotion"
          disabled
        />
      </div>

      <!-- <h1>For the best results:</h1>
      <ol>
        <li>Position your camera at a {{ exercise.preferredCameraAngle }}.</li>
        <li>Make sure your entire body is visible in the frame.</li>
      </ol> -->
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
            <p>Analyse</p>
            <span class="material-icons arrow-icon">arrow_forward</span>
          </div>
        </button>
      </div>
    </div>
    
  </div>
</template>


<script>
import { nextTick } from "vue";
import { exercises } from "../data/exerciseData.js"; // Centralized data for fallback

export default {
  name: 'LiveAnalysis',
  data() {
    return {
      webcamUrl: "",
      cameraActive: false,
      exercise: null,
      rangeOfMotion: 0,
    };
  },
  async mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', false);

    // Retrieve the slug from the route parameters
    const slug = this.$route.params.slug;

    // Find the exercise based on the slug
    this.exercise = exercises.find((ex) => ex.slug === slug);

    // Redirect if the exercise is not found
    if (!this.exercise) {
      console.error(`Exercise with slug "${slug}" not found.`);
      this.$router.push("/");
    }

    // Fetch request to activate the camera
    this.activateCamera();

    this.simulateRangeOfMotion();
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
  async activateCamera() {
    try {
      const response = await fetch("http://127.0.0.1:5000/start_camera", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          slug: this.exercise.slug, // Include the slug in the request body
        }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.status === "success") {
          this.webcamUrl = `http://127.0.0.1:5000/video?time=${Date.now()}`;
          this.cameraActive = true;
        }
      }
    } catch (error) {
      console.error("Error activating camera:", error);
      this.cameraActive = false;
    }
  },
  simulateRangeOfMotion() {
    // Simulate updating the range of motion dynamically
    setInterval(async () => {
      this.rangeOfMotion = Math.floor(Math.random() * 101); // Random value between 0-100

      await nextTick();

      const slider = this.$refs.rangeSlider;
      if (slider) {
        this.updateSliderGradient(slider);
      }
    }, 1000);
  },
  updateSliderGradient(slider) {
    const value = slider.value;
    const min = slider.min || 0;
    const max = slider.max || 100;

    // Calculate thumb position percentage
    const percentage = ((value - min) / (max - min)) * 100;

    // Update the slider's background
    slider.style.background = `linear-gradient(to right, var(--primary-color) 0%, var(--primary-color) ${percentage}%, var(--button-background-color) ${percentage}%, var(--button-background-color) 100%)`;
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
  height: 600px; /* Fixed height */
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
  text-align: center;
}

.analysis-text-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  margin: 18px 18px;
  overflow: hidden;
  text-align: center;
}

.analysis-text-container h1 {
  font-size: 1.8em;
}
.analysis-text-container ol {
  margin-top: 0px;
  margin-bottom: 0px;
  font-size: 1.1em;
  font-weight: 500;
  text-align: left;
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

.range-of-motion-slider {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
  margin: 18px 0;
}

.range-of-motion-slider input[type="range"] {
  width: 100%; /* Adjust slider width as needed */
  appearance: none;
  height: 6px;
  background: linear-gradient(to right, var(--primary-color) 0%, var(--primary-color) var(--thumb-position, 50%), var(--button-background-color) var(--thumb-position, 50%), var(--button-background-color) 100%);
  border-radius: 6px; /* Rounded track */
  border-radius: 3px;
  outline: none;
}


.range-of-motion-slider input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
}

.range-of-motion-slider input[type="range"]:disabled::-webkit-slider-thumb {
  background-color: var(--primary-color);
}
</style>
