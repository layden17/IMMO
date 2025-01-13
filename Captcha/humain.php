<?php 

//global $lang = "fr";

function RandomImage($dbname){

    $db = new PDO('mysql:host=sqlprive-dn717-001.privatesql;dbname=captcha','captcha_L2E2_us', 'QDy54vZua4U8');
    $requete = $db->query("SELECT id_image FROM `image` WHERE deja_valide = 0 ORDER BY rand() LIMIT 1");
    $randImage = array();
    while(false != ($result = $requete->fetch(PDO::FETCH_ASSOC)))
    {
        $randImage[] = $result['id_image'];
    }
    $r = $randImage[0];
    return $r;
}

function RandomQuestion($dbname){

    if(isset($_POST['valider1'])){
        if(!empty($_POST['langue'])) {
            $choixLangue = $_POST['langue'];
        } 
        else {
            echo 'Please select the value.';
        }
    }

    global $consigne,$name_button;
	$lang = "$choixLangue" ;

    switch ($choixLangue) {
        
        case 'en':
            $min = 11 ; /*creation de variables pour la fonction random*/
            $max = 20;
            $consigne = "Choose a single box, associate it with the right question then validate.";
            $name_button = "CONFIRM";
            break;
        case 'ch':
            $min = 21 ; /*creation de variables pour la fonction random*/
            $max = 30;
            $consigne = "选择一个框，将其与正确的问题相关联，然后验证。";
            $name_button = "验证";
            break;
        case 'fr':
            $min = 1 ; /*creation de variables pour la fonction random*/
            $max = 10;
            $consigne = "Choisir une seule case, l'associer à la bonne question puis valider.";
            $name_button = "VALIDER";
            break;
        default:
            $min = 1 ; /*creation de variables pour la fonction random*/
            $max = 10;
            $consigne = "Choisir une seule case, l'associer à la bonne question puis valider.";
            $name_button = "VALIDER";
            break;
    }

    $user= 'root';
    $tab_int = array();/*creation d'un tableau vide permettant d'eviter les doublons*/
    $tab_q = array();
    $tab_id = array();



    try{
        $db = new PDO('mysql:host=sqlprive-dn717-001.privatesql;dbname=captcha','captcha_L2E2_us', 'QDy54vZua4U8');//comande de connection à la BDD phpmyadmin
            
        for ($i=0;$i<5;$i++){//boucle pour les 5 questions à afficher
                
            do{
                $aleatoire= rand($min,$max);
            }while(in_array($aleatoire, $tab_int));//teste evitant les doublons
            
            foreach($db->query('SELECT * FROM `question` where id_question ='.$aleatoire.'')as $row)//requete sql pour cherhcer le libelle de la question associé au numero aléatoire

            array_push($tab_int,$aleatoire);//ajout du numero déjà affiché pour éviter les doublons
            array_push($tab_q,$row['libelle']);
            array_push($tab_id,$row['id_question']);

        }
        global $id_1,$id_2,$id_3,$id_4,$id_5;
        list($id_1,$id_2,$id_3,$id_4,$id_5)= $tab_id;
        
        return $tab_q;
                    
    }
    catch (PDOException $e){
        print "Erreur : " . $e->getMessage()."<br/r>";//teste arretant et affichant un message d'erreur si la connexion à la BDD est un échec
        die;
    }
}

//Execution des fonctions
$r = RandomImage("captcha");
list($q1,$q2,$q3,$q4,$q5) = RandomQuestion("captcha");
?>


<!DOCTYPE html>
<html lang="fr">
<style>
    .meme_hauteur {
    height: 100px;
    width: 100px;
    }
</style>
<head>
    <meta charset="UTF-8">
    <title>Projet Captcha</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<form action= "" method="post" class="langues">
        <bloc>
            <input id ="langue_francais" type="radio" name="langue" class="leslangues" value="fr"><label for ="langue_francais"><img src="fr.png" alt="image" class="drapeau"></label>
        </bloc>
        
        <bloc>
             <input id ="langue_anglais" type="radio" name="langue" class="leslangues" value="en"><label for ="langue_anglais"><img src="uk.png" alt="image" class="drapeau"></label>
        </bloc>
        
        
        <bloc>
            <input id ="langue_chinois" type="radio" name="langue" class="leslangues" value="ch"><label for ="langue_chinois"><img src="ch.png" alt="image" class="drapeau"></label>
        </bloc>
        
        <bloc>
           <button class="slide" type="sumbit" name="valider1">✔</button>
        </bloc>
</form>

