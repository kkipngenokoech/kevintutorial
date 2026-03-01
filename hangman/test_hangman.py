"""Tests for the hangman game."""

import pytest
from unittest.mock import patch
from hangman.hangman import HangmanGame
from hangman.words import get_random_word, EASY_WORDS, MEDIUM_WORDS, HARD_WORDS, ALL_WORDS
from hangman.ascii_art import get_hangman_art, display_word_progress

class TestWords:
    """Test word selection functionality."""
    
    def test_get_random_word_easy(self):
        """Test getting random easy word."""
        word = get_random_word("easy")
        assert word.upper() in [w.upper() for w in EASY_WORDS]
        assert word.isupper()
    
    def test_get_random_word_medium(self):
        """Test getting random medium word."""
        word = get_random_word("medium")
        assert word.upper() in [w.upper() for w in MEDIUM_WORDS]
        assert word.isupper()
    
    def test_get_random_word_hard(self):
        """Test getting random hard word."""
        word = get_random_word("hard")
        assert word.upper() in [w.upper() for w in HARD_WORDS]
        assert word.isupper()
    
    def test_get_random_word_random(self):
        """Test getting random word from all difficulties."""
        word = get_random_word("random")
        assert word.upper() in [w.upper() for w in ALL_WORDS]
        assert word.isupper()
    
    def test_get_random_word_invalid_difficulty(self):
        """Test getting random word with invalid difficulty defaults to all words."""
        word = get_random_word("invalid")
        assert word.upper() in [w.upper() for w in ALL_WORDS]
        assert word.isupper()

class TestAsciiArt:
    """Test ASCII art functionality."""
    
    def test_get_hangman_art_valid_stages(self):
        """Test getting hangman art for valid stages."""
        for i in range(7):
            art = get_hangman_art(i)
            assert isinstance(art, str)
            assert len(art) > 0
            assert "+---+" in art
    
    def test_get_hangman_art_negative_input(self):
        """Test hangman art with negative input."""
        art = get_hangman_art(-1)
        assert art == get_hangman_art(0)
    
    def test_get_hangman_art_too_high_input(self):
        """Test hangman art with input too high."""
        art = get_hangman_art(10)
        assert art == get_hangman_art(6)
    
    def test_display_word_progress_no_guesses(self):
        """Test word progress display with no guesses."""
        result = display_word_progress("HELLO", set())
        assert result == "_ _ _ _ _"
    
    def test_display_word_progress_some_guesses(self):
        """Test word progress display with some correct guesses."""
        result = display_word_progress("HELLO", {"H", "L"})
        assert result == "H _ L L _"
    
    def test_display_word_progress_all_guesses(self):
        """Test word progress display with all letters guessed."""
        result = display_word_progress("HELLO", {"H", "E", "L", "O"})
        assert result == "H E L L O"
    
    def test_display_word_progress_case_insensitive(self):
        """Test word progress display is case insensitive."""
        result = display_word_progress("hello", {"H", "L"})
        assert result == "h _ l l _"

