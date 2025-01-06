<template>
  <head>
    
  </head>
  <nav class="bottom-nav">
    <router-link to="/" class="nav-link" active-class="active">
      <span class="material-icons">home</span>
      <span>Home</span>
    </router-link>
    <router-link to="/progress" class="nav-link" active-class="active">
      <span class="material-icons">insights</span>
      <span>Activity</span>
    </router-link>
    <router-link to="/programs" class="nav-link" active-class="active">
      <span class="material-icons">fitness_center</span>
      <span>Programs</span>
    </router-link>
    <!-- <router-link to="/friends" class="nav-link" active-class="active">
      <span class="material-icons">groups</span>
      <span>Community</span>
    </router-link> -->
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style>
/* Navbar container */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: var(--background-color);
  display: flex;
  justify-content: space-around;
  padding: 18px 0;
}

/* Router-link styling */
.nav-link {
  color: var(--icon-button-color);
  text-align: center;
  text-decoration: none;
  display: flex;
  flex-direction: column; /* Align icons and text vertically */
  align-items: center;
  transition: color 0.3s ease;

  font-size: 0.9em;
  font-weight: 500;
}

/* Hover effect */
.nav-link:hover {
  color: #BBBBBB;
}

/* Active link styling */
.nav-link.active {
  color: #4ed0c3;
}

/* Material icons */
.material-icons {
  font-size: 24px; /* Icon size */
  margin-bottom: 5px; /* Spacing between icon and text */
}
</style>
