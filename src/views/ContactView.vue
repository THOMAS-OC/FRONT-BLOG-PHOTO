<template>
  
    <main class="contact">
        <h1>Contactez-moi</h1>
       
        <form action="/sendEmail" method="post">

            <label for="nom">nom</label>
            <input pattern="[a-zA-Z]{3,50}" required placeholder="Dupont" type="text" id="nom" name="nom">

            <label for="prenom">prenom</label>
            <input pattern="[a-zA-Z]{3,50}" required placeholder="Jean" type="text" id="prenom" name="prenom">

            <label for="message">Message</label>
            <textarea placeholder="Bonjour..." name="message" id="message" cols="30" rows="10"></textarea>

            <label for="email">email</label>
            <input required placeholder="doudoulapinou@gmail.com" type="email" name="email" id="email">

            <input disabled type="submit" value="Envoyer">

        </form>

    </main>

</template>

<script>
// @ is an alias to /src

export default {
  name: 'ContactView',
  components: {
  },

  created: function() {
    let description = "Vous pouvez directement me contacter à travers ce formulaire pour toutes demandes !"
    document.title = "Contactez-moi / Arty blog photographique"
    document.querySelector('meta[name="description"]').setAttribute("content", description)

  }
}
</script>


<style scoped>

h1{
    margin-top: 150px;
    margin-bottom: 50px;
    color: white;
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



/* CONTACT LAYOUT */

  form{
      background-color: rgba(0, 0, 0, 0.386);
      border-radius: 15px;
      padding: 30px;
      margin: 150px auto;
      width: 70vw;
      max-width: 800px;
      flex-direction: column;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      color: white;
      animation-name: windowForm;
      animation-duration: 1.5s;
      animation-iteration-count: 1;
      animation-fill-mode: both;
      animation-delay: 2s;
  }

  input, textarea{
    max-width: 100%;
    font-size: 20px;
  }

  input, select, textarea {
      border: none;
      border: 2px solid white;
      background-color: transparent;
      color: white;
      height: 30px;
      border-radius: 3px;
      resize : none;
      animation-name: toRight;
      animation-duration: 1.5s;
      animation-iteration-count: 1;
      animation-fill-mode: both;
      animation-delay: 2s;

  }

  textarea{
      height: 100px;
  }

  option{
      color: black;
  }

  @keyframes toRight {
      from{
          opacity: 0;
          transform: translateX(-200%);
      }

      to{
          opacity: 1;
          transform: translateX(0%);
      }
  }


  @keyframes windowForm {
      from{
          opacity: 0;
          transform: translateX(100%);
      }

      to{
          opacity: 1;
          transform: translateX(0%);
      }
  }


  @keyframes label {
      from{
          opacity: 0;
          transform: translateY(100%);
      }

      to{
          opacity: 1;
          transform: translateY(0%);
      }
  }

  @keyframes button {
      from{
          opacity: 0;
          transform: translateX(50%);
      }

      to{
          opacity: 1;
          transform: translateX(0%);
      }
  }

  input:focus{
      border-bottom: 2px solid rgb(104, 104, 255);
  }

  label {
      margin-top: 70px;
      margin-bottom: 20px;
      cursor: pointer;
      font-style: italic;
      animation-name: label;
      animation-duration: 1s;
      animation-iteration-count: 1;
      animation-fill-mode: both;
      animation-delay: 2s;
      margin-left: 10px;
  }

  input[type="submit"]{
      width: 240px;
      height: 50px;
      border: 3px solid white;
      cursor: pointer;
      border-radius: 10px;
      margin-top: 50px;
      font-size: 20px;
      transition-duration: 0.5s;
      animation-name: button;
      animation-duration: 1s;
      animation-iteration-count: 1;
      animation-fill-mode: both;
      animation-delay: 2s;
  }

  input[type="submit"]:hover{
      background-color: gray;
      padding-left: 10px;
  }

  input[type="submit"]:focus{
      background-color: gray;
  }

  input:focus:valid{
      border-bottom: 2px solid rgb(76, 255, 76);
  }

  input:focus:invalid{
      border: 2px solid rgb(255, 29, 29);
  }

</style>