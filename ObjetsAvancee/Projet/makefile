# Makefile for graphic.cpp

# Compiler
CC = g++

# Compiler flags
CFLAGS = -Wall -std=c++11

# SFML libraries
LIBS = -lsfml-graphics -lsfml-window -lsfml-system

# Target executable
TARGET = graphic

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) $(TARGET).cpp -o $(TARGET) $(LIBS)

.PHONY: clean

clean:
	rm -f $(TARGET)
