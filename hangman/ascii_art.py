"""ASCII art for the hangman game."""

HANGMAN_STAGES = [
    # Stage 0: No wrong guesses
    r"""
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    # Stage 1: Head
    r"""
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    # Stage 2: Body
    r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    # Stage 3: Left arm
    r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    # Stage 4: Right arm
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    # Stage 5: Left leg
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    # Stage 6: Right leg (Game Over)
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

def get_hangman_art(wrong_guesses):
    """Get the hangman ASCII art for the current number of wrong guesses.
    
    Args:
        wrong_guesses (int): Number of wrong guesses (0-6)
        
    Returns:
        str: ASCII art string for the hangman
    """
    if wrong_guesses < 0:
        wrong_guesses = 0
    elif wrong_guesses >= len(HANGMAN_STAGES):
        wrong_guesses = len(HANGMAN_STAGES) - 1
    
    return HANGMAN_STAGES[wrong_guesses]

def display_word_progress(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores.
    
    Args:
        word (str): The word to guess
        guessed_letters (set): Set of guessed letters
        
    Returns:
        str: Word with guessed letters shown and others as underscores
    """
    display = ""
    for letter in word:
        if letter.upper() in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
