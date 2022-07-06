<template>
  <div id="app">

    <the-header></the-header>

    <transition>

      <router-view/>

    </transition>

    <the-footer></the-footer>


  </div>
</template>

<script>

import TheHeader from './components/TheHeader.vue'
import TheFooter from './components/TheFooter.vue'


export default {
  name:"app",
  components: {
    TheHeader,
    TheFooter
  },

}


</script>

<style>

/* TRANSITION DU ROUTEUR */


/* DISPARITION */

.v-leave-active{
  opacity: 1;
  transform: translateX(0%);
  transition-duration: 2s;
}

.v-leave-to{
  opacity: 0;
  transform: translateX(-100%);

}

/* GESTION DU BACKGROUND */

body{
    background-image: url("assets/background-flou.jpg");
    background-position: center;
    background-attachment: fixed;
    width: 100vw;
    height: 100vh;
    background-repeat: no-repeat;
    background-size: cover;
}

/* FIN DE GESTION DU BACKGROUND */

/* GESTION DE L'AFFICHAGE DES PHOTOS */

section.album{
  margin: 100px auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 1300px;
  max-width: 90vw;
  height: auto;
}

section.album div{
  width: 400px;
  max-width: 90vw;
  max-height: 90vw;
  height: 400px;
  margin: auto;
  margin-top: 50px;
  border: 2px solid white;
  border-radius: 2px;
  animation-name: imageAnimate;
  animation-delay: 2s;
  animation-duration: 1s;
  animation-fill-mode: both;
}

section.album img{
  object-fit: contain;
  object-position: center;
  width: 100%;
  height: 100%;
}

section.album a {
  position: absolute;
  bottom: 50px;
  right: 50px;
  font-size: 50px;
  color: white;
  text-shadow: 0px 0px 5px rgb(0, 0, 0);

}

@keyframes imageAnimate {
  from{
    transform: scale(0.2);
    opacity: 0;
  }

  to{
    transform: scale(1);
    opacity: 1;
  }
}


/* FIN DE GESTION DE L'AFFICHAGE DES PHOTOS */

/* GESTION DU LOGO */

.logoInNav {
    position: absolute;
    bottom: 0;
    left: 50%;
    font-weight: normal;
    transform: translateX(-50%);
    font-size: 50px;
    font-family: 'Splash', cursive;
}

</style>
