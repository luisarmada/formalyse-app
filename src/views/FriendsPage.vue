<template>
    <h1>Community Page</h1>
</template>

<script>
export default {
  name: 'FriendsPage',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
};
</script>