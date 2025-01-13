#include <SFML/Graphics.hpp>
using namespace sf;
int main(){
    RenderWindow app(VideoMode(800, 600, 32), "Test ");
    while (app.isOpen()){
        Event event;
        while (app.pollEvent(event)){
            switch (event.type) {
                case Event::Closed:
                app.close(); break;
                default: break;
            }
        }
        Font font;
         if (!font.loadFromFile("/Users/lathan/Documents/ObjetsAvancee/Projet/Agatha.ttf")) {
        // Gérer l'erreur si le chargement de la police échoue
            return EXIT_FAILURE;
        }
        Text text;
        text.setFont(font);
        text.setString(" Hello world");
        text.setCharacterSize(100);
        text.setFillColor(Color::Red);  
        app.clear(); // vide l'écran
        app.draw(text);
        app.display(); // Affichage effectif
    } // fenêtre fermée
    return EXIT_SUCCESS;
}