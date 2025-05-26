import random

# ======================
# 1. NUMBER GUESSING GAME
# ======================
def play_guessing():
    print("\n=== NUMBER GUESSING ===")
    secret = random.randint(1, 100)
    guesses = 0
    
    while True:
        try:
            guess = int(input("Guess (1-100): "))
            guesses += 1
            
            diff = abs(guess - secret)
            
            if guess == secret:
                print(f"Correct! You won in {guesses} guesses!")
                break
            elif diff <= 5:
                print("Boiling hot!")
            elif diff <= 10:
                print("Hot!")
            elif diff <= 20:
                print("Warm")
            elif diff <= 40:
                print("Cold")
            else:
                print("Freezing cold!")
                
        except ValueError:
            print("Please enter a number")

# ======================
# 2. PIG DICE GAME
# ======================
def play_pig():
    print("\n=== PIG DICE ===")
    score = 0
    
    while True:
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")
        
        if roll == 1:
            print("Oops! Rolled a 1. Turn over.")
            score = 0
            break
        else:
            score += roll
            print(f"Current turn score: {score}")
            
            choice = input("Roll again or hold? (r/h): ").lower()
            if choice == 'h':
                break
    
    print(f"Your total score: {score}\n")

# ======================
# 3. ROCK-PAPER-SCISSORS
# ======================
def play_rps():
    print("\n=== ROCK-PAPER-SCISSORS ===")
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    
    player = input("Choose (rock/paper/scissors): ").lower()
    while player not in choices:
        player = input("Invalid choice. Try again: ").lower()
    
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("Tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
    print()

# ======================
# 4. WHEEL OF FORTUNE
# ======================
def play_wheel():
    print("\n=== WHEEL OF FORTUNE ===")
    words = ["PYTHON", "HANGMAN", "PROGRAMMING", "COMPUTER"]
    word = random.choice(words)
    guessed = []
    attempts = 6
    
    while attempts > 0:
        masked = [letter if letter in guessed else '_' for letter in word]
        print(' '.join(masked))
        
        if '_' not in masked:
            print("You won!")
            break
            
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            print("Correct!")
            guessed.append(guess)
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left")
    
    if attempts == 0:
        print(f"Game over! The word was: {word}")
    print()

# ======================
# MAIN MENU
# ======================
def main_menu():
    while True:
        print("\n=== GAME COLLECTION ===")
        print("1. Number Guessing")
        print("2. Pig Dice")
        print("3. Rock-Paper-Scissors")
        print("4. Wheel of Fortune")
        print("5. Quit")
        
        choice = input("Select game (1-5): ")
        
        if choice == "1":
            play_guessing()
        elif choice == "2":
            play_pig()
        elif choice == "3":
            play_rps()
        elif choice == "4":
            play_wheel()
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

# Start the program
if __name__ == "__main__":
    print("Welcome to Python Game Collection!")
    main_menu()
