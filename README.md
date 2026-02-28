# Rock Paper Scissors Game

A simple command-line Rock Paper Scissors game implemented in Python.

## Features

- Interactive gameplay with user input validation
- Computer opponent with random choice generation
- Score tracking throughout the game session
- Clean, user-friendly interface
- Comprehensive test suite

## How to Play

1. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```

2. Enter your choice when prompted:
   - `rock`
   - `paper` 
   - `scissors`
   - `quit` to exit

3. The computer will make its choice and the winner will be determined
4. Scores are tracked and displayed after each round
5. Final scores are shown when you quit

## Game Rules

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper
- Same choices result in a tie

## Running Tests

To run the test suite:

```bash
pytest test_rock_paper_scissors.py
```

Or with verbose output:

```bash
pytest test_rock_paper_scissors.py -v
```

## Requirements

- Python 3.6+
- pytest (for running tests)

## File Structure

- `rock_paper_scissors.py` - Main game implementation
- `test_rock_paper_scissors.py` - Comprehensive test suite
- `README.md` - This file