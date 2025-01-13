var longueurInput = document.getElementById("id_longueur");
var largeurInput = document.getElementById("id_largeur");
var prixServiceInput = document.getElementById("id_prix_service");
var crochetInput = document.getElementById("id_crochet_opti");



//fonction qui charge les données qui viennent de produit brut
function updateStockInputs() {
    const selectedOption = produitSelect.options[produitSelect.selectedIndex];
    stock_quintalInput.value = selectedOption.dataset.stock_quintal;
    stock_barreInput.value = selectedOption.dataset.stock_barre;
    stock_metreInput.value = selectedOption.dataset.stock_metre;
}


//fonction qui calcul l'otimisation en réduisant le crochet
function optimal(consommation_sans_chute, consommation,crochet, chute, max, prix_service) {
    var prix_quintal = document.getElementById("id_prix_quntal").value ;
    var nb_barre = document.getElementById("id_nombre_barre").value ;

//si la chute = 0 pas besoin d'optimiser ,  la taille minimal du crochet est 7
    if((chute != 0.00  || chute != 0) && crochet>7){
        var maxOPTI = max;
        var consomOPTI=consommation;
        var limite_Crochet = (Math.abs(7 - crochet)) / 100;

        for (let x = consommation_sans_chute ; x >= consommation_sans_chute-limite_Crochet; x -= 0.01) {
            let y = 12 / x;
            if (Math.trunc(y) > maxOPTI) {
                maxOPTI =Math.trunc(y) ;
                consomOPTI = x;
            }
        }
        var prix_metre = (prix_quintal /nb_barre)/12;
        prix_metre = prix_metre.toFixed(2)
        var prix_total =  prix_metre* consomOPTI + prix_service;
        document.getElementById("id_consommation_sans_chute").value =consommation_sans_chute.toFixed(2);
        document.getElementById("id_consommation").value = consomOPTI.toFixed(2);

        document.getElementById("id_chute_valeur").value = 0.00;
        document.getElementById("id_max").value =maxOPTI.toFixed(2);
        document.getElementById("id_prix").value =prix_total.toFixed(2);

        var crochetOPTI = crochet - ((consommation_sans_chute - consomOPTI)*100);
        if(crochet < crochetOPTI){
            document.getElementById("id_crochet").value = crochet;
        }else{
            document.getElementById("id_crochet").value = crochetOPTI.toFixed(2);
        }

    }
}

//fonction qui attribue les valeurs
function appliquer(consommation_sans_chute, consommation,crochet, chute, max, prix_total){
    document.getElementById("id_consommation_sans_chute").value = consommation_sans_chute.toFixed(2);
    document.getElementById("id_consommation").value = consommation.toFixed(2);
    document.getElementById("id_chute_valeur").value = chute.toFixed(2);
    document.getElementById("id_max").value = max.toFixed(2);
    document.getElementById("id_prix").value = prix_total.toFixed(2);
    document.getElementById("id_crochet").value =  0;
}

//fonction applicable que pour fer6
function fer6_application(consommation_sans_chute, consommation){
    var stock_metre = document.getElementById("id_stock_metre").value;
    document.getElementById("id_consommation_sans_chute").value = consommation_sans_chute.toFixed(2);
    document.getElementById("id_consommation").value = consommation.toFixed(2);
    document.getElementById("id_chute_valeur").value = 0;
    var prix_metre = document.getElementById("id_prix_metre").value;
    var max_fer6 = stock_metre/  consommation_sans_chute;
    document.getElementById("id_max").value = Math.trunc(max_fer6);

    var prix_fer6 = prix_metre* consommation_sans_chute;
    document.getElementById("id_prix").value =prix_fer6.toFixed(2);
}

//fonction applicable que pour fer6
function cache_prix_fer() {
    var prix_metre_div = document.getElementById("id_prix_metre").parentNode;

    var bar = document.getElementById("id_produit");
    var selectedOption = bar.options[bar.selectedIndex];
    var designation = selectedOption.innerHTML;
    var diametre_bar = designation.split("/")[1];

    // Si la case à cocher est cochée, afficher le champ
    if (diametre_bar === "6") {
        prix_metre_div.style.display = "block";
    } else {
        prix_metre_div.style.display = "none"; // réinitialiser l'affichage
    }
}


