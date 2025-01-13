#include "Vecteur.hpp"

Vecteur::Vecteur (int x_a, int y_a, int x_b, int y_b) :  x{x_b - x_a},y{y_b - y_a} {}

Vecteur::Vecteur (int abs, int ord) :  x{abs},y{ord} {}

Vecteur::Vecteur () :  x{0},y{0} {}

bool Vecteur::operator==(const Vecteur& v) const{
    if (v.getX() == getX() && v.getY() == getY() ){
        return true;
    }
    else {
        return false;  
    }
}

bool Vecteur::operator!=(const Vecteur& v) const {
    if (getX() != v.getX() || getY() != v.getY()) {
        return true;
    } else {
        return false;
    }
}


Vecteur Vecteur::operator+(const Vecteur& v)const{
    return Vecteur(getX() + v.getX(), getY() + v.getY());
}
 
Vecteur Vecteur::operator-(const Vecteur& v )const{
    return Vecteur (getX()-v.getX(),getY()-v.getY());
}

int Vecteur::getX() const {return x;}

int Vecteur::getY() const {return y;}

std::ostream& operator<<(std::ostream& os, const Vecteur& v) {
    os << "(" << v.getX() << ", " << v.getY() << ")";
    return os;
}
