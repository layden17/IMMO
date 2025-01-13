

 

// On initialise les variables qui contiendront le prix total des produits sélectionnés
let totalPrice1 = 0;
let totalPrice2 = 0;

// Cette fonction calcule le prix total des produits d'une table donnée
function calculateTotalPrice(tableId) {
  
  // On récupère la table des produits sélectionnés à partir de son ID
  const selectedProductsTable = document.getElementById(tableId);
  
  // On initialise la variable qui contiendra le prix total
  let totalPrice = 0;
  
  // Pour chaque ligne de la table (à partir de la 2ème car la première contient les entêtes de colonne)
  for (let i = 1; i < selectedProductsTable.rows.length; i++) {
    
    // On récupère la cellule qui contient le prix total de la ligne
    const totalPriceCell = selectedProductsTable.rows[i].cells[selectedProductsTable.rows[i].cells.length - 2];
    
    // On extrait le prix à partir du contenu de la cellule
    const price = parseFloat(totalPriceCell.textContent);

    // On affiche le prix dans la console (pour des raisons de débogage)
    console.log(`Price: ${price}`);
    
    // On ajoute le prix à la variable qui contient le prix total
    totalPrice +=price;
  }
  
  // On retourne le prix total
  return totalPrice;
}

// Cette fonction permet de gerer 
function setupProductTable(containerId, tableId, namequantity, onChangeQuantity) {
  const container = document.getElementById(containerId);
  if (container) {
    container.addEventListener('change', function(event) {
      if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {
        if (event.target.checked) {
          addProduct(event.target);
        } else {
          removeProduct1(event.target.value);
        }
      }
    });
  }

  // Cette fonction permet d'ajouter un produit à la table des produits sélectionnés
function addProduct(checkbox) {
    
  // On récupère l'élément label associé à la case à cocher, qui contient le nom, le prix et la quantité du produit
  const productLabel = checkbox.parentNode.querySelector('label');
  
  // On extrait le nom, le prix et la quantité du produit à partir de l'élément label
  const productName = productLabel.textContent.trim();
  const productPrice = productLabel.getAttribute('data-price');
  const productquantite = productLabel.getAttribute('data-quantite');

  // On récupère l'ID du produit à partir de la valeur de la case à cocher
  const productId = checkbox.value;

  // On crée un champ input pour entrer le prix du produit
  const PriceInput=document.createElement('input');
  PriceInput.setAttribute('type', 'number');
  PriceInput.setAttribute('id',  `prix_${productId}`);
  PriceInput.setAttribute('name',  `prix_${productId}`)
  PriceInput.value=productPrice

  // On récupère la table des produits sélectionnés à partir de son ID
  const selectedProductsTable = document.getElementById(tableId);

  // On insère une nouvelle ligne dans la table pour le produit ajouté
  const newRow = selectedProductsTable.insertRow();
  newRow.setAttribute('id', `product_${productId}`);
  newRow.insertCell().textContent = productName;

  // On insère un champ input pour entrer la quantité du produit
  const priceCell = newRow.insertCell();
  priceCell.appendChild(PriceInput)

  const quantityCell = newRow.insertCell();
  const quantityInput = document.createElement('input');
  quantityInput.setAttribute('type', 'number');
  quantityInput.setAttribute('name', `${namequantity}_${productId}`);
  quantityInput.setAttribute('id',  `${namequantity}_${productId}`);
  quantityInput.value=productquantite
  quantityCell.appendChild(quantityInput);

  // On insère une cellule pour afficher le prix total du produit
  const totalPriceCell = newRow.insertCell();
  totalPriceCell.setAttribute('id', `total_price_${productId}`);

  // On ajoute des écouteurs d'événements sur les champs input pour recalculer le prix total et appeler la fonction onChangeQuantity à chaque changement de quantité ou de prix
  PriceInput.addEventListener('input',function(){
    if(quantityInput.value!=""){
    const totalPriceCell = document.getElementById(`total_price_${productId}`);
    const totalPrice = (quantityInput.value * PriceInput.value).toFixed(2);
    totalPriceCell.textContent = totalPrice;
    onChangeQuantity(productId, quantityInput.value, totalPrice);

    }
  }
  )
  quantityInput.addEventListener('input', function() {
    const totalPriceCell = document.getElementById(`total_price_${productId}`);
    const totalPrice = (quantityInput.value * PriceInput.value).toFixed(2);
    totalPriceCell.textContent = totalPrice;
    onChangeQuantity(productId, quantityInput.value, totalPrice);
  });

  // On calcule le prix total initial du produit et on l'affiche dans la cellule correspondante
  const totalPrice = (quantityInput.value * PriceInput.value).toFixed(2);
  totalPriceCell.textContent = totalPrice;

  // On ajoute un bouton de suppression pour le produit ajouté
  const deleteCell = newRow.insertCell();
  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Supprimer';
  deleteButton.addEventListener('click', function() {
    removeProduct1(productId);
    checkbox.checked = false;
  });
  deleteCell.appendChild(deleteButton)

    checkbox.addEventListener('change', function() {
      if (!checkbox.checked) {
        removeProduct1(productId);
      }
    });
  }

  // Cette fonction permet de supprimer un produit de la table des produits sélectionnés à partir de son ID
function removeProduct1(productId) {
    
  // On récupère la ligne correspondant au produit à partir de son ID
  const productRow = document.getElementById(`product_${productId}`);
  
  // Si la ligne existe
  if (productRow) {
    
    // On supprime la ligne de la table
    productRow.parentNode.removeChild(productRow);
    
    // On recalcule le prix total des produits sélectionnés
    totalPrice1 = calculateTotalPrice(tableId);

    // On met à jour l'affichage de la somme des prix totaux
    document.getElementById('id_Prix_total').value =totalPrice2 + totalPrice1;
    triggerEvent(document.getElementById('id_Prix_total'), 'input');
  }
}

// Ce code permet de vérifier si des cases à cocher sont déjà cochées au chargement de la page, et d'ajouter les produits correspondants à la table des produits sélectionnés
const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
checkboxes.forEach(checkbox => {
addProduct(checkbox);
});

// Cet écouteur d'événements permet de recalculer le prix total des produits sélectionnés et d'afficher la somme des prix totaux à chaque changement dans la table des produits sélectionnés
document.getElementById(tableId).addEventListener('input', function() {
totalPrice1 = calculateTotalPrice(tableId);

// Modifier le code ici pour afficher la somme des prix totaux, par exemple :
console.log(totalPrice1)
document.getElementById('id_Prix_total').value =totalPrice2 + totalPrice1;
triggerEvent(document.getElementById('id_Prix_total'), 'input');
});
}


