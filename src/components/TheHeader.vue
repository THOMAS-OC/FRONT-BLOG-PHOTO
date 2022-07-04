<template>


    <header class="TheHeader">
      <nav>
        <router-link to="/">Accueil</router-link>
        <router-link to="/Contact">Contact</router-link>
        <h1 class="logoInNav">Arty</h1>
      </nav>
    </header>


</template>

<script>
export default {
  name: 'TheHeader',

  methods:{

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


header{
    height: 100px;
    width: 100vw;
    background-color: #FFFFFF;
    box-shadow: 0px 10px 3px rgba(0, 0, 0, 0.80);
    position: relative;
    z-index: 2;
}

nav {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    color: black;
    font-style: italic;
    text-decoration: none;
    line-height: 100px;
    font-size: 35px;
    position: relative;
}

nav a {
  font-weight: bold;
  color: #7b7b7b;
}

nav a.router-link-exact-active {
  color: #000000;
}


</style>
