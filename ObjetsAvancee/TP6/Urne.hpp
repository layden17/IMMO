#ifndef SCRUTIN_H
#define SCRUNTIN_H

class Scrutin;

class Urne{

    private:
        const Scrutin& scrutin;
        static unsigned int NB;
        const unsigned int n;
        vector<unsigned int> resultats;
        Urne(const Urne&)=delete;
        Urne& operator =(const Urne&)=delete;

    public:
        Urne(scrutin);
        bool voter(int choix);

}

#endif
