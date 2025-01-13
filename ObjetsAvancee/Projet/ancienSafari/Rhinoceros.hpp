#ifndef RHINOCEROS_HPP
#define RHINOCEROS_HPP

#include "Piece.hpp"

class Rhinoceros : public Piece {
public:
    Rhinoceros(int playerID,int pieceID);

    bool move(int newX, int newY) override;

    // ... (ajoutez d'autres membres spécifiques si nécessaire)
};

#endif // RHINOCEROS_HPP