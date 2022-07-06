<template>
  <div id="app">

    <div class="loading">
      <div class="lds-grid"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
    
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

/* LOADING DE LA PAGE */

.loading{
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: black;
  z-index: 100;
  animation-name: loader;
  animation-duration: 4s;
  animation-fill-mode: both;
}

@keyframes loader {
  0%{
    opacity: 1;
  }
  50%{
    display: inline-block;
    opacity: 1;
  }
  95%{
    display: inline-block;
    opacity: 0;
  }
  100%{
    opacity: 0;
    visibility: hidden;
    display: none;
  }
}

.lds-grid {
  display: inline-block;
  position: absolute;
  width: 80px;
  height: 80px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(2);
}
.lds-grid div {
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #fff;
  animation: lds-grid 1.2s linear infinite;
}
.lds-grid div:nth-child(1) {
  top: 8px;
  left: 8px;
  animation-delay: 0s;
}
.lds-grid div:nth-child(2) {
  top: 8px;
  left: 32px;
  animation-delay: -0.4s;
}
.lds-grid div:nth-child(3) {
  top: 8px;
  left: 56px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(4) {
  top: 32px;
  left: 8px;
  animation-delay: -0.4s;
}
.lds-grid div:nth-child(5) {
  top: 32px;
  left: 32px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(6) {
  top: 32px;
  left: 56px;
  animation-delay: -1.2s;
}
.lds-grid div:nth-child(7) {
  top: 56px;
  left: 8px;
  animation-delay: -0.8s;
}
.lds-grid div:nth-child(8) {
  top: 56px;
  left: 32px;
  animation-delay: -1.2s;
}
.lds-grid div:nth-child(9) {
  top: 56px;
  left: 56px;
  animation-delay: -1.6s;
}
@keyframes lds-grid {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

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


#app{
    background-image: url("assets/background-flou.jpg");
    overflow-x: hidden;
    background-position: center;
    background-attachment: fixed;
    width: 100vw;
    background-repeat: no-repeat;
    background-size: cover;
    padding-bottom: 20px;
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
