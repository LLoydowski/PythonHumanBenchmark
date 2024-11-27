## John&Martin Benchmarks – Documentation

## 1. Introduction
Project Purpose:
The Human Benchmark application is a web-based tool that allows users to test and improve their cognitive abilities through interactive games. Users can log in, play games such as Reaction Time, Number Memory, and Verbal Memory, and view their scores on a centralized leaderboard.

Technologies Used:

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript

## 2. Features
User registration and login system.
Three games to test cognitive abilities:
Number Memory: Challenge memory by recalling sequences of numbers.
Reaction Time: Measure how quickly the user reacts.
Verbal Memory: Test the ability to remember previously seen words.
Leaderboard to track scores.
Modular structure with each game implemented in a separate file.
Easily customizable core mechanics (e.g., words in Verbal Memory).

## 3. Project Structure

| **File**              | **Description**                                                              |
|-----------------------|------------------------------------------------------------------------------|
| `Game.py`             | Base class for shared game logic.                                            |
| `main.py`             | Main file to start the application.                                          |
| `NumberMemory.py`     | Logic for the Number Memory game.                                            |
| `ReactionTime.py`     | Logic for the Reaction Time game.                                            |
| `VerbalMemory.py`     | Logic for the Verbal Memory game.                                            |
| `Scoreboard.py`       | Manages scores and leaderboards.                                             |
| `server.py`           | Sets up the Flask server.                                                    |
| `userManagement.py`   | Handles user authentication and session management.                          |
| HTML and CSS files    | Frontend files for the website.                    

## 4. Installation
Prerequisites:

Python 3.10 or higher
Flask
Steps:

Download the project.
Run the main file.
Choose the mode:
Press 1 for the terminal version.
Press 2 for the website version.
If using the terminal version:
Choose a game:
1: Reaction Time
2: Number Memory
3: Verbal Memory
4: Scores
If using the website version:
Copy the printed IP address (in the terminal).
Paste it into your browser, ensuring the port is set to 85.

## 5. File Descriptions
### 1. Game.py
Purpose: Serves as a parent class for all game modes.
Core Features:

Contains shared functionality like starting, ending, and scoring.
Defines methods like startGame() and endGame().

### 2. NumberMemory.py
Purpose: Implements the Number Memory game.
Core Features:

Generates random numbers to memorize.
Checks user input for correctness.
Tracks scores based on correct sequences.

### 3. ReactionTime.py
Purpose: Implements the Reaction Time game.
Core Features:

Displays a stimulus for the player to react to.
Measures reaction time.
Updates scores based on performance.

### 4. VerbalMemory.py
Purpose: Implements the Verbal Memory game.
Core Features:

Presents words to identify as "Seen" or "New."
Tracks correct answers and scores.

### 5. Scoreboard.py
Purpose: Manages the scoreboard system.
Core Features:

Reads and writes scores from a text file (scores.txt).
Updates and retrieves persistent score records.

### 6. userManagement.py
Purpose: Handles user authentication and account management.
Core Features:

User registration and login with secure password storage.
Integration with the games and leaderboard.

### 7. server.py
Purpose: Manages server-side operations.
Core Features:

Handles HTTP requests and serves API endpoints.
Processes game data and user actions.

### 8. main.py
Purpose: Starts the app and allows mode selection.
Core Features:

Opens the server for the web mode.
Handles CLI-based game interactions.

## 6. Game Descriptions
Number Memory
Objective: Recall the numbers shown in the correct sequence.
Mechanics:
A sequence of numbers is displayed.
User inputs the sequence.
Difficulty increases with correct answers.
Reaction Time
Objective: Click as quickly as possible when the screen turns green.
Mechanics:
A stimulus appears randomly.
Reaction time is recorded and scored.
Verbal Memory
Objective: Identify whether a word has been seen before.
Mechanics:
Words are displayed one by one.
User selects "Seen" or "New."

## 7. Authors
The application was created by Janek Baszczyński and Marcin Gromadzki.

Marcin Gromadzki:

Website frontend
Python games (2)

Janek Baszczyński:

Website backend (Flask)
Python games (1)
