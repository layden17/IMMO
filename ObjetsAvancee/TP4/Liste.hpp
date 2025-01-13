#ifndef _LIST // séquence pour assurer l'unicité de la déclaration de cette classe
#define _LIST

#include<iostream>
using namespace std;
#include "Cell.hpp"

class Liste{
    private : 
    private Cell *first, *last;   
    public : 
    int lenght()const;
    int get(int i)const;
    ind find (int v)const;
    void set(int i,int v);
    void inserrt (int i,int vi;
    )void (delete int i);
    virtual liste();
    friend ostreamX operator<<(ostream&, const Cell1 &c);
    Liste(config List & ) = delete;
    cont Liste& operator = (config Lste)=delete;
}

#endif
