<template>
  
</template>

<script>
export default {
  name: 'ProgressPage',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
};
</script>