class TestHangmanGame:
    """Test hangman game logic."""
    
    @patch('hangman.hangman.get_random_word')
    def test_game_initialization(self, mock_get_word):
        """Test game initialization."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        assert game.word == "HELLO"
        assert game.max_wrong_guesses == 6
        assert game.guessed_letters == set()
        assert game.wrong_guesses == 0
        assert game.game_over is False
        assert game.won is False
    
    @patch('hangman.hangman.get_random_word')
    def test_valid_guess_checking(self, mock_get_word):
        """Test valid guess checking."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        assert game.is_valid_guess("A") is True
        assert game.is_valid_guess("a") is True
        assert game.is_valid_guess("1") is False
        assert game.is_valid_guess("AB") is False
        assert game.is_valid_guess("") is False
        
        game.guessed_letters.add("A")
        assert game.is_valid_guess("A") is False
        assert game.is_valid_guess("a") is False
    
    @patch('hangman.hangman.get_random_word')
    def test_correct_guess(self, mock_get_word):
        """Test making a correct guess."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        result = game.make_guess("H")
        
        assert result["status"] == "correct"
        assert "H" in game.guessed_letters
        assert game.wrong_guesses == 0
        assert game.game_over is False
    
    @patch('hangman.hangman.get_random_word')
    def test_wrong_guess(self, mock_get_word):
        """Test making a wrong guess."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        result = game.make_guess("X")
        
        assert result["status"] == "wrong"
        assert "X" in game.guessed_letters
        assert game.wrong_guesses == 1
        assert game.game_over is False
    
    @patch('hangman.hangman.get_random_word')
    def test_invalid_guess(self, mock_get_word):
        """Test making an invalid guess."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        result = game.make_guess("12")
        assert result["status"] == "invalid"
        
        result = game.make_guess("1")
        assert result["status"] == "invalid"
    
    @patch('hangman.hangman.get_random_word')
    def test_duplicate_guess(self, mock_get_word):
        """Test making a duplicate guess."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        game.make_guess("H")
        result = game.make_guess("H")
        
        assert result["status"] == "duplicate"
    
    @patch('hangman.hangman.get_random_word')
    def test_winning_game(self, mock_get_word):
        """Test winning the game."""
        mock_get_word.return_value = "CAT"
        game = HangmanGame()
        
        game.make_guess("C")
        game.make_guess("A")
        result = game.make_guess("T")
        
        assert result["status"] == "win"
        assert game.game_over is True
        assert game.won is True
    
    @patch('hangman.hangman.get_random_word')
    def test_losing_game(self, mock_get_word):
        """Test losing the game."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        wrong_letters = ["X", "Y", "Z", "Q", "W", "R"]
        for letter in wrong_letters[:-1]:
            result = game.make_guess(letter)
            assert result["status"] == "wrong"
            assert game.game_over is False
        
        result = game.make_guess(wrong_letters[-1])
        assert result["status"] == "lose"
        assert game.game_over is True
        assert game.won is False
    
    @patch('hangman.hangman.get_random_word')
    def test_get_game_state(self, mock_get_word):
        """Test getting game state."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        game.make_guess("H")
        game.make_guess("X")
        
        state = game.get_game_state()
        
        assert "word_progress" in state
        assert "hangman_art" in state
        assert "guessed_letters" in state
        assert "wrong_guesses" in state
        assert "max_wrong_guesses" in state
        assert "game_over" in state
        assert "won" in state
        assert "word" in state
        
        assert state["wrong_guesses"] == 1
        assert "H" in state["guessed_letters"]
        assert "X" in state["guessed_letters"]
        assert state["game_over"] is False
        assert state["won"] is False
    
    @patch('hangman.hangman.get_random_word')
    def test_reset_game(self, mock_get_word):
        """Test resetting the game."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        game.make_guess("H")
        game.make_guess("X")
        
        mock_get_word.return_value = "WORLD"
        game.reset_game()
        
        assert game.word == "WORLD"
        assert game.guessed_letters == set()
        assert game.wrong_guesses == 0
        assert game.game_over is False
        assert game.won is False
    
    @patch('hangman.hangman.get_random_word')
    def test_case_insensitive_guesses(self, mock_get_word):
        """Test that guesses are case insensitive."""
        mock_get_word.return_value = "HELLO"
        game = HangmanGame()
        
        result = game.make_guess("h")
        assert result["status"] == "correct"
        assert "H" in game.guessed_letters
        
        result = game.make_guess("H")
        assert result["status"] == "duplicate"
    
    @patch('hangman.hangman.get_random_word')
    def test_case_insensitive_word_matching(self, mock_get_word):
        """Test that word matching is case insensitive."""
        mock_get_word.return_value = "hello"
        game = HangmanGame()
        
        result = game.make_guess("H")
        assert result["status"] == "correct"
        
        result = game.make_guess("X")
        assert result["status"] == "wrong"
        assert game.wrong_guesses == 1