setupProductTable('autre_produits_container', 'selected_products_table','quantity_autre_produit', function(productId, quantity, totalPrice) {
  // Do something with the updated quantity and total price
});


// Cette fonction permet de configurer la table des produits pour les produits bruts

function setupProductTable2(containerId, tableId,onChangeQuantity) {
  // On récupère l'élément conteneur à partir de son ID

  const container = document.getElementById(containerId);
  if (container) {

    // On ajoute un écouteur d'événements sur le conteneur pour détecter les changements de valeur dans les cases à cocher

    container.addEventListener('change', function(event) {
      if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {
        if (event.target.checked) {
    // Si la case à cocher est cochée, on ajoute le produit correspondant à la table des produits sélectionnés

          addProduct(event.target);
        } else {
          // Sinon, on supprime le produit correspondant de la table des produits sélectionnés
          removeProduct2(event.target.value);
        }
      }
    });
  }

  function addProduct(checkbox) {

    // On récupère le label correspondant à la case à cocher
    const productLabel = checkbox.parentNode.querySelector('label');
    
    // On récupère le nom, la quantité, le type de fer, la quantité en quintal et la quantité en barre du produit à partir des attributs data du label
    const productName = productLabel.textContent.trim();
    const quantite = productLabel.getAttribute('data-quantite');
    const producttyperfer = productLabel.getAttribute('data-type-fer');
    const quantite_quintal = productLabel.getAttribute('data-quintal');
    const quantite_barre = productLabel.getAttribute('data-barre');
    const pricequintal = productLabel.getAttribute('data-price-quintal');
    const productId = checkbox.value;
  
    // On crée un élément input pour le prix du produit en quintal
    const priceInput = document.createElement('input');
    priceInput.setAttribute('type', 'number');
    priceInput.setAttribute('step', '0.01');
    priceInput.setAttribute('name', `prix_brut_${productId}`);
    priceInput.setAttribute('id', `prix_brut_${productId}`);
    priceInput.value = pricequintal;
  
    // On récupère la table des produits sélectionnés
    const selectedProductsTable = document.getElementById(tableId);
  
    // On insère une nouvelle ligne pour le produit sélectionné
    const newRow = selectedProductsTable.insertRow();
    newRow.setAttribute('id', `product_brut_${productId}`);
    newRow.insertCell().textContent = productName;
    
    // On insère une cellule pour le prix en quintal du produit
    const priceCell = newRow.insertCell();
    priceCell.appendChild(priceInput);
 

  // On insère une cellule pour la quantité en kilogrammes du produit
const quantityCell = newRow.insertCell();
const quantityInput = document.createElement('input');
quantityInput.setAttribute('type', 'number');
quantityInput.setAttribute('step', '0.01');
quantityInput.setAttribute('name', `quantite_produit_brut_${productId}`);
quantityInput.setAttribute('id', `quantite_produit_brut_${productId}`);
quantityInput.value = quantite;
quantityCell.appendChild(quantityInput);

// On insère une cellule pour la quantité en quintal du produit
const quintalQuantityCell = newRow.insertCell();
const quintalQuantityInput = document.createElement('input');
quintalQuantityInput.setAttribute('type', 'number');
quintalQuantityInput.setAttribute('step', '0.01');
quintalQuantityInput.setAttribute('name', `quantite_quintal_produit_brut_${productId}`);
quintalQuantityInput.setAttribute('id', `quantite_quintal_produit_brut_${productId}`);
quintalQuantityInput.value = quantite_quintal;
quintalQuantityCell.appendChild(quintalQuantityInput);

// On insère une cellule pour la quantité en barres du produit
const barQuantityCell = newRow.insertCell();
const barQuantityInput = document.createElement('input');
barQuantityInput.setAttribute('type', 'number');
barQuantityInput.setAttribute('step', '1');
barQuantityInput.setAttribute('name', `quantite_barre_produit_brut_${productId}`);
barQuantityInput.setAttribute('id', `quantite_barre_produit_brut_${productId}`);
barQuantityInput.value = quantite_barre;
barQuantityCell.appendChild(barQuantityInput);

// On insère une cellule pour le prix total du produit
const totalPriceCell = newRow.insertCell();
totalPriceCell.setAttribute('id', `total_price_${productId}`);
totalPriceCell.setAttribute('step', '0.01');

  // On écoute les changements de la valeur de prix par quintal et on calcule le prix total en temps réel si la quantité en quintal est renseignée
priceInput.addEventListener('input', function() {
  if (quintalQuantityInput.value !== '') {
    const totalPriceCell = document.getElementById(`total_price_${productId}`);
    const totalPrice = (quintalQuantityInput.value * priceInput.value).toFixed(2);
    totalPriceCell.textContent = totalPrice;
  }
});

// On écoute les changements de la quantité en kilogrammes et on convertit les quantités en quintal et en barres en temps réel
quantityInput.addEventListener('input', function() {
  const convertedValues = convert_stock_metre(producttyperfer, quantityInput.value, quantityInput, quintalQuantityInput, barQuantityInput);
  quintalQuantityInput.value = convertedValues.stock_quintal;
  barQuantityInput.value = convertedValues.stock_barre;
  const totalPriceCell = document.getElementById(`total_price_${productId}`);
  const totalPrice = (quintalQuantityInput.value * priceInput.value).toFixed(2);
  totalPriceCell.textContent = totalPrice;
});

// On écoute les changements de la quantité en barres et on convertit les quantités en quintal et en kilogrammes en temps réel
barQuantityInput.addEventListener('input', function() {
  const convertedValues = convert_stock_barre(producttyperfer, barQuantityInput.value, quantityInput, quintalQuantityInput, barQuantityInput);
  const totalPriceCell = document.getElementById(`total_price_${productId}`);
  quintalQuantityInput.value = convertedValues.stock_quintal;
  quantityInput.value = convertedValues.stock_metre;
  const totalPrice = (quintalQuantityInput.value * priceInput.value).toFixed(2);
  totalPriceCell.textContent = totalPrice;
  onChangeQuantity(productId, barQuantityInput.value, totalPrice);
});

// On écoute les changements de la quantité en quintal et on convertit les quantités en kilogrammes et en barres en temps réel
quintalQuantityInput.addEventListener('input', function() {
  const totalPriceCell = document.getElementById(`total_price_${productId}`);
  const totalPrice = (quintalQuantityInput.value * priceInput.value).toFixed(2);
  totalPriceCell.textContent = totalPrice;
  const convertedValues = convert_stock_quintal(producttyperfer, quintalQuantityInput.value, quantityInput, quintalQuantityInput, barQuantityInput); 
  quantityInput.value = convertedValues.stock_metre;
  barQuantityInput.value = convertedValues.stock_barre;
  onChangeQuantity(productId, quintalQuantityInput.value, totalPrice);
});

  //Ce code calcule le prix total d'un produit, crée un bouton de suppression associé et ajoute un événement pour détecter les changements dans l'état de la case à cocher du produit. 
  //Il vérifie également si des cases à cocher sont déjà cochées et ajoute les produits correspondants à la liste.
 
  const totalPrice = quintalQuantityInput.value * priceInput.value;
  totalPriceCell.textContent = totalPrice.toFixed(2);

  const deleteCell = newRow.insertCell();
  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Supprimer';
  deleteButton.addEventListener('click', function() {
    removeProduct2(productId);
    checkbox.checked = false;
    
  });
  deleteCell.appendChild(deleteButton);

  checkbox.addEventListener('change', function() {
    if (!checkbox.checked) {
      removeProduct2(productId);
      
    }
  });
}
// Ajoute les lignes aux tableaux pour les cases cochés lorsque on ouvre la page
const checkboxes = container.querySelectorAll('input[type="checkbox"]:checked');
checkboxes.forEach(checkbox => {
  addProduct(checkbox);
 

});

// Permet de retirer le produit du tableau
function removeProduct2(productId) {
  const productRow = document.getElementById(`product_brut_${productId}`);
  if (productRow) {
    productRow.parentNode.removeChild(productRow);
    totalPrice2 = calculateTotalPrice(tableId);
    document.getElementById('id_Prix_total').value =  totalPrice2 + totalPrice1;
    triggerEvent(document.getElementById('id_Prix_total'), 'input');
      }
}



// Ecoute toutes les changements de type input et permet d'actualiser le Prix Total
document.getElementById(tableId).addEventListener('input', function() {
  totalPrice2 = calculateTotalPrice(tableId);
  // Modifier le code ici pour afficher la somme des prix totaux, par exemple :
  console.log(totalPrice2)
  document.getElementById('id_Prix_total').value =totalPrice2 + totalPrice1;
  triggerEvent(document.getElementById('id_Prix_total'), 'input');
  });
 
}


