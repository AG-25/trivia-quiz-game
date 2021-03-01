# Trivia Quiz Game
This is a trivia quiz that extracts general knowledge questions from an API, provides the player with a graphical user interface, checks the players answers and keeps track of their score.

## How the Game Works
1. Extracts true or false questions from the OpenTrivia API (URL provided below).  
1. Serves questions to the player through a graphical user interface using a QuizInterface class, which utilises the tkinter module. 
1. Checks answers and changes the question using a  QuizBrain class.   
1. Ends the quiz after 10 questions have been answered and provides the players final score.  

## Installation
* Download main.py and the other source code files in the src folder, or clone the repository. 
* Install the requests module using pip (see requirements.txt).
* Start the game by running main.py  

## Supporting Libraries and APIs
* OpenTrivia API (for quiz questions): https://opentdb.com/
