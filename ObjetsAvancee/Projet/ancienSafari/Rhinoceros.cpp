#include "Rhinoceros.hpp"

Rhinoceros::Rhinoceros(int playerID, int pieceID)
    : Piece('R', playerID, pieceID) {}

bool Rhinoceros::move(int newX, int newY) {
    // Implémentation spécifique pour le déplacement du rhinocéros
    // Par exemple, vous pouvez autoriser les déplacements horizontaux ou verticaux d'une seule case
    if ((newX == getX() + 1 || newX == getX() - 1 || newX == getX()) && (newY == getY() + 1 || newY == getY() - 1 || newY == getY())) {
        // Déplacement autorisé
        setCoordinates(newX, newY);
        return true;
    }
    // Déplacement non autorisé
    return false;
}

// ... (ajoutez d'autres membres spécifiques si nécessaire)