<form action="" method="post" class="myForm">
            <bloc>
                <input type="radio" id="case1" name="unecase" class = "cases" value="1"/><label for ="case1"><img src=<?php echo "./images/c-$r/1_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        
            <bloc>
                <input type="radio" id="case2" name="unecase" class="cases" value="2"/><label for ="case2"> <img src=<?php echo "./images/c-$r/2_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        
            <bloc>
                <input type="radio" id="case3" name="unecase" class="cases" value="3" /><label for ="case3"><img src=<?php echo "./images/c-$r/3_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        <br>
        
            <bloc>
                <input type="radio" id="case4" name="unecase" class="cases" value="4"/><label for ="case4"> <img src=<?php echo "./images/c-$r/4_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>

        
            <bloc>
                <input type="radio" id="case5" name="unecase" class="cases" value="5"/><label for ="case5"><img src=<?php echo "./images/c-$r/5_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        
            <bloc>
                <input type="radio" id="case6" name="unecase" class="cases" value="6"/><label for ="case6"> <img src=<?php echo "./images/c-$r/6_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        <br>
        
            <bloc>
                <input type="radio" id="case7" name="unecase" class="cases" value="7"/><label for ="case7"><img src=<?php echo "./images/c-$r/7_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        
            <bloc>
                <input type="radio" id="case8" name="unecase" class="cases" value="8"/><label for ="case8"><img src=<?php echo "./images/c-$r/8_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>
        
        
            <bloc>
                <input type="radio" id="case9" name="unecase" class="cases" value="9"/><label for ="case9"> <img src=<?php echo "./images/c-$r/9_$r.png"; ?> alt="image" class="meme_hauteur"></label>
            </bloc>

            <input type="HIDDEN" name="id_image" value="<?php echo $r; ?>">
 
        <script language="javascript">
        //Afficher l'image au passage de la souri
        function showPic(e,sUrl){
            var x,y;
            x = e.clientX;
            y = e.clientY; //coordonnées de la souris
            document.getElementById("layer").style.left = x+(-500)+'px';
            document.getElementById("layer").style.top = y+(-100)+'px'; //Affichez l'image et la souris à une certaine distance pour éviter le scintillement
            document.getElementById("layer").innerHTML = "<img border='0' src=\"" + sUrl + "\">";
            document.getElementById("layer").style.display = "";
        }
        function hiddenPic(){ //fermer l'image
            document.getElementById("layer").innerHTML = "";
            document.getElementById("layer").style.display = "none";
        }
        </script>
        <!--Aide_end -->
        <!--Suntanqing_Aide version0.01 13/3/2022-->
        <div id="layer"  style="display: inline; position: absolute; z-index:15;">
        </div>
        <p>
		<img src="question_mark.png" onmouseout="hiddenPic();" onmousemove="showPic(event,'help/WhyShowUp_'+'<?php echo "$lang" ; ?>'+'.jpg');">
		<!--Pourquoi exist Captcha?-->
		<a href onclick=location.reload([bForceGet])><img src="refresh.png"></a>
		<!--Refresh-->

        </p>
        <!--Aide_end-->

    <div class = "question">
                <span class="consigne"><?php echo nl2br($consigne."\n\n"); ?></span>
                <input type="radio" name="question" value= <?php echo $id_1 ; ?> > <?php echo $q1 ; ?><br /><br />
                <input type="radio" name="question" value= <?php echo $id_2 ; ?> > <?php echo $q2 ; ?><br /><br />
                <input type="radio" name="question" value= <?php echo $id_3 ; ?> > <?php echo $q3 ; ?><br /><br />
                <input type="radio" name="question" value= <?php echo $id_4 ; ?> > <?php echo $q4 ; ?><br /><br />
                <input type="radio" name="question" value= <?php echo $id_5 ; ?> > <?php echo $q5 ; ?><br /><br />
    </div>

                <input type="submit" name="submit" id="cb" class="cb" class="boutonValider" value=<?php echo $name_button ; ?>>
    
</form>

<div class ="logo">
    <img src="LOMS.png">
</div>

<?php
    if(isset($_POST['submit'])){
    if( !empty($_POST['question']) AND !empty($_POST['unecase']) AND !empty($_POST['id_image'])) { //AND !empty($_POST['case'])
            $Q = $_POST['question'];
            $C = $_POST['unecase'];
            $I = $_POST['id_image'];
            echo ' Question :  ' . $Q. "<br>"."Case : " .$C. "<br>"."Image : " .$I;
            echo "humain";
            $db = new PDO('mysql:host=sqlprive-dn717-001.privatesql;dbname=captcha','captcha_L2E2_us', 'QDy54vZua4U8');
            $result = $db->query('SELECT fois_selection FROM case_question WHERE (id_image = '.$I.' AND id_question = '.$Q.' AND id_case = '.$C.')');
            $req = $result->fetchall();
            //insertion des lien case question dans bdd
            if (!empty($req[0][0])) {
                $incremente = $req[0][0] + 1;
                $update = $db->query('UPDATE case_question SET fois_selection = '.$incremente.' WHERE (id_image = '.$I.' AND id_question = '.$Q.' AND id_case = '.$C.')');
                if ($incremente >= 20){
                    $update = $db->query('UPDATE image SET deja_valide = 1 WHERE (id_image = '.$I.')');
                    for($i = 1 ; $i<=9 ; $i++){
                        for($j=1 ; $j<=10 ; $j++){
                            $result = $db->query('SELECT fois_selection FROM case_question WHERE (id_image = '.$I.' AND id_question = '.$j.' AND id_case = '.$i.')');
                            $req = $result->fetchall();
                            if (!empty($req[0][0])) {
                                if ($req[0][0] >= 10){
                                    $update = $db->query('UPDATE case_question SET valide = 1 WHERE (id_image = '.$I.' AND id_question = '.$j.' AND id_case = '.$i.')');
                                }
                            }
                            else{
                                $insertion = $db->query('INSERT INTO case_question VALUES (NULL, '.$I.', '.$j.','.$i.', 0, 0, 0)');
                            }
                        }
                    }
                }
            }   
            else {
                $insertion = $db->query('INSERT INTO case_question VALUES (NULL, '.$I.', '.$Q.','.$C.', 0, 1, 0)');
            }
        }
    else {
        echo 'Please select the value.';
    }
    }
?>

</body>
</html>