//fonction qui permet de calculer les couts selon la longueur, largeur, prix_service, crochet
function calculerResultat() {
    //je recupere le produit ensuite je splite pour avoir le diametre
    var bar = document.getElementById("id_produit");
    var selectedOption = bar.options[bar.selectedIndex];
    var designation = selectedOption.innerHTML;
    var diametre_bar = designation.split("/")[1];

    var prix_quintal = document.getElementById("id_prix_quntal").value ;
    var nb_barre = document.getElementById("id_nombre_barre").value ;
    var forme = document.getElementById("id_cadre_choix").value;

    var longueur = parseFloat(longueurInput.value);
    var largeur = parseFloat(largeurInput.value);
    var prix_service = parseFloat(prixServiceInput.value);
    var crochet = parseFloat(crochetInput.value);
    var bar_12 = 12;
    var maCase = document.getElementById("id_chute");
    var prix_metre = (prix_quintal /nb_barre)/12;
    prix_metre = prix_metre.toFixed(2)
    if (forme === "Cadre") {
        var consommation_sans_chute = ((2 * (longueur +largeur))+ crochet) /100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Octogone"){
        var consommation_sans_chute = (((4*longueur) + (4*largeur)) + crochet) /100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;

        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Hexagon"){
        var consommation_sans_chute = ((2*longueur) + (4*largeur) + crochet)/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Losange"){
        var consommation_sans_chute = ((4*longueur)  + crochet)/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Epingle"){
        var consommation_sans_chute = ((longueur)*2 + crochet)/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Crochet"){
        var consommation_sans_chute = ((longueur)  + crochet)/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Higes"){
        var consommation_sans_chute = ((longueur))/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Senelle"){
        var consommation_sans_chute = ((longueur)+ crochet)/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }

    }else if(forme === "Fiche Poteau"){
        var consommation_sans_chute = ((longueur + largeur))/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }


    }else if(forme === "S"){
        var consommation_sans_chute = ((2*longueur) + (largeur))/100;
        var prix_total =  prix_metre* consommation_sans_chute + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;


        if(maCase.checked){
            if(diametre_bar != '6') {
                optimal(consommation_sans_chute, consommation, crochet, chute, max, prix_service);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }else{
            if(diametre_bar != '6'){
                appliquer(consommation_sans_chute,consommation,crochet,chute,max,prix_total);
            }else{
                fer6_application(consommation_sans_chute, consommation);
            }
        }
    }
}


//fonction qui affiche l'image selon le choix du cadre
function afficherImage(){

    var forme = document.getElementById("id_cadre_choix").value;
    var image_cadre = document.getElementById("image_cadre");

    if (forme === "Cadre") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/carre.png";
        img.alt = "Cadre";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Octogone") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/octogone.png";
        img.alt = "Octogone";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Hexagon") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/hexagone.png";
        img.alt = "Hexagone";
        image_cadre.appendChild(img);
    }else if (forme === "Losange") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/losange.png";
        img.alt = "Losange";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Epingle") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/epingle.png";
        img.alt = "Epingle";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Crochet") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/crochet.png";
        img.alt = "Crochet";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Higes") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/higes.png";
        img.alt = "Higes";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Senelle") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/senelle.png";
        img.alt = "Senelle";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "Fiche Poteau") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/fiche_poteau.png";
        img.alt = "Fiche poteau";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else if (forme === "S") {
        image_cadre.innerHTML = "";
        var img = document.createElement("img");
        img.src = "/static/images/s.png";
        img.alt = "S";
        image_cadre.innerHTML = "";
        image_cadre.appendChild(img);
    } else {
        image_cadre.innerHTML = "";
    }
}

//fonction qui permet de mettre à jour les données en fonction du choix de Forme,  Produit et affiche les images
function event_form() {
    updateStockInputs();
    calculerResultat();
    afficherImage();
}
//fonction qui permet de mettre à jour les données en fonction du choix de Forme,  Produit
function event_checkbox() {
    updateStockInputs();
    calculerResultat();
}
//fonction qui permet de mettre à jour les données en fonction du choix de Forme,  Produit
function event_produit() {
    updateStockInputs();
    calculerResultat();
    cache_prix_fer();
}