import pytest
from unittest.mock import patch
from rock_paper_scissors import (
    get_computer_choice,
    determine_winner,
    display_choices,
    display_result,
    display_score
)


class TestRockPaperScissors:
    
    def test_get_computer_choice(self):
        """Test that computer choice is valid."""
        choice = get_computer_choice()
        assert choice in ['rock', 'paper', 'scissors']
    
    def test_determine_winner_tie(self):
        """Test tie scenarios."""
        assert determine_winner('rock', 'rock') == 'tie'
        assert determine_winner('paper', 'paper') == 'tie'
        assert determine_winner('scissors', 'scissors') == 'tie'
    
    def test_determine_winner_user_wins(self):
        """Test user winning scenarios."""
        assert determine_winner('rock', 'scissors') == 'user'
        assert determine_winner('paper', 'rock') == 'user'
        assert determine_winner('scissors', 'paper') == 'user'
    
    def test_determine_winner_computer_wins(self):
        """Test computer winning scenarios."""
        assert determine_winner('rock', 'paper') == 'computer'
        assert determine_winner('paper', 'scissors') == 'computer'
        assert determine_winner('scissors', 'rock') == 'computer'
    
    @patch('builtins.print')
    def test_display_choices(self, mock_print):
        """Test display choices function."""
        display_choices('rock', 'paper')
        mock_print.assert_any_call('\nYou chose: rock')
        mock_print.assert_any_call('Computer chose: paper')
    
    @patch('builtins.print')
    def test_display_result_tie(self, mock_print):
        """Test display result for tie."""
        display_result('tie')
        mock_print.assert_called_with("It's a tie!")
    
    @patch('builtins.print')
    def test_display_result_user_wins(self, mock_print):
        """Test display result for user win."""
        display_result('user')
        mock_print.assert_called_with("You win this round!")
    
    @patch('builtins.print')
    def test_display_result_computer_wins(self, mock_print):
        """Test display result for computer win."""
        display_result('computer')
        mock_print.assert_called_with("Computer wins this round!")
    
    @patch('builtins.print')
    def test_display_score(self, mock_print):
        """Test display score function."""
        display_score(3, 2)
        mock_print.assert_called_with('\nScore - You: 3, Computer: 2')
