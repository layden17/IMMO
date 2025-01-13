#include "Urne.hpp"
#include "Scrutin.hpp"

unsigned int Urne::NB=0;
Urne::Urne (const Scrutin & x): scrutin{x},n{NB++},resultats(x.getNbOption(),0){}

Urne::Urne(){ cout << "destruction de l'urne " << n << endl;}

Urne::voter(int choix){

    this.resultats


}