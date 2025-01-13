#include "Barriere.hpp"
#include <iostream>

// Constructeur
Barriere::Barriere(int x1, int y1, int x2, int y2) : coord1(x1, y1), coord2(x2, y2), gauche{false}, droite{false}, haut{false}{
            
        if (x1 == x2) {
        if (y1 > y2) {
            gauche = true;
        } else if (y1 < y2) {
            droite = true;
        }
    } else if (y1 == y2) {
        if (x1 > x2) {
            haut = true;
        } else if (x1 < x2) {
            bas = true;
        }
    }
}

// Méthode pour afficher la barrière
void Barriere::display() const {
    std::cout << "Barriere between (" << coord1.first << ", " << coord1.second << ") and ("
              << coord2.first << ", " << coord2.second << ")" << std::endl;
}

// Méthodes pour obtenir les coordonnées des cases adjacentes
std::pair<int, int> Barriere::getAdjacentCoord1() const {
    return coord1;
}

std::pair<int, int> Barriere::getAdjacentCoord2() const {
    return coord2;
}

void Barriere::setGauche(bool value) {
        gauche = value;
}

void Barriere::setDroite(bool value) {
        droite = value;
}

void Barriere::setHaut(bool value) {
        haut = value;
}

void Barriere::setBas(bool value) {
        bas = value;
}

bool Barriere::getGauche() const {
        return gauche ;
}

bool Barriere::getDroite() const{
        return droite ;
}

bool Barriere::getHaut() const{
        return haut;
}

bool Barriere::getBas() const{
        return bas ;
}