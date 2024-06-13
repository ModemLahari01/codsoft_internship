import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors Game")
        print("Enter 'quit' to end the game.")
        
        # User Input
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice == 'quit':
            break
        
        # Computer Selection
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        # Game Logic
        result = determine_winner(user_choice, computer_choice)
        
        # Display Result
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        
        # Score Tracking
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"\nYour Score: {user_score}")
        print(f"Computer's Score: {computer_score}")

if __name__ == "__main__":
    main()
