#ifndef BARRIERE_HPP
#define BARRIERE_HPP

#include <utility>

class Barriere {
public:
    // Constructeur
    Barriere(int x1, int y1, int x2, int y2);
    

    // Méthode pour afficher la barrière
    void display() const;
    virtual ~Barriere()=default;

    // Méthodes pour obtenir les coordonnées des cases adjacentes
    std::pair<int, int> getAdjacentCoord1() const;
    std::pair<int, int> getAdjacentCoord2() const;

    void setGauche(bool value);
    void setDroite(bool value); 
    void setHaut(bool value); 
    void setBas(bool value);

    bool getGauche() const;
    bool getDroite() const;
    bool getHaut() const;
    bool getBas() const;


private:
    // Coordonnées des cases adjacentes
    std::pair<int, int> coord1;
    std::pair<int, int> coord2;
    bool gauche;
    bool droite;
    bool haut;
    bool bas;
};

#endif // BARRIERE_HPP
