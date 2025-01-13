var longueurInput = document.getElementById("id_longueur");
var largeurInput = document.getElementById("id_largeur");
var prixServiceInput = document.getElementById("id_prix_service");
var crochetInput = document.getElementById("id_crochet");
var resultatSpan = document.getElementById("resultat");


function calculerResultat() {
    var forme = document.getElementById("id_cadre_choix").value;
    var bar = document.getElementById("id_article_choix").value;
    var nombre = bar.toString().split('/')[1];
    var longueur = parseFloat(longueurInput.value);
    var largeur = parseFloat(largeurInput.value);
    var prix_service = parseFloat(prixServiceInput.value);
    var crochet = parseFloat(crochetInput.value);



    if (forme === "Cadre") {
        var consommation = ((2 * (longueur +largeur))+ crochet) /100;
        var prix = 12000 * (consommation)/240 + prix_service ;
        var quintal = 240;
        var max = nombre /consommation;

        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + max + " <br>" ;
    }else if(forme === "Octogone"){
        var consommation = ((4*longueur) + (4*largeur)) + crochet;
        var prix = consommation/2;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Hexagone"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Losange"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Crochet"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Higes"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Senelle"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "Fiche Poteau"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }else if(forme === "S"){
        var consommation = (2*longueur) + (2*largeur) + crochet;
        var prix = longueur + largeur + prix_service + crochet;
        resultatSpan.innerHTML = "Prix (DA): " + prix + "<br>" +
            "Consommation sans chute (m): " + consommation/100 + "<br>" +
            "Consommation (m): " + " <br>" +
            "Chute (m): " + " <br>" +
            "Max : " + " <br>" ;
    }
}

longueurInput.addEventListener("input", calculerResultat);
largeurInput.addEventListener("input", calculerResultat);
prixServiceInput.addEventListener("input", calculerResultat);
crochetInput.addEventListener("input", calculerResultat);

