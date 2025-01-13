#include "Elephant.hpp"

Elephant::Elephant(int playerID, int pieceID)
    : Piece('E', playerID, pieceID) {}

bool Elephant::move(int newX, int newY) {
    // Implémentation spécifique pour le déplacement de l'éléphant
    // Par exemple, vous pouvez autoriser les déplacements en diagonale
    if ((newX == getX() + 1 || newX == getX() - 1) && (newY == getY() + 1 || newY == getY() - 1)) {
        // Déplacement autorisé
        setCoordinates(newX, newY);
        return true;
    }
    // Déplacement non autorisé
    return false;
}

// ... (ajoutez d'autres membres spécifiques si nécessaire)
