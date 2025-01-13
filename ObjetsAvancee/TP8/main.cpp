#include <iostream>
#include "Vecteur.hpp"
using namespace std;

int main(){
    Vecteur AB (-2,3,4,5);
    //Vecteur AB (6,2);
    Vecteur CD (6,2);
    Vecteur resultat = AB + CD;
    //cout << "Résultat de l'addition : " << resultat.getX() << ", " << resultat.getY() << endl;
    cout << "Les vecteurs sont-ils egaux ?  : " << (AB==resultat)<< endl;
    cout << AB << endl;
    return 0;
}