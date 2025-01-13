#ifndef BOARD_HPP
#define BOARD_HPP

#include "Piece.hpp"
#include "Barriere.hpp"
#include <vector>
#include <ostream>

class Board {
public:
    // Constructeur
    Board();

    // Méthodes pour gérer la disposition des pièces
    void placePiece(const Piece& piece);
    void MAJPiece(const Piece& piece);
    bool isPositionOccupied(int x, int y) const;

    // Méthodes pour gérer l'ajout de barrières
    void addBarrier(const Barriere& barriere);
    bool isBarrierBetween(int x1, int y1, int x2, int y2) const;

    // Opérateur de flux de sortie
    friend std::ostream& operator<<(std::ostream& os, const Board& board);

    bool isAdjacent(int x1, int y1, int x2, int y2);
    virtual ~Board()=default;

    void afficherBarrieres() const;


    /*bool isPieceAt(int x, int y) const;
    const Piece& getPieceAt(int x, int y) const ;
    bool hasBarrierAt(int x, int y) const;*/

public:
    // Dimensions du plateau
    static const int boardSize = 8;
private:
    // Matrice pour représenter le plateau (8x8)
    char board[boardSize][boardSize];

    // Vecteur pour stocker les pièces sur le plateau
    std::vector<Piece> pieces;

    // Vecteur pour stocker les barrières sur le plateau
    std::vector<Barriere> barrieres;
};

#endif // BOARD_HPP