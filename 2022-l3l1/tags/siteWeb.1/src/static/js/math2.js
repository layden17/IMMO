var longueurInput = document.getElementById("id_longueur");
var largeurInput = document.getElementById("id_largeur");
var prixServiceInput = document.getElementById("id_prix_service");
var crochetInput = document.getElementById("id_crochet");
var resultatSpan = document.getElementById("resultat");
//var bar = document.getElementById("id_article_choix").value;
//var taille_bar = bar.toString().split('/')[1];

function optimal(consommation_sans_chute, consommation, chute, max, prix_service) {
    var maxOPTI = max;
    var consomOPTI=consommation;
    for (let x = consommation_sans_chute ; x >= consommation_sans_chute-0.03; x -= 0.01) {
        let y = 12 / x;
        if (Math.trunc(y) > maxOPTI) {
            maxOPTI =Math.trunc(y) ;
            consomOPTI = x;
        }
    }
    var prix = 12000 * ((consomOPTI)/240) + prix_service ;

    document.getElementById("id_consommation_sans_chute").value =consommation_sans_chute.toFixed(2);
    document.getElementById("id_consommation").value = consomOPTI.toFixed(2);
    document.getElementById("id_chute_valeur").value = 0.00;
    document.getElementById("id_max").value =maxOPTI.toFixed(2);
    document.getElementById("id_prix").value =prix.toFixed(2);
}

function appliquer(consommation_sans_chute, consommation, chute, max, prix_total){
    document.getElementById("id_consommation_sans_chute").value = consommation_sans_chute.toFixed(2);
    document.getElementById("id_consommation").value = consommation.toFixed(2);
    document.getElementById("id_chute_valeur").value = chute.toFixed(2);
    document.getElementById("id_max").value = max.toFixed(2);
    document.getElementById("id_prix").value = prix_total.toFixed(2);
}


function calculerResultat() {

    var forme = document.getElementById("id_cadre_choix").value;
    var bar = document.getElementById("id_article_choix").value;

    var longueur = parseFloat(longueurInput.value);
    var largeur = parseFloat(largeurInput.value);
    var prix_service = parseFloat(prixServiceInput.value);
    var crochet = parseFloat(crochetInput.value);
    var bar_12 = 12;

    var maCase = document.getElementById("id_chute");


    if (forme === "Cadre") {
        var taille_bar = bar.toString().split('/')[1];
        var consommation_sans_chute = ((2 * (longueur +largeur))+ crochet) /100;

        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }




    }else if(forme === "Octogone"){
        var consommation_sans_chute = (((4*longueur) + (4*largeur)) + crochet) /100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;

        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Hexagone"){
        var consommation_sans_chute = ((2*longueur) + (4*largeur) + crochet)/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;

        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Losange"){
        var consommation_sans_chute = ((4*longueur)  + crochet)/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;

        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }

    }else if(forme === "Epingle"){
        var consommation_sans_chute = ((longueur)*2 + crochet)/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Crochet"){
        var consommation_sans_chute = ((longueur)  + crochet)/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Higes"){
        var consommation_sans_chute = ((longueur))/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Senelle"){
        var consommation_sans_chute = ((longueur)+ crochet)/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }else if(forme === "Fiche Poteau"){
        var consommation_sans_chute = ((longueur + largeur))/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service ;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }

    }else if(forme === "S"){
        var consommation_sans_chute = ((2*longueur) + (largeur))/100;
        var prix = 12000 * ((consommation_sans_chute)/240) + prix_service;
        let max = Math.trunc((bar_12 /consommation_sans_chute)) ;
        var consommation = bar_12 /max ;
        var chute = (bar_12 /consommation_sans_chute) - max;
        if(maCase.checked){
            optimal(consommation_sans_chute, consommation, chute, max, prix_service);
        }else{
            appliquer(consommation_sans_chute,consommation,chute,max,prix);
        }
    }
}



