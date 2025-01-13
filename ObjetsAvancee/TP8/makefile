CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -pedantic

all: main
	./main

main: main.o Vecteur.o
	$(CXX) $(CXXFLAGS) -o main main.o Vecteur.o

main.o: main.cpp Vecteur.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

Vecteur.o: Vecteur.cpp Vecteur.hpp
	$(CXX) $(CXXFLAGS) -c Vecteur.cpp

clean:
	rm -f main main.o Vecteur.o
