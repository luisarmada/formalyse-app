<template>
    <h1>Programs Page</h1>

</template>

<script>
export default {
  name: 'ProgramsPage',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
};
</script>