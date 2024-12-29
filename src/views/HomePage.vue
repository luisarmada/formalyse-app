<template>
    
    <div id="page-content">
      <div id="account-bar">
        <div id="formalyse-logo">
            <img src="/formalyse-logo-teal-invert.png" />
            <h1 id="logo-name">formalyse</h1>
        </div>
        <div class="account-icons">
          <router-link to="/account" class="nav-link" active-class="active">
            <span class="material-icons-outlined outlined-icon">person</span>
          </router-link>
          <router-link to="/settings" class="nav-link" active-class="active">
              <span class="material-icons-outlined outlined-icon">settings</span>
          </router-link>
        </div>
        
      </div>
      
      <p id="greetings-text">Morning, Luis 👋</p>

      <SectionCategory class=""
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
        redirectTo="/exercise-search" 
      />

      <SearchBar @search="handleSearch" />

      <div class="exercise-list">
        <ExerciseInformation
          v-for="exercise in filteredExercises"
          :key="exercise.slug"
          :exerciseName="exercise.name"
          :description="exercise.description"
          :tags="exercise.tags"
          :slug="exercise.slug"
        />
      </div>

      <div v-if="filteredExercises.length === 0" class="no-results">
        <p>0 results found. Search in the Exercise Database instead.</p>
        <button class="see-all-button" @click="resetSearch">Open Exercise Database</button>
      </div>

      <!-- <p v-for="i in 50" :key="i">Placeholder content {{ i }}</p> -->
    </div>
    
</template>

<script>
import { exercises } from "../data/exerciseData.js";
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
      searchQuery: "",
      exercises,
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
    resetSearch() {
      this.searchQuery = ""; // Clear the search query
    },
  },
};
</script>

<style scoped>

#page-content{
  margin: 0px 18px;
}

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
    color: var(--icon-button-color);
}

#greetings-text{
    margin-top: 32px;
    margin-bottom: 18px;
    font-size: 1.8em;
    font-weight: 500;
}

.exercise-list {
  display: flex;
  flex-direction: column;
  margin-top: 12px;
  gap: 12px;
}

.account-icons {
  display: flex;
  flex-direction: row;
  /* border: 2px solid red; */
  gap: 12px;
}

.no-results {
  text-align: center;
  margin: 20px 0;
  color: #555;
}

.no-results p {
  font-size: 1.2em;
  margin-bottom: 12px;
}

.see-all-button {
  padding: 10px 20px;
  background-color: #76dbd1;
  color: white;
  font-size: 1em;
  font-weight: bold;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.see-all-button:hover {
  background-color: #4aa79d;
}

</style>