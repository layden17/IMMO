// script.js
const openPopupButton = document.getElementById("openPopup");
const closePopupButton = document.getElementById("closePopup");
const popup = document.getElementById("popup");
const popupContent = document.getElementById("popupContent");

openPopupButton.addEventListener("click", () => {
  // Charger le contenu de la page souhaitée dans popupContent
  // Exemple : Vous pouvez utiliser une requête AJAX pour obtenir le contenu de la page.
  // Ici, je vais simplement afficher un texte d'exemple.
  popupContent.innerHTML = "<p>Contenu de la page à afficher dans la pop-up.</p>";

  popup.style.display = "block";
});

closePopupButton.addEventListener("click", () => {
  popup.style.display = "none";
});
