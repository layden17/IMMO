#ifndef PIECE_HPP
#define PIECE_HPP

#include <iostream>

class Piece {
    private:
        char symbol;  // Symbole représentant l'animal sur le plateau
        int playerID; // ID du joueur propriétaire de l'animal
        int pieceID;
        int x;        // Coordonnée x sur le plateau
        int y;        // Coordonnée y sur le plateau

    public:
        // Constructeur
        Piece(char symbol, int playerID,int pieceID);

        // Méthode pour afficher l'animal
        void display() const;

        // Méthode pour obtenir le symbole de l'animal
        char getSymbol() const;

        // Méthode pour obtenir l'ID du joueur propriétaire
        int getPlayerID() const;

        int getPieceID() const;

        // Méthodes pour obtenir et définir les coordonnées de l'animal
        int getX() const;
        int getY() const;
        void setCoordinates(int newX, int newY);

        // Méthode pour déplacer l'animal
        virtual bool move(int newX, int newY);

        // Destructeur virtuel pour permettre la polymorphie
        virtual ~Piece()=default;

};

#endif // PIECE_HPP
