#include<iostream>
using namespace std;

class Cell{
 public :
    int contenu;
 private :
    Cell *pred,*suiv;

    public Cell (int x){
        contenu{x};
        this.getPred(){nullptr}
        this.getSuiv(){nullptr}

    }

    public Cell(){
        contenu{0};
        this.getPred(){nullptr}
        this.getSuiv(){nullptr}
    }
   
    public void connect(Cell c){

        this.suiv = c.pred;
        c.pred = this.suiv;

    }

    public Cell getPred(){
        return this.pred;

    }
    
    public Cell getSuiv(){
        return this.suiv;

    }

    public void disconnect_next(){

     this.suiv.pred = nullptr;
     this.suiv = nullptr;
    }

    public void disconnect_previous(){

     this.pred.suiv = nullptr;
     this.pred = nullptr;
    }



}

int main(){


}