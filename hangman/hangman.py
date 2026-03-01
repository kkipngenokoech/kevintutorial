"""Main hangman game logic."""

import re
from .words import get_random_word
from .ascii_art import get_hangman_art, display_word_progress

class HangmanGame:
    """Hangman game class that manages game state and logic."""
    
    def __init__(self, difficulty="medium", max_wrong_guesses=6):
        """Initialize a new hangman game.
        
        Args:
            difficulty (str): Difficulty level ('easy', 'medium', 'hard', 'random')
            max_wrong_guesses (int): Maximum number of wrong guesses allowed
        """
        self.word = get_random_word(difficulty)
        self.max_wrong_guesses = max_wrong_guesses
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False
    
    def is_valid_guess(self, guess):
        """Check if a guess is valid (single letter, alphabetic).
        
        Args:
            guess (str): The guessed character
            
        Returns:
            bool: True if guess is valid, False otherwise
        """
        return (len(guess) == 1 and 
                guess.isalpha() and 
                guess.upper() not in self.guessed_letters)
    
    def make_guess(self, guess):
        """Make a guess and update game state.
        
        Args:
            guess (str): The guessed character
            
        Returns:
            dict: Result of the guess with status and message
        """
        guess = guess.upper()
        
        if not self.is_valid_guess(guess):
            if len(guess) != 1 or not guess.isalpha():
                return {"status": "invalid", "message": "Please enter a single letter."}
            else:
                return {"status": "duplicate", "message": f"You already guessed '{guess}'."}
        
        self.guessed_letters.add(guess)
        
        if guess in self.word.upper():
            # Check if word is complete
            if all(letter.upper() in self.guessed_letters for letter in self.word):
                self.game_over = True
                self.won = True
                return {"status": "win", "message": f"Correct! You won! The word was '{self.word}'."}
            else:
                return {"status": "correct", "message": f"Good guess! '{guess}' is in the word."}
        else:
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_wrong_guesses:
                self.game_over = True
                self.won = False
                return {"status": "lose", "message": f"Game over! The word was '{self.word}'."}
            else:
                remaining = self.max_wrong_guesses - self.wrong_guesses
                return {"status": "wrong", "message": f"'{guess}' is not in the word. {remaining} guesses left."}
    
    def get_game_state(self):
        """Get current game state for display.
        
        Returns:
            dict: Current game state information
        """
        return {
            "word_progress": display_word_progress(self.word, self.guessed_letters),
            "hangman_art": get_hangman_art(self.wrong_guesses),
            "guessed_letters": sorted(list(self.guessed_letters)),
            "wrong_guesses": self.wrong_guesses,
            "max_wrong_guesses": self.max_wrong_guesses,
            "game_over": self.game_over,
            "won": self.won,
            "word": self.word
        }
    
    def reset_game(self, difficulty="medium"):
        """Reset the game with a new word.
        
        Args:
            difficulty (str): Difficulty level for new word
        """
        self.word = get_random_word(difficulty)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False

def play_hangman():
    """Play a console-based hangman game."""
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("You have 6 wrong guesses before you lose.\n")
    
    while True:
        # Get difficulty
        difficulty = input("Choose difficulty (easy/medium/hard/random): ").strip().lower()
        if difficulty not in ["easy", "medium", "hard", "random"]:
            difficulty = "medium"
        
        game = HangmanGame(difficulty)
        
        while not game.game_over:
            state = game.get_game_state()
            
            # Display game state
            print(state["hangman_art"])
            print(f"Word: {state['word_progress']}")
            print(f"Guessed letters: {', '.join(state['guessed_letters']) if state['guessed_letters'] else 'None'}")
            print(f"Wrong guesses: {state['wrong_guesses']}/{state['max_wrong_guesses']}\n")
            
            # Get guess
            guess = input("Enter your guess: ").strip()
            result = game.make_guess(guess)
            
            print(f"\n{result['message']}\n")
            
            if result["status"] in ["win", "lose"]:
                state = game.get_game_state()
                print(state["hangman_art"])
                print(f"Final word: {state['word']}\n")
        
        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y' and play_again != 'yes':
            break
        print("\n" + "="*50 + "\n")
    
    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    play_hangman()
