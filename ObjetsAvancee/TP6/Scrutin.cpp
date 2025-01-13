#include "Scrutin.hpp"


Scrutin::~Scrutin(){
    for (Urne * x : urnes) delete x;
}

unsigned int getNbOpt() const {return nbOpt;}

Scrutin::Scrutin (unsigned int nbU, unsigned int nbO) :  nbUrnes{nbU},nbOption{nbO} {
    for (int i=0;i<nbU;i+1)
        urnes.push_back(new Urne{*this});
}