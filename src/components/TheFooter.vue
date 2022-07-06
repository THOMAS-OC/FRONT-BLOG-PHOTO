<template>

    <footer class="TheFooter">
        <a target="_blank" href="https://www.instagram.com/arty_photography_83/">
            <i class="fa-brands fa-instagram"></i>
        </a>
        <i class="fa-brands fa-linkedin"></i>
        <i class="fa-brands fa-flickr"></i>
    </footer>

</template>

<script>
export default {
  name: 'TheFooter',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    /* FOOTER */

    footer{
        margin: 200px auto 50px auto;
        width: 200px;
        height: 50px;
        border-bottom: 2px solid white;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 3px;
        border-radius: 2px;
        transform: scaleX(0.2);
        animation-name: footerAnimate;
        animation-duration: 1s;
        animation-delay: 3s;
        animation-fill-mode: both;
    }

    footer i {
        cursor: pointer;
        font-size: 32px;
        color: black;
        text-shadow: 0px 0px 3px white;
    }


    @keyframes footerAnimate {
        from{
            opacity: 0;
            transform: scaleX(0.2);
        }

        to{
            opacity: 1;
            transform: scaleX(1)
        }
    }

    /* RESPONSIVE TABLET */

    
    @media (max-width: 1100px) { 

        footer {
            width: 50vw;
        }

        footer i {
            font-size: 40px;
        }

    }

    /* RESPONSIVE SMARTPHONE */

    @media (max-width: 680px) { 

        footer {
            width: 90vw;
        }

        footer i {
            font-size: 45px;
        }

    }

</style>
