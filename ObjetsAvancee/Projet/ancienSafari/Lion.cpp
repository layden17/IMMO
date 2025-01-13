#include "Lion.hpp"

Lion::Lion(int playerID, int pieceID)
    : Piece('L', playerID, pieceID) {}

bool Lion::move(int newX, int newY) {
    // Implémentation spécifique pour le déplacement du lion
    // Par exemple, vous pouvez autoriser les déplacements dans toutes les directions d'une case
    if (newX == getX() + 1 || newX == getX() - 1 || newX == getX()) {
        if (newY == getY() + 1 || newY == getY() - 1 || newY == getY()) {
            // Déplacement autorisé
            setCoordinates(newX, newY);
            return true;
        }
    }
    // Déplacement non autorisé
    return false;
}

// ... (ajoutez d'autres membres spécifiques si nécessaire)
