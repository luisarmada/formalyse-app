<template>
    <div :class="['tag', { 'live-analysis-tag': isLiveAnalysis }]">
        {{ tag }}
    </div>
  </template>
  
  <script>
  export default {
    name: "ExerciseTag",
    props: {
      tag: {
        type: String,
        required: true,
      },
    },
    computed: {
        isLiveAnalysis() {
            return this.tag.toLowerCase() === "live analysis"; // Check if the tag is "Live Analysis"
        },
    },
  };
  </script>
  
<style scoped>
.tag {
padding: 2px 8px;
background-color: #ffffff00;
color: var(--primary-darker-color);
font-size: 0.7em;
font-weight: 600;
border-radius: 12px;
border: 1px solid var(--primary-darker-color);
}

 /**af8dff */
.live-analysis-tag {
padding: 2px 8px;
background-color: #ffffff00;
color: var(--primary-darker-color);
font-size: 0.7em;
font-weight: 600;
border-radius: 12px;
border: 1px solid var(--primary-darker-color);
}
</style>
