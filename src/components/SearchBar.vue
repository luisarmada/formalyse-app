<template>
    <div class="search-bar">
      <input
        type="text"
        class="search-input"
        placeholder="Search..."
        v-model="searchQuery"
        @keyup.enter="onSearch"
      />
      <span class="material-icons search-icon" @click="onSearch">search</span>
    </div>
  </template>


<script>
export default {
  name: "SearchBar",
  data() {
    return {
      searchQuery: "",
    };
  },
  methods: {
    onSearch() {
      this.$emit("search", this.searchQuery.trim());
    },
  },
};
</script>


<style scoped>
.search-bar {
    display: flex;
    align-items: center;
    margin-left: 18px;
    margin-right: 18px;
    width: auto;

    border: 1px solid #4ed0c3; /* Border color */
    border-radius: 24px; /* Rounded edges */
    padding: 8px 16px; /* Inner padding for the input and icon */
    background-color: #ffffff00; /* Background color */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Optional shadow */
}

.search-input {
  flex: 1; /* Take up available space */
  border: none; /* Remove default input border */
  outline: none; /* Remove focus outline */
  font-size: 1em; /* Font size */
  background-color: #ffffff00;
  color: white;
  padding: 4px; /* Optional padding for the text */
  transform: translateY(-1px);
}

.search-icon {
  font-size: 1.5em; /* Icon size */
  transform: translateY(2px);
  color: #4ed0c3; /* Icon color */
  cursor: pointer; /* Change cursor to pointer */
}
</style>
