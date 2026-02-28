import random

def get_user_choice():
    """Get and validate user's choice."""
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        if choice in ['rock', 'paper', 'scissors', 'quit']:
            return choice
        print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'quit'.")

def get_computer_choice():
    """Generate computer's random choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round."""
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper')
    }
    
    if (user_choice, computer_choice) in winning_combinations:
        return 'user'
    else:
        return 'computer'

def display_choices(user_choice, computer_choice):
    """Display the choices made by user and computer."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def display_result(winner):
    """Display the result of the round."""
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win this round!")
    else:
        print("Computer wins this round!")

def display_score(user_score, computer_score):
    """Display the current score."""
    print(f"\nScore - You: {user_score}, Computer: {computer_score}")

def play_game():
    """Main game loop."""
    print("Welcome to Rock Paper Scissors!")
    print("Enter 'quit' at any time to exit the game.\n")
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            break
        
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        
        winner = determine_winner(user_choice, computer_choice)
        display_result(winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        display_score(user_score, computer_score)
        print("-" * 30)
    
    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations! You won overall!")
    elif computer_score > user_score:
        print("Computer won overall. Better luck next time!")
    else:
        print("It's a tie overall! Great game!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()