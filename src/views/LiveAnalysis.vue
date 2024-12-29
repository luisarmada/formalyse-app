<template>
    <div class="video-container">
      <video :src="webcamUrl" autoplay playsinline muted alt="Webcam Feed" class="webcam-stream" />
    </div>

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
</template>

<script>
export default {
  name: 'LiveAnalysis',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', false);
  },
  data() {
    return {
      webcamUrl: "http://127.0.0.1:5000/video", // Update with your Flask server URL and port
    };
  },
  methods: {
    goBack() {
        window.history.back(); // Go back to the previous page
    },
  }
};
</script>

<style>
body{
    overflow: hidden;
}

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
}

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
.analysis-button div{
  display:flex;
  flex-direction: row;
  height: 100%;
  gap: 12px;
  align-items: center;
  justify-content: center;
  margin-top: 1px;
}

.arrow-icon{
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



.video-container {
  margin-top: 20px;
  width: 80%;
  max-width: 600px;
}

.webcam-stream {
  width: 100%;
  border-radius: 8px;
  border: 2px solid #333;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

</style>