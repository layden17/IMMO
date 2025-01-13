#include "Board.hpp"
#include <iomanip>

// Constructeur
Board::Board() {
    // Initialise le plateau à vide
    for (int i = 0; i < boardSize; ++i) {
        for (int j = 0; j < boardSize; ++j) {
            board[i][j] = ' ';
        }
    }
}

// Méthode pour gérer la disposition des pièces
void Board::placePiece(const Piece& piece) {
    int x = piece.getX();
    int y = piece.getY();

    pieces.push_back(piece);
    board[x][y] = piece.getSymbol();
}

void Board::MAJPiece(const Piece& piece) {
    int playerID = piece.getPlayerID();
    int pieceID = piece.getPieceID();

    // Rechercher la pièce dans le vecteur
    auto it = std::find_if(pieces.begin(), pieces.end(), [playerID, pieceID](const Piece& p) {
        return p.getPlayerID() == playerID && p.getPieceID() == pieceID;
    });

    // Si la pièce est trouvée, la supprimer du vecteur
    if (it != pieces.end()) {
        pieces.erase(it);

        // Ajouter la pièce avec les nouvelles coordonnées
        pieces.push_back(piece);
    }
}

bool Board::isPositionOccupied(int x, int y) const {
    if (board[x][y] != ' ')
        std::cout << "Vos coordonées ne sont pas bonnes car la case est déjà occupé" << std::endl;
    return (board[x][y] != ' ');
}

// Méthodes pour gérer l'ajout de barrières
void Board::addBarrier(const Barriere& barriere) {
    barrieres.push_back(barriere);

    auto coord1 = barriere.getAdjacentCoord1();
    auto coord2 = barriere.getAdjacentCoord2();
    board[coord1.first][coord1.second] = 'X';
    board[coord2.first][coord2.second] = 'X';
}

bool Board::isBarrierBetween(int x1, int y1, int x2, int y2) const {
    for (const auto& barriere : barrieres) {
        auto coord1 = barriere.getAdjacentCoord1();
        auto coord2 = barriere.getAdjacentCoord2();
        if ((coord1.first == x1 && coord1.second == y1 && coord2.first == x2 && coord2.second == y2) ||
            (coord1.first == x2 && coord1.second == y2 && coord2.first == x1 && coord2.second == y1)) {
            return true;
        }
    }
    return false;
}

/*
std::ostream& operator<<(std::ostream& os, const Board& board) {
    // Affiche le plateau avec les pièces et les barrières
    for (int i = 0; i < Board::boardSize; ++i) {
        for (int j = 0; j < Board::boardSize; ++j) {
            char pieceSymbol = ' ';
            int pieceID=-1;
            for (const auto& piece : board.pieces) {
                if (piece.getX() == i && piece.getY() == j) {
                    pieceSymbol = piece.getSymbol();
                    pieceID = piece.getPieceID();
                }
            }

            char barrierSymbol = ' ';
            char barrierHorizontal = '_';
            char barrierVertical = '|';
            for (const auto& barriere : board.barrieres) {
                auto coord1 = barriere.getAdjacentCoord1();
                auto coord2 = barriere.getAdjacentCoord2();
                if ((coord1.first == i && coord1.second == j) ||
                    (coord2.first == i && coord2.second == j)) {
                    barrierSymbol = 'X';
                }
            }

            if (pieceID != -1) {
                os << "[" << std::setw(1) << pieceSymbol << pieceID << barrierSymbol << "]";
            } else {
                os << "[" << std::setw(2) << "  " << barrierSymbol << "]";
            }
        }
        os << std::endl;
    }
    return os;
}
*/


std::ostream& operator<<(std::ostream& os, const Board& board) {
    const int taille = 8;
    std::string BariHaute[taille];
    std::string BariBas[taille];

    for (int i = 0; i < Board::boardSize; ++i) {
        for (int j = 0; j < Board::boardSize; ++j) {
            const Barriere* b = nullptr;
            for (const auto& barriere : board.barrieres) {
                auto coord1 = barriere.getAdjacentCoord1();
                if ((coord1.first == i && coord1.second == j)) {
                    b = &barriere;
                }
            }
            // Ajout d'espaces à l'intérieur de la boucle
            if (b != nullptr && b->getHaut()) {
                BariHaute[i] += "__ ";
            } else {
                BariHaute[i] += "   ";
            }
        }
    }

    for (int i = 0; i < Board::boardSize; ++i) {
        for (int j = 0; j < Board::boardSize; ++j) {
            const Barriere* b = nullptr;
            for (const auto& barriere : board.barrieres) {
                auto coord1 = barriere.getAdjacentCoord1();
                if ((coord1.first == i && coord1.second == j)) {
                    b = &barriere;
                }
            }
            // Ajout d'espaces à l'intérieur de la boucle
            if (b != nullptr && b->getBas()) {
                BariBas[i] += "__ ";
            } else {
                BariBas[i] += "   ";
            }
        }
    }

    // Ajout d'espaces à l'extérieur de la boucle
    for (int i = 0; i < Board::boardSize; ++i) {
        os << BariHaute[i] << std::endl;
        for (int j = 0; j < Board::boardSize; ++j) {
            char pieceSymbol = ' ';
            int pieceID = -1;
            for (const auto& piece : board.pieces) {
                if (piece.getX() == i && piece.getY() == j) {
                    pieceSymbol = piece.getSymbol();
                    pieceID = piece.getPieceID();
                }
            }

            if (pieceID != -1) {
                os << "[" << std::setw(1) << pieceSymbol << pieceID << "]";
            } else {
                os << "[" << std::setw(2) << "]";
            }
        }
        os << std::endl;
        os << BariBas[i];
        
    }
    return os;
}

 


bool Board::isAdjacent(int x1, int y1, int x2, int y2) {
    // Votre logique pour vérifier si (x1, y1) et (x2, y2) sont des coordonnées adjacentes
    // Par exemple, vérifier si la distance entre les deux points est égale à 1
    return (std::abs(x1 - x2) == 1 && y1 == y2) || (x1 == x2 && std::abs(y1 - y2) == 1);
}


/*
bool Board::isPieceAt(int x, int y) const {
    // Rechercher la pièce aux coordonnées spécifiées
    auto it = std::find_if(pieces.begin(), pieces.end(), [x, y](const Piece* piece) {
        return piece->getX() == x && piece->getY() == y;
    });

    // Retourner true si la pièce est trouvée, sinon false
    return it != pieces.end();
}



const Piece& Board::getPieceAt(int x, int y) const {
    // Rechercher la pièce aux coordonnées spécifiées
    auto it = std::find_if(pieces.begin(), pieces.end(), [x, y](const Piece& piece) {
        return piece.getX() == x && piece.getY() == y;
    });

    // Retourner la pièce si elle est trouvée, sinon une référence constante par défaut
    return (it != pieces.end()) ? *it : une référence constante par défaut ;
}
*/

void Board::afficherBarrieres() const {
    for (const auto& barriere : barrieres) {
        barriere.display();
    }
}