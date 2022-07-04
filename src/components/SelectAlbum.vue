<template>
  <main class="SelectAlbum">
    <h2>{{ nameAlbum }}</h2>
        <section class="choiceGalerie">
            
            <a class="bnw" v-on:click="select('bnw')" href="#">
                <h2>Black and white</h2>
                <img src="../assets/bnw_section.jpg" alt="Album noir et blanc">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>
            <a v-on:click="select('macro')" href="#">
                <h2>Macrophotographie</h2>
                <img src="../assets/macro_section.jpg" alt="Album macro">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>
            <a v-on:click="select('paysage')" href="#">
                <h2>Paysage</h2>
                <img src="../assets/paysage_section.jpg" alt="Album paysage">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>

            <a v-on:click="select('animalier')" href="#">
                <h2>Animalier</h2>
                <img src="../assets/animalier_section.jpg" alt="Album animaux">
                <div class="curl">
                    <img src="../assets/curlRotate.png" alt="">
                </div>
            </a>

        </section>

        <section class="album">
        </section>

        <img src="" alt="">

  </main>
</template>

<script>
export default {
  name: 'SelectAlbum',



  props: {
    msg: String
  },

  methods:{

    select(album){
      document.querySelector(".album").innerHTML = ""
      console.log(album);
      this.$http.get(`https://apiphotos.herokuapp.com/album/${album}`)
      .then(function (response) {
        const imgData = response.data;
        for (let img of imgData){
            let newDiv = document.createElement("div");
            newDiv.innerHTML = `<img src="${img.urlFileCompressed}" alt="${img.alt}">`
            document.querySelector(".album").appendChild(newDiv)
        }
      })
      .catch((err)=> {
        console.log(err);
      })

    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

/* Layout galerie */
.choiceGalerie{
    margin: 30px auto;
    width: 1500px;
    max-width: 90vw;
    display: flex;
    justify-content: space-between;
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
    animation-delay: 1s;
    animation-fill-mode: both;
    position: relative;
    margin-top: 50px;
}

.choiceGalerie > a h2{
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
    font-family: 'Splash', cursive;
    box-shadow: 0px 3px 3px black;
}

.choiceGalerie > a:nth-child(1){
    animation-delay: 1s;
}

.choiceGalerie > a:nth-child(2){
    animation-delay: 1.5s;
}

.choiceGalerie > a:nth-child(3){
    animation-delay: 2s;
}

.choiceGalerie > a:nth-child(4){
    animation-delay: 2.5s;
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
        transform: translateY(-500px);
    }

    to{
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
