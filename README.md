# cse210-02
Abstraction: Teach One Another

Hilo The Game
# Libraries
* deque
* random

# Hilo
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. 
Points are won or lost based on whether or not the player guessed correctly.

# Rules
* The player starts the game with 300 points.
* Individual cards are represented as a number from 1 to 13.
* The current card is displayed.
* The player guesses if the next one will be higher or lower.
* The the next card is displayed.
* The player earns 100 points if they guessed correctly.
* The player loses 75 points if they guessed incorrectly.
* If a player reaches 0 points the game is over.
* If a player has more than 0 points they decide if they want to keep playing.
* If a player decides not to play again the game is over.

# Instructions
* In the cli execute python3 __main__.py
* Select "h" for higher or "l" for lower.
* Decide if wants to continue playing the game.

# Project Structure
* __main__.py     (program entry point)
* hilo.py         (Game main structure)

# Required Software
* Python 3.8.0

# Contributors
* Joseph Perez
    - per16068@byui.edu
    - Class Game_Logic
* Daniel Parra
    - par21002@byui.edu
    - Class Player
* Jonathan Uribe 
    - u266801382@byui.edu
    - Class card
* Gloria Rosado 
    - ros21035@byui.edu
    - Documentation of the game
* Thomas Villalobos
    - vil22003@byui.edu
    - Fix some bugs and add features