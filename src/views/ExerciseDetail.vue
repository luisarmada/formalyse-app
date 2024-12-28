<template>
    <div class="exercise-detail">
      <h1>{{ exerciseName }}</h1>
      <p>Details about the exercise will go here.</p>
    </div>
  </template>

<script>
export default {
  name: "ExerciseDetail",
  computed: {
    exerciseName() {
      return this.$route.params.name.replace(/-/g, " ");
    },
  },
};
</script>
