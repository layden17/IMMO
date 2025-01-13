#include "Piece.hpp"
#include "Elephant.hpp"
#include "Rhinoceros.hpp"
#include "Lion.hpp"
#include "Barriere.hpp"
#include "Board.hpp"
#include "Player.hpp"
#include "Game.hpp"



int main() {
    
    /*
    // Création d'un pion (à remplacer par des éléphants, rhinocéros, lions)
    Piece genericPiece('P', 1, 3, 4);

    // Affichage du pion
    std::cout << "Pion sur les coordonnées (" << genericPiece.getX() << ", " << genericPiece.getY() << "): ";
    genericPiece.display();
    std::cout << std::endl;

    // Déplacement du pion
    genericPiece.move(5, 6);

    // Affichage des nouvelles coordonnées
    std::cout << "Nouvelles coordonnées (" << genericPiece.getX() << ", " << genericPiece.getY() << ")" << std::endl;

        // Créez un éléphant, un rhinocéros et un lion
    Elephant elephant(1, 2, 3);
    Rhinoceros rhinoceros(2, 4, 5);
    Lion lion(3, 6, 7);

    // Affichez les positions initiales
    std::cout << "Position initiale de l'éléphant : (" << elephant.getX() << ", " << elephant.getY() << ")" << std::endl;
    std::cout << "Position initiale du rhinocéros : (" << rhinoceros.getX() << ", " << rhinoceros.getY() << ")" << std::endl;
    std::cout << "Position initiale du lion : (" << lion.getX() << ", " << lion.getY() << ")" << std::endl;

    // Testez le déplacement
    elephant.move(3, 4);
    rhinoceros.move(5, 6);
    lion.move(7, 8);

    // Affichez les nouvelles positions
    std::cout << "Nouvelle position de l'éléphant : (" << elephant.getX() << ", " << elephant.getY() << ")" << std::endl;
    std::cout << "Nouvelle position du rhinocéros : (" << rhinoceros.getX() << ", " << rhinoceros.getY() << ")" << std::endl;
    std::cout << "Nouvelle position du lion : (" << lion.getX() << ", " << lion.getY() << ")" << std::endl;

    // Exemple d'utilisation
    Barriere myBarrier(2, 3, 3, 3);
    myBarrier.display();

    std::pair<int, int> coord1 = myBarrier.getAdjacentCoord1();
    std::pair<int, int> coord2 = myBarrier.getAdjacentCoord2();

    std::cout << "Adjacent Coordinates: (" << coord1.first << ", " << coord1.second << ") and ("
            << coord2.first << ", " << coord2.second << ")" << std::endl;

    Board myBoard;
    // ... Ajoutez des pièces et des barrières à votre plateau ...

    std::cout << myBoard; // Utilisation de l'opérateur de flux de sortie pour afficher le plateau

    */

    Game game;
    game.start();
    std::cout << "START FIN" << std::endl;
    game.displayPlayers();
    game.placeBarriers();

    return 0;
}
