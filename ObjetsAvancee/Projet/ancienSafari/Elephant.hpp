#ifndef ELEPHANT_HPP
#define ELEPHANT_HPP

#include "Piece.hpp"

class Elephant : public Piece {
public:
    Elephant(int playerID, int pieceID);

    // Implémentation spécifique pour le déplacement de l'éléphant
    bool move(int newX, int newY) override;

    // ... (ajoutez d'autres membres spécifiques si nécessaire)
};

#endif // ELEPHANT_HPP