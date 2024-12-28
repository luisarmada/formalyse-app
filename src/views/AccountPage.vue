<template>
    <div id="header">
        <BackButton />
        <h1>Account</h1>
    </div>
    
</template>

<script>
import BackButton from '../components/BackButton.vue';
export default {
  name: 'AccountPage',
  components: {
    BackButton,
  },
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', false);
  },
};
</script>

<style>

#header {
    display: flex;
    align-items: center;
    justify-content: row;
    gap: 18px;
    margin-top: 24px;
    margin-left: 18px;
    height: 50px;
}

.back-button {
    font-size: 2.2em;
    margin-top: 4px;
}
h1 {
   font-size: 1.8em; 
}
</style>