setupProductTable2('produits_brut_container', 'selected_products_brut_table', function(productId, quantity, totalPrice) {
});

function triggerEvent(element, eventName) {
  const event = new Event(eventName);
  element.dispatchEvent(event);
}

//fonction qui permet de gerer la case Vermeent Totalite
function updateVersementDetteValues() {
  const checkboxVersementTotalite = document.getElementById("id_Versement_totalite");
  const inputVersement = document.getElementById("id_Versement");
  const inputDette = document.getElementById("id_Dette");
  const prixTotal = document.getElementById("id_Prix_total").value;

  if (checkboxVersementTotalite.checked) {
    inputVersement.value = prixTotal;
    inputDette.value = "0";
  } else {
    document.getElementById('id_Versement').addEventListener("input",CalculDette)
  }
}

document.getElementById("id_Prix_total").addEventListener("input", updateVersementDetteValues);
document.getElementById("id_Versement_totalite").addEventListener("change", updateVersementDetteValues);


updateVersementDetteValues();


function forceUpdatePrixTotal() {
  const prixTotalInput = document.getElementById("id_Prix_total");
  const event = new Event("input");
  prixTotalInput.dispatchEvent(event);
}
   //Fonction qui permet de calculer la dette si la case versement totalite n'est pas caché 
        function CalculDette(){
          console.log("calcul dette");
          var inputVersement = document.getElementById('id_Versement');
          var inputDette = document.getElementById('id_Dette');
          var inputPrixTotal = document.getElementById('id_Prix_total');
         if(inputDette.value=inputPrixTotal.value-inputVersement.value<0){
          inputDette.value='Erreur'
         } 
         else{
          inputDette.value=inputPrixTotal.value-inputVersement.value
         }
        }
        //Fonction qui permet de faire la recherche pour produit Brut en utilisant Jquery 
        $(document).ready(function() {
          $('#searchBar1').on('input', function() {
            const searchTerm = $(this).val().toLowerCase();
            $('.produit_brut').each(function() {
              const labelText = $(this).find('label').text().toLowerCase();
              if (labelText.indexOf(searchTerm) !== -1) {
                $(this).show();
              } else {
                $(this).hide();
              }
            });
          });
        });
