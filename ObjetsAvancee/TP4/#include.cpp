#include<iostream>
using namespace std;
include "Cell.hpp";

Cell:Cell (int v,Cell* p,Cell* m): contenu{v},pred{p},suiv(m){}
bool Cell:connect (Cell &c1,Cell &c2 ){
    if (c1.next != nullptr) || (c1.pred != nullptr) return false;
        c1.next = &c2;
        c2.prev = &c1;
    return true;
}

Cell * Cell:: disconnect_next(){
    Cell *rep=next;
    Cell next = nullptr;
    if(rep != )
        rep.pred= nullptr;
    return rep;

}

friend ostreamX operator<<(ostream&, const Cell1 &c){
    o << c.val << " ";
    return 0;
}