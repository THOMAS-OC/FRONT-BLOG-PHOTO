<template>


    <header class="TheHeader">
      <nav>
        <router-link to="/">Accueil</router-link>
        <div class="transition"></div>
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

.transition{
  position: absolute;
  display: none;
  top: 50%;
  left: 50%;
  height: 40%;
  width: 2px;
  transform: translate(-50%, -50%);
  background-color: black;
}


header{
    height: 100px;
    width: 100vw;
    background-color: #FFFFFF;
    box-shadow: 0px 10px 3px rgba(0, 0, 0, 0.80);
    position: relative;
    z-index: 2;
    font-weight: 600;
}

nav {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    color: black;
    text-decoration: none;
    line-height: 100px;
    font-size: 35px;
    position: relative;
}

nav a {
  color: #7b7b7b;
}

nav a.router-link-exact-active {
  color: #000000;
}

/* RESPONSIVE */

@media (max-width: 680px) { 

  header {
      height: 100px;
  }

  .logoInNav {
      position: absolute;
      bottom: -100%;
      color: white;
      text-shadow: 0px 0px 13px black;
      left: 50%;
      transform: translateX(-50%);
      font-size: 50px;
      font-family: 'Splash', cursive;
  }

  .transition{
    display: block;
  }

}


</style>