//Fonction qui permet de faire la recherche pour autre produit en utilisant Jquery
        $(document).ready(function() {
          $('#searchBar2').on('input', function() {
            const searchTerm = $(this).val().toLowerCase();
            $('.autre_produit').each(function() {
              const labelText = $(this).find('label').text().toLowerCase();
              if (labelText.indexOf(searchTerm) !== -1) {
                $(this).show();
              } else {
                $(this).hide();
              }
            });
          });
        });
       
        //Partie du code qui permet de ordonner les checkbox selon si ils sont coches(en avant du conteneut) et non (en arriere u conteneur)
        $('#autre_produits_container input[type="checkbox"]').on('change', function() {
          const container = $(this).closest('.autre_produit');
          if ($(this).is(':checked')) {
            container.prependTo('#autre_produits_container');
          } else {
            container.appendTo('#autre_produits_container');
          }
        });
        
        
        $('#produits_brut_container input[type="checkbox"]').on('change', function() {
          const container = $(this).closest('.produit_brut');
          if ($(this).is(':checked')) {
            container.prependTo('#produits_brut_container');
          } else {
            container.appendTo('#produits_brut_container');
          }
        });

      

//Fonction qui permet de faire les conversions quintaux,barre,metre
function convert_stock_quintal(typefer, stock_quintal, quantityInput, quintalQuantityInput, barQuantityInput) {
    console.log(typefer)
    if (stock_quintal != "") {
        if(typefer=="Fer /8"){
            var b= parseFloat(stock_quintal) * 20;
            var m = parseFloat(stock_quintal) * 240; //240
        }else if (typefer=="Fer /10"){
            var b= parseFloat(stock_quintal) * 12;
            var m = parseFloat(stock_quintal) * 144;//144
        }else if (typefer=="Fer /12"){
            var b= parseFloat(stock_quintal) * 9;
            var m = parseFloat(stock_quintal) * 108;// 108
        } else if (typefer=="Fer /14"){
            var b= parseFloat(stock_quintal) * 7;
            var m = parseFloat(stock_quintal) *84 ;//84
        }else if (typefer=="Fer /16"){
            var b= parseFloat(stock_quintal) * 5;
            var m = parseFloat(stock_quintal) *60 ;//60
        }else{
            var m = parseFloat(stock_quintal) * 1;
            var b= parseFloat(stock_quintal) * 1;
        }
        
        stock_metre= m.toFixed(2);
        stock_barre = b.toFixed(0);
    } else {
      stock_metre= "";
      stock_barre = "";

    }
    return { stock_metre, stock_barre };
}

