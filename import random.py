import random

def guessing_game():
    """
    A simple number guessing game where the player tries to guess a random number between 1 and 100.
    Provides temperature-based hints (boiling, hot, warm, cold, freezing) based on how close the guess is.
    """
    # Initialize game variables
    secret_number = random.randint(1, 100)
    guess_count = 0

    while True:
        try:
            # Get user input and validate it's a number
            guess = int(input("\nGuess a number between 1 and 100: "))
            guess_count += 1

            # Calculate how far the guess is from the secret number
            difference = abs(guess - secret_number)

            # Provide appropriate feedback based on the difference
            if guess == secret_number:
                print(f"\nCongratulations! You guessed the number in {guess_count} tries!")
                if play_again():
                    return True  # Play again
                else:
                    return False  # Return to main menu
            elif difference <= 5:
                print("Boiling! You're extremely close!")
            elif difference <= 10:
                print("Hot! You're getting very close!")
            elif difference <= 20:
                print("Warm! You're in the right range.")
            elif difference <= 40:
                print("Cold! You need to get closer.")
            else:
                print("Freezing! You're way off.")
                
        except ValueError:
            print("Please enter a valid number between 1 and 100.")

def play_again():
    """
    Asks the player if they want to play another round.
    Returns True if they want to play again, False otherwise.
    """
    while True:
        play = input("\nWould you like to play again? (yes/no) ").lower()
        
        if play in ["y", "yes"]:
            print("\nStarting a new game...\n")
            return True
        elif play in ["n", "no"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def show_instructions():
    """Displays game instructions to the player"""
    print("\n=== NUMBER GUESSING GAME INSTRUCTIONS ===")
    print("1. The computer will generate a random number between 1-100")
    print("2. You need to guess the secret number")
    print("3. After each guess, you'll get a temperature hint:")
    print("   - Boiling: Within 5 numbers")
    print("   - Hot: Within 10 numbers")
    print("   - Warm: Within 20 numbers")
    print("   - Cold: Within 40 numbers")
    print("   - Freezing: More than 40 away")
    print("4. Try to guess the number in as few attempts as possible!\n")
    input("Press Enter to return to the main menu...")

def main_menu():
    """Displays the main menu and handles user selection"""
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play Game")
        print("2. View Instructions")
        print("3. Exit")
        
        choice = input("Please select an option (1-3): ")
        
        if choice == "1":
            print("\nStarting new game... Good luck!\n")
            if not guessing_game():  # If player chooses not to play again
                continue
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    main_menu()