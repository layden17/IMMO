
function dessiner() {
    var canvas = document.getElementById("canvas");
    var contexte = canvas.getContext("2d");

    var forme = document.getElementById("id_cadre_choix").value;

    contexte.clearRect(0, 0, canvas.width, canvas.height);

    if (forme === "Cadre") {
        var x = 50;
        var y = 50;
        var largeur = 100;
        var hauteur = 100;
        contexte.fillStyle = "#FF0000";
        contexte.fillRect(x, y, largeur, hauteur);
        var dimensions = "Largeur : " + largeur + "px, Hauteur : " + hauteur + "px";
        document.getElementById("dimensions").innerHTML = dimensions;
    } else if (forme === "Octogone") {
        var x = 30;
        var y = 60;
        var largeur = 140;
        var hauteur = 80;
        contexte.fillStyle = "#FF0000";
        contexte.fillRect(x, y, largeur, hauteur);
        var dimensions = "Largeur : " + largeur + "px, Hauteur : " + hauteur + "px";
        document.getElementById("dimensions").innerHTML = dimensions;
    }else if (forme === "Hexagone") {
        var x = 100;
        var y = 100;
        var size = 50;
        contexte.beginPath();
        contexte.moveTo(x + size * Math.cos(0), y + size * Math.sin(0));
        for (var i = 1; i <= 6; i++) {
            contexte.lineTo(x + size * Math.cos(i * 2 * Math.PI / 6), y + size * Math.sin(i * 2 * Math.PI / 6));
        }
        contexte.fillStyle = "#FF0000";
        contexte.fill();
        contexte.closePath();

        var dimensions = "Taille : " + size + "px";
        document.getElementById("dimensions").innerHTML = dimensions;
    }else if (forme === "Losange") {
        var x = 100;
        var y = 100;
        var size = 50;
        contexte.beginPath();
        contexte.moveTo(x, y - size);
        contexte.lineTo(x + size, y);
        contexte.lineTo(x, y + size);
        contexte.lineTo(x - size, y);
        contexte.fillStyle = "#FF0000";
        contexte.fill();
        contexte.closePath();

        var dimensions = "Taille : " + size + "px";
        document.getElementById("dimensions").innerHTML = dimensions;
    }else if (forme === "Epingle") {
        var x = 100;
        var y = 100;
        var rayon = 40;
        var longueur = 60;

        contexte.beginPath();
        contexte.arc(x, y - rayon, rayon, 0, Math.PI, false);
        contexte.lineTo(x, y);
        contexte.closePath();

        contexte.moveTo(x, y);
        contexte.lineTo(x, y + longueur);

        contexte.lineTo(x - 10, y + longueur - 10);
        contexte.moveTo(x, y + longueur);
        contexte.lineTo(x + 10, y + longueur - 10);

        contexte.fillStyle = "#F00"; // rouge

        contexte.fill();
        contexte.closePath();
    }else if (forme === "Crochet") {
        var x = 100;
        var y = 100;
        var size = 50;

        contexte.beginPath();
        contexte.moveTo(x, y);
        contexte.lineTo(x + size/2, y - size/2);
        contexte.lineTo(x + size/2, y - size);
        contexte.lineTo(x + size/4, y - size);
        contexte.lineTo(x + size/4, y - size/2);
        contexte.lineTo(x - size/4, y - size/2);
        contexte.lineTo(x - size/4, y - size);
        contexte.lineTo(x - size/2, y - size);
        contexte.lineTo(x - size/2, y - size/2);
        contexte.lineTo(x, y);
        contexte.fillStyle = "#FF0000";
        contexte.fill();
        contexte.closePath();

        var dimensions = "Taille : " + size + "px";
        document.getElementById("dimensions").innerHTML = dimensions;
    }


}


