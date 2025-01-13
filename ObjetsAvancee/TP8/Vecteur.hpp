#ifndef VECTEUR_H
#define VECTEUR_H

#include <string>
#include <vector>
#include<iostream>
using namespace std;


class Vecteur{
    private : 
        int x,y;
       
    public:
        Vecteur(int x_a, int y_a,int x_b, int y_b);
        Vecteur(int abs, int ord);
        Vecteur();
        virtual ~ Vecteur() = default;
        bool operator==(const Vecteur& v) const;
        bool operator!=(const Vecteur&)const ;
        Vecteur operator+(const Vecteur&)const;
        Vecteur operator-(const Vecteur&)const;
        Vecteur& operator*(const Vecteur&)const;
        int getX() const ;
        int getY() const ;
        friend std::ostream& operator<<(std::ostream& os, const Vecteur& v);

};

#endif