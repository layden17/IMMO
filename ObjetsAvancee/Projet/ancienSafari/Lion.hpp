#ifndef LION_HPP
#define LION_HPP

#include "Piece.hpp"

class Lion : public Piece {
public:
    Lion(int playerID, int pieceID);

    bool move(int newX, int newY) override;

    // ... (ajoutez d'autres membres spécifiques si nécessaire)
};

#endif // LION_HPP
