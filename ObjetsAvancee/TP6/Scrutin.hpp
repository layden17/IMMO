#ifndef SCRUTIN_H
#define SCRUNTIN_H

#include <string>
#include <vector>
#include<iostream>
#include"Urne.hpp"
using namespace std;


class Scrutin{
    private : 
        const int unsigned nbUrnes;
        const int unsigned nbOption;
        vector<Urne *> urnes;
    public:
        Scrutin(unsigned int nbU, unsigned int nbO);
        virtual ~ Scrutin();
        Scrutin (const & Scrutin)=delete;
        Scrutin& operator=(const Scrutin&)=delete;
        unsigned int getNbOption() const;

}

#endif