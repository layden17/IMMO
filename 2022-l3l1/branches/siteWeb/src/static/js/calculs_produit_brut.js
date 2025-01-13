



function convert_prix_vente() {
    var pv_quintal = document.getElementById("id_prix_quintal").value;
    var type_fer=document.getElementById("id_type_fer").value;

    if (pv_quintal != "" ) {
        if(type_fer=="Fer /8"){
            var m = parseFloat(pv_quintal) / 240;
            var b= parseFloat(pv_quintal) / 20;
        }else if (type_fer=="Fer /10"){
            var m = parseFloat(pv_quintal) / 144;
            var b= parseFloat(pv_quintal) / 12;
        }else if (type_fer=="Fer /12"){
            var m = parseFloat(pv_quintal) / 12;
            var b= parseFloat(pv_quintal) /9;
        } else if (type_fer=="Fer /14"){
            var m = parseFloat(pv_quintal) / 84;
            var b= parseFloat(pv_quintal) / 7;
        }else if (type_fer=="Fer /16"){
            var m = parseFloat(pv_quintal) /60;
            var b= parseFloat(pv_quintal) / 5;
        }else{
            var m = parseFloat(pv_quintal) / 1;
            var b= parseFloat(pv_quintal) /1;
        }
        
        document.getElementById("id_prix_metre").value = m.toFixed(2);
        document.getElementById("id_prix_barre").value = b.toFixed(2);
    } else {
        document.getElementById("id_prix_metre").value = "";
        document.getElementById("id_prix_barre").value = "";

    }
}


function convert_prix_achat() {
    var pa_quintal = document.getElementById("id_prix_achat_quintal").value;
    var type_fer=document.getElementById("id_type_fer").value;

    if (pa_quintal != "" ) {
        if(type_fer=="Fer /8"){
            var m = parseFloat(pa_quintal) / 240;
            var b= parseFloat(pa_quintal) / 20;
        }else if (type_fer=="Fer /10"){
            var m = parseFloat(pa_quintal) / 144;
            var b= parseFloat(pa_quintal) / 12;
        }else if (type_fer=="Fer /12"){
            var m = parseFloat(pa_quintal) / 12;
            var b= parseFloat(pa_quintal) /9;
        } else if (type_fer=="Fer /14"){
            var m = parseFloat(pa_quintal) / 84;
            var b= parseFloat(pa_quintal) / 7;
        }else if (type_fer=="Fer /16"){
            var m = parseFloat(pa_quintal) /60;
            var b= parseFloat(pa_quintal) / 5;
        }else{
            var m = parseFloat(pa_quintal) / 1;
            var b= parseFloat(pa_quintal) /1;
        }
        
        document.getElementById("id_prix_achat_metre").value = m.toFixed(2);
        document.getElementById("id_prix_achat_barre").value = b.toFixed(2);
    } else {
        document.getElementById("id_prix_achat_metre").value = "";
        document.getElementById("id_prix_achat_barre").value = "";

    }
}


function convert_stock() {
    var stock_quintal = document.getElementById("id_stock_quintal").value;
    var type_fer=document.getElementById("id_type_fer").value;

    if (stock_quintal != "") {
        if(type_fer=="Fer /8"){
            var b= parseFloat(stock_quintal) * 20;
            var m = parseFloat(stock_quintal) * b*12; //240
        }else if (type_fer=="Fer /10"){
            var b= parseFloat(stock_quintal) * 12;
            var m = parseFloat(stock_quintal) * b*12;//144
        }else if (type_fer=="Fer /12"){
            var b= parseFloat(stock_quintal) * 9;
            var m = parseFloat(stock_quintal) * b*12;// 108
        } else if (type_fer=="Fer /14"){
            var b= parseFloat(stock_quintal) * 7;
            var m = parseFloat(stock_quintal) *b*12 ;//84
        }else if (type_fer=="Fer /16"){
            var b= parseFloat(stock_quintal) * 5;
            var m = parseFloat(stock_quintal) *b*12 ;//60
        }else{
            var m = parseFloat(stock_quintal) * 1;
            var b= parseFloat(stock_quintal) * 1;
        }
        
        document.getElementById("id_stock_metre").value = m.toFixed(2);
        document.getElementById("id_stock_barre").value = b.toFixed(2);
    } else {
        document.getElementById("id_stock_metre").value = "";
        document.getElementById("id_stock_barre").value = "";

    }
}

     