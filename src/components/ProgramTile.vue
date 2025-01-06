<template>
<div class="center-container">
    <img v-if="image" :src="image" alt="Background" class="background-image" />
    <div class="content-overlay">
        <h1 id="program-name">{{ name }}</h1>
        <div class="program-info">
            <p>{{ day_name }}</p>
            <p id="metrics-text">
                {{ metrics }}
                <span class="space"> </span>
                <span class="material-icons metrics-icon streak-flame">local_fire_department</span>
                <span class="space"> </span>
                0%
                <span class="space"> </span>
                <span class="material-icons metrics-icon trophy">emoji_events</span>
            </p>
        </div>
        
    </div>
</div>
</template>
  
<script>
    export default {
    name: "ProgramTile",
    props: {
        name: {
            type: String,
            default: "Default Title",
        },
        metrics: {
            type: String,
            default: "",
        },
        day_name: {
            type: String,
            default: "",
        },
        image: {
            type: String,
            default: "", // Path to the background image
        },
    },
    };
</script>
  
<style scoped>
.center-container {
    position: relative;
    width: 100%;
    height: 220px;
    display: flex;
    overflow: hidden; 
    background-color: #111;
    border-radius: 24px;
    margin: 0 auto;
}

.background-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; 
    z-index: 1; 
}

.content-overlay {
    position: relative; 
    display: flex;
    flex-direction: column;
    z-index: 2; 
    height: auto;
    width: 100%;
    align-self: flex-end;
    gap: 6px;
    margin: 12px;
}

#program-name {
    font-size: 1.5em;
    margin: 0;
}

.program-info {
    display: flex;
    justify-content: space-between;
    align-items: center; /* Ensure items align vertically */
    font-size: 0.9em;
    font-weight: 500;
    gap: 24px;
    margin: 0;
    height: 100%; /* Ensure this div determines the height */
}

.program-info p {
    margin: 0;
    display: flex;
    align-items: center; /* Align text and icon vertically */
}

.space {
    display: inline-block;
    width: 3px; /* Adjust for consistent spacing */
}

#metrics-text {
    font-weight: 600;
}

.metrics-icon {
    display: inline-flex;
    align-items: center;
    height: 100%; /* Matches parent height */
    font-size: inherit; /* Optional: Adjust icon size to text size */
    transform: translateY(-1px);
}

.streak-flame{
    color: #FFA500;
}

.trophy {
    color: #555555;
}

</style>
  