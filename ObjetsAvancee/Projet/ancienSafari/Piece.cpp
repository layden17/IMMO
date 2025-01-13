#include "Piece.hpp"

// Constructeur
Piece::Piece(char symbol, int playerID,int pieceID)
    : symbol{symbol}, playerID{playerID},pieceID{pieceID}, x(-1), y(-1) {}

// Méthode pour afficher l'animal
void Piece::display() const {
    std::cout << symbol << pieceID << "(" << x << "," << y <<  ")" << std::endl; 
}

// Méthode pour obtenir le symbole de l'animal
char Piece::getSymbol() const {
    return symbol;
}

// Méthode pour obtenir l'ID du joueur propriétaire
int Piece::getPlayerID() const {
    return playerID;
}


int Piece::getPieceID() const {
    return pieceID;
}

// Méthodes pour obtenir et définir les coordonnées de l'animal
int Piece::getX() const {
    return x;
}

int Piece::getY() const {
    return y;
}

void Piece::setCoordinates(int newX, int newY) {
    x = newX;
    y = newY;
}

// Méthode pour déplacer l'animal
bool Piece::move(int newX, int newY) {
    std::cout << "(dans piece) les coord :" << newX << " , " << newY << std::endl;
    x = newX;
    y = newY;
    return true;
}

// Destructeur virtuel pour permettre la polymorphie
