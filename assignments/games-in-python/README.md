
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python that practices string manipulation, loops, and conditional logic while delivering a clear win/lose experience.

## 📝 Tasks

### 🛠️ Core Hangman Gameplay

#### Description
Create a playable Hangman game that selects a secret word, accepts single-letter guesses, and updates the masked word state until the player wins or loses.

#### Requirements
Completed program should:

- Randomly select the secret word from a predefined list of at least 8 words
- Display the current word state using underscores for hidden letters (e.g., `_ _ g _ _`)
- Track and show remaining incorrect attempts (recommend 6-10)
- Reject repeated guesses and do not penalize them twice
- End the game with a win message when all letters are revealed or a loss message when attempts reach zero

### 🛠️ User Experience and Validation

#### Description
Improve the player's experience with clear prompts, input validation, and a summary of guesses made.

#### Requirements
Completed program should:

- Accept only single alphabetic characters for guesses; reprompt on invalid input
- Show the list of guessed letters after each turn
- Provide distinct messages for correct vs. incorrect guesses
- Offer an option to play again without restarting the script
- Include at least one sample run (input/output) in comments or a separate text block within the script
