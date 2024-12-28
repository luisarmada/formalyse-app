<template>
    <div class="section-category">
      <p class="category-header">{{ headerText }}</p>
      <router-link :to="redirectTo" class="redirect-text">{{ redirectText }}</router-link>
    </div>
  </template>

<script>
export default {
  name: "SectionCategory",
  props: {
    headerText: {
      type: String,
      default: "Today's Workout", // Default header text
    },
    redirectTo: {
      type: String,
      required: true, // URL path for the router-link
    },
    redirectText: {
        type: String,
        default: "",
    }
  },
};
</script>

<style scoped>
.section-category {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 0px 18px;
}

.category-header {
  font-size: 1.05em;
  font-weight: 600;
}

.redirect-text {
  font-size: 0.9em;
  color: #76dbd1;
  text-decoration: none;
}

.redirect-text:hover {
  text-decoration: underline; /* Optional hover effect */
}
</style>
