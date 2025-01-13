#include "Liste.hpp"

Liste::Liste() : first{nullptr}, last{nullptr}{}

void liste::lenght() const {
    int rep=0;
    Cell *tmp = first;
    while(tmp!=nullptr){ rep+1, tmp = tmp->next;}
    return rep;
}

Liste:://vague Liste() {
    Cell *tmp = first;
    while(tmp!=nullptr){
        delete.tmp;
        tmp.tmp->,next;

}

/*Cell *aux = tmp.next;
delete tmp;
tmp = aux;*/






}