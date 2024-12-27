<template>
    
    <div id="account-bar">
        <div id="formalyse-logo">
            <img src="../../public/formalyse-logo-teal-invert.png" />
            <h1 id="logo-name">formalyse</h1>
        </div>
        <router-link to="/settings" class="nav-link" active-class="active">
            <span class="material-icons-outlined outlined-icon">settings</span>
        </router-link>
    </div>
    
    <p id="greetings-text">Morning, Luis 👋</p>

    <p class="category-header">Today's Workout</p>

    <p class="category-header">Custom Workout</p>

    <p class="category-header">Live Analysis</p>


    <!-- <div class="video-container">
      <img :src="webcamUrl" alt="Webcam Feed" class="webcam-stream" />
    </div> -->


</template>

<script>
export default {
  name: 'HomePage',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
};
</script>

<style scoped>
#account-bar {

    display: flex;
    justify-content: row;
    align-items: center;

    margin-top: 24px;
    height: 48px;
    width: 100%;
}


#formalyse-logo {
    flex: 1;
    display: flex;
    align-items: row;
    align-items: center;

    height: 100%;
    gap: 8px;

    margin-left: 18px;

    font-family: 'Poppins', sans-serif;
    font-weight: 100;
    font-size: 0.8em;
}

#formalyse-logo img {
    max-height: 100%;
    object-fit: contain;
    border-radius: 12px;
}

#logo-name{
  color: #76dbd1;
}

.outlined-icon {
    color: #999999;
    margin-right: 24px;
}

p {
    margin-left: 18px;
}

#greetings-text{
    margin-top: 32px;
    font-size: 1.8em;
    font-weight: 500;
}

.category-header{
    font-size: 1.05em;
    font-weight: 500;
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