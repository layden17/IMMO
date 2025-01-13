#ifndef _CELL // séquence pour assurer l'unicité de la déclaration de cette classe
#define _CELL

#include<iostream>
using namespace std;
class Liste;

class Cell{
 public :
    int contenu;
    Cell *pred,*suiv;

    Cell (int v, Cell *p =nullptr, Cell *p=nullptr );
    static void content (Cell &c1, Cell &c2);
    void disconnect_next;
private:
    Cell(const Cell&) = delete;
    Cell& operator = (const Cell &)= delete;
    friend ostreamX operator<<(ostream&, const Cell1&);
    friend class liste;

}

#endif