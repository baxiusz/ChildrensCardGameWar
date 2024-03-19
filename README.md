Children's Card Game: War
Overview
The goal of this project is to implement a Python program for the classic children's card game, War. The game will be developed using the Object-Oriented Programming (OOP) paradigm to ensure modularity, readability, and extensibility of the codebase.

Requirements
Functional Requirements:
Deck of Cards:

The game must have a standard 52-card deck, consisting of four suits (hearts, diamonds, clubs, spades) and thirteen ranks (2 through Ace).
The deck should be shuffled before each game.
Players:

The game should support two players.
Each player should be dealt an equal number of cards from the shuffled deck at the beginning of the game.
Gameplay:

Players take turns playing cards from the top of their respective decks.
The player with the higher-ranked card wins the round and collects both cards.
In the event of a tie, a "war" occurs:
Each player places three cards face down and then one card face up.
The player with the higher-ranked face-up card wins all the cards in the war.
If there's another tie during a war, the process repeats until a winner is determined.
The game continues until one player runs out of cards, at which point the other player is declared the winner.
User Interface:

Implement a simple text-based user interface to display game information, such as the cards played by each player and the outcome of each round.
Non-Functional Requirements:
Object-Oriented Design:

The program must be structured using OOP principles, with classes representing entities like cards, decks, players, and the game itself.
Readability and Documentation:

Code should be well-documented using meaningful variable names, comments, and docstrings to ensure readability and ease of understanding for future maintainers.
Error Handling:

Implement error handling to gracefully deal with invalid user inputs or unexpected runtime errors.
Git Version Control:

Utilize Git for version control, with regular commits and meaningful commit messages to track changes and collaborate effectively.
Getting Started
Clone the repository to your local machine.
Install Python (if not already installed).
Navigate to the project directory.
Run the Python program to start the game.