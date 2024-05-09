document.addEventListener("DOMContentLoaded", function () {
    var myCarousel = new bootstrap.Carousel(document.getElementById('carouselExample'), {
      interval: 5000, // Définissez l'intervalle entre les diapositives en millisecondes
      pause: "hover", // Mettez en pause le carrousel lors du survol
      wrap: true // Permettez le rebobinage du carrousel
      
    });
  });
 
  