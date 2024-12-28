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

    <SectionCategory 
      headerText="Continue Your Program" 
      redirect-text="Change"
      redirectTo="/programs" 
    />

    <ProgramTile
      name="Beginners Calisthenics"
      day_name= "Monday, Push Day"
      metrics="120"
      image="/stock/bodyweight/ab-crunch.jpg"
    />

    <SectionCategory 
      headerText="Exercise Database" 
      redirect-text=""
      redirectTo="/programs" 
    />

    <SearchBar @search="handleSearch" />

    <div class="exercise-list">
      <ExerciseInformation
        v-for="exercise in filteredExercises"
        :key="exercise.name"
        :exerciseName="exercise.name"
        :exerciseLink="exercise.link"
      />
    </div>

    <!-- <p v-for="i in 50" :key="i">Placeholder content {{ i }}</p> -->
    <!-- <div class="video-container">
      <img :src="webcamUrl" alt="Webcam Feed" class="webcam-stream" />
    </div> -->


</template>

<script>
import ProgramTile from '../components/ProgramTile.vue';
import SectionCategory from '../components/SectionCategory.vue';
import SearchBar from '../components/SearchBar.vue';
import ExerciseInformation from '../components/ExerciseInformation.vue';

export default {
  name: 'HomePage',
  components: {
    ProgramTile,
    SectionCategory,
    SearchBar,
    ExerciseInformation,
  },
  data() {
    return {
      exercises: [
        {
          name: "Push-ups",
          description: "A bodyweight exercise targeting chest, shoulders, and triceps.",
          imageSrc: "/stock/bodyweight/ab-crunch.jpg",
          link: "/exercises/push-ups",
        },
        {
          name: "Pull-ups",
          description: "A compound exercise focusing on back and biceps strength.",
          imageSrc: "https://via.placeholder.com/80?text=Pull-ups",
          link: "/exercises/pull-ups",
        },
        {
          name: "Squats",
          description: "A foundational exercise for lower body strength and stability.",
          imageSrc: "https://via.placeholder.com/80?text=Squats",
          link: "/exercises/squats",
        },
        {
          name: "Lunges",
          description: "A great unilateral exercise for quads, hamstrings, and glutes.",
          imageSrc: "https://via.placeholder.com/80?text=Lunges",
          link: "/exercises/lunges",
        },
        {
          name: "Plank",
          description: "An isometric core exercise for stability and endurance.",
          imageSrc: "https://via.placeholder.com/80?text=Plank",
          link: "/exercises/plank",
        },
      ],
      searchQuery: "",
    };
  },
  computed: {
    filteredExercises() {
      if (!this.searchQuery) return this.exercises;
      return this.exercises.filter((exercise) =>
        exercise.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
  methods: {
    handleSearch(query) {
      this.searchQuery = query;
    },
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
    margin-bottom: 18px;
    font-size: 1.8em;
    font-weight: 500;
}


.section-category {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    margin-right: 24px;
}

.category-header{
    font-size: 1.05em;
    font-weight: 500;
}

.redirect-text {
  font-size: 0.9em;
  color: #76dbd1;
}

.exercise-list {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
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