function convert_stock_barre(typefer, stock_barre, quantityInput, quintalQuantityInput, barQuantityInput) {
  console.log(typefer)
  if (stock_barre != "") {
      if(typefer=="Fer /8"){
          var q= parseFloat(stock_barre) /20;
          var m = parseFloat(stock_barre)*12; //240
      }else if (typefer=="Fer /10"){
          var q= parseFloat(stock_barre) / 12;
          var m = parseFloat(stock_barre) *12;//144
      }else if (typefer=="Fer /12"){
          var q= parseFloat(stock_barre) / 9;
          var m = parseFloat(stock_barre) *12;// 108
      } else if (typefer=="Fer /14"){
          var q= parseFloat(stock_barre) / 7;
          var m = parseFloat(stock_barre) *12 ;//84
      }else if (typefer=="Fer /16"){
          var q= parseFloat(stock_barre) /5;
          var m = parseFloat(stock_barre) *12 ;//60
      }else{
          var q = parseFloat(stock_barre) / 1;
          var b= parseFloat(stock_barre) * 1;
      }
      
      stock_quintal= q.toFixed(2);
      stock_metre = m.toFixed(2);
  } else {
    stock_quintal= "";
    stock_metre = "";

  }
  return { stock_quintal, stock_metre};
}

function convert_stock_metre(typefer, stock_metre, quantityInput, quintalQuantityInput, barQuantityInput) {
  console.log(typefer)
  if (stock_metre != "") {
      if(typefer=="Fer /8"){
          var q= parseFloat(stock_metre) /240;
          var b = parseFloat(stock_metre) /12; //240
      }else if (typefer=="Fer /10"){
          var q= parseFloat(stock_metre) /144;
          var b = parseFloat(stock_metre) /12;//144
      }else if (typefer=="Fer /12"){
          var q= parseFloat(stock_metre) /108;
          var b = parseFloat(stock_metre) /12;// 108
      } else if (typefer=="Fer /14"){
          var q= parseFloat(stock_metre) /84;
          var b = parseFloat(stock_metre) /12 ;//84
      }else if (typefer=="Fer /16"){
          var q= parseFloat(stock_metre) /60;
          var b = parseFloat(stock_metre) /12 ;//60
      }else{
          var q = parseFloat(stock_metre) / 1;
          var b= parseFloat(stock_metre) / 1;
      }
      
      stock_quintal= q.toFixed(2);
      stock_barre = b.toFixed(0);
  } else {
    stock_quintal= "";
    stock_barre = "";

  }
  return { stock_quintal, stock_barre };
}


