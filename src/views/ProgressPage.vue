<template>
    <h1>Progress Page</h1>

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