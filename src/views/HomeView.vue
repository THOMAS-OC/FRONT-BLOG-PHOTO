<template>
  <main class="SelectAlbum">
        <h2> ALBUMS PHOTOS </h2>
        <section class="choiceGalerie">

            <a v-on:click="filterJsonFile('macro')" href="#">
                <h3>Macrophotographie</h3>
                <img src="../assets/macro_section.jpg" alt="Album macro">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>
            <a v-on:click="filterJsonFile('paysage')" href="#">
                <h3>Paysage</h3>
                <img src="../assets/paysage_section.jpg" alt="Album paysage">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>

            <a v-on:click="filterJsonFile('animalier')" href="#">
                <h3>Animalier</h3>
                <img src="../assets/animalier_section.jpg" alt="Album animaux">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>

        </section>

        <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>

        <h2 class="nameAlbum">{{ nameAlbum }}</h2>

        <section class="album displayNone">

          <div v-for="item in currentJsonFile" :key="item.categorie">
            <a download="arty.jpg" :href=item.urlDownload target="_blank"> <i class="fa-solid fa-file-arrow-down"></i> </a>
            <img :src=item.urlFileCompressed :alt=item.alt>
          </div>

        </section>


  </main>
</template>

<script>
export default {
  name: 'SelectAlbum',

  data(){
      return {
        nameAlbum: "",
        saveJsonFile : require('../assets/' + 'photos.json'),
        currentJsonFile : null
      }
  },

  created: function() {
    let description = "Bienvenu dans mon univers photographique ! Vous trouverez ici l'ensemble de mes photos téléchargeables gratuitement ainsi que de nombreux photographes amateurs à découvrir"
    document.title = "Découvrez mon univers photographique / ARTY"
    document.querySelector('meta[name="description"]').setAttribute("content", description)
  },

  methods:{
    filterJsonFile (album) {
    this.currentJsonFile = null
    this.currentJsonFile = this.saveJsonFile.filter(item => item.categorie == album)
    this.currentJsonFile = this.currentJsonFile.sort((a, b) => a.order - b.order)
    // Affichage de la section
    document.querySelector(".album").className = "album"

    // AFFICHAGE DU NOM DE L'ALBUM

     if (album == "macro"){
          this.nameAlbum = "Macro".toUpperCase()
          document.querySelector(".nameAlbum").className = "nameAlbum op1"

      }
    else if (album == "paysage"){
          this.nameAlbum = "Paysage".toUpperCase()
          document.querySelector(".nameAlbum").className = "nameAlbum op1"

      }
    else if (album == "animalier"){
          this.nameAlbum = "Animalier".toUpperCase()
          document.querySelector(".nameAlbum").className = "nameAlbum op1"

      }

      document.querySelector(".lds-roller").className = "lds-roller loaderFondu"

      setTimeout(()=>{
        document.querySelector(".lds-roller").className = "lds-roller"
        document.querySelector(".album").scrollIntoView()
      }, 2500)

    },

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.nameAlbum{
  font-style: italic;
  height: 500px;
  opacity: 0 !important;
  line-height: 500px;
  background-attachment: fixed;
  background-size: cover;
  transition-duration: 1s;
}

.displayNone {
  display: none;
}

.op1{
  opacity: 1 !important;
}

.loaderFondu{
    animation-name: loaderFondu;
    animation-duration: 2.5s;
    animation-fill-mode: both;
}

@keyframes loaderFondu {
    from{
        opacity: 1
    }

    to{
        opacity: 0
    }
}

/* LOADER */

.lds-roller {
  display: block;
  position: relative;
  margin: 10px auto;
  opacity: 0;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: " ";
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #fff;
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* END LOADER */

h2{
    margin-top: 150px;
    margin-bottom: 50px;
    color: white;
    letter-spacing: 5px;
    word-spacing: 10px;
    font-size: 40px;
    animation-name: titleAnimation;
    animation-duration: 1s;
    animation-delay: 2s;
    animation-fill-mode: both;
    text-align: center;
    text-shadow: 0px 0px 3px black;
}

@keyframes titleAnimation {
  0%{
    opacity: 0;
  }
  100%{
    opacity: 1;
  }
}


/* Layout galerie */
.choiceGalerie{
    margin: 30px auto;
    width: 1500px;
    max-width: 90vw;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;

}

.choiceGalerie > a {
    height: 400px;
    width: 300px;
    background-color: black;
    border: 2px solid white;
    overflow: hidden;
    cursor: pointer;
    position: relative;
    z-index: 1;
    transition-duration: 0.3;
    animation-name: cardSection;
    animation-duration: 1s;
    animation-delay: 2.5s;
    animation-fill-mode: both;
    position: relative;
    margin: auto;
    margin-top: 50px;
}

.choiceGalerie > a h3{
    position: absolute;
    top: 0;
    left: 0;
    height: 60px;
    width: 100%;
    background-color: rgb(255, 255, 255);
    color: black;
    text-align: center;
    line-height: 60px;
    z-index: 50;
    font-size: 30px;
    font-weight: normal;
    font-family: 'Splash', cursive;
    box-shadow: 0px 3px 3px black;
}

.choiceGalerie > a:nth-child(1){
    animation-delay: 2s;
}

.choiceGalerie > a:nth-child(2){
    animation-delay: 2.5s;
}

.choiceGalerie > a:nth-child(3){
    animation-delay: 3s;
}

.choiceGalerie > a:nth-child(4){
    animation-delay: 3.5s;
}

.choiceGalerie a:hover {
    box-shadow: 0px 0px 30px whitesmoke;
}

.choiceGalerie a:hover img {
    transform: scale(1.2);
    filter: brightness(1);
}

.choiceGalerie img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition-duration: 1s;
    filter: brightness(0.8);
}

.curl{
    background-image: url("../assets/curlRotate.png");
    position: absolute;
    right: 0;
    bottom: 0;
    width: 100px;
    height: 100px;
}

@keyframes cardSection {
    from{
        opacity: 0;
        transform: translateY(500px);
    }

    to{
        opacity: 1;
        transform: translateY(0px);
    }
}

/* RESPONSIVE */

@media (max-width: 680px) { 

  .choiceGalerie > a {
        width: 85vw;
  }

  .nameAlbum{
    height: 200px;
    line-height: 200px;

  }

}


</style>
