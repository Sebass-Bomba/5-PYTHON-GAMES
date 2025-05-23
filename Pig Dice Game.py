import random

def play_pig():
    """Main game function for Pig dice game"""
    players = ["Player 1", "Player 2"]
    scores = [0, 0]
    current_player = 0
    
    print("\n=== PIG DICE GAME ===")
    print("First to 100 points wins!\n")
    
    while True:
        print(f"{players[current_player]}'s turn")
        print(f"Current score: {scores[current_player]}")
        turn_score = 0
        
        while True:
            choice = input("Roll or Hold? (r/h): ").lower()
            
            if choice == 'r':
                roll = random.randint(1, 6)
                print(f"You rolled: {roll}")
                
                if roll == 1:
                    print("Oops! Rolled a 1. Turn over.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"Turn total: {turn_score}")
                    print(f"Potential total: {scores[current_player] + turn_score}")
            
            elif choice == 'h':
                scores[current_player] += turn_score
                print(f"Score saved. {players[current_player]} now has {scores[current_player]}")
                break
            
            else:
                print("Invalid choice. Enter 'r' to roll or 'h' to hold.")
        
        # Check for winner
        if scores[current_player] >= 100:
            print(f"\n{players[current_player]} wins with {scores[current_player]} points!")
            break
        
        # Switch player
        current_player = 1 - current_player
        print("\n" + "="*30 + "\n")

def show_rules():
    """Display game rules"""
    print("\n=== PIG DICE RULES ===")
    print("1. Players take turns rolling a die")
    print("2. Roll as many times as you want to accumulate points")
    print("3. If you roll a 1, you lose all points for that turn")
    print("4. Choose 'hold' to save your turn points to your total")
    print("5. First player to reach 100 points wins!\n")
    input("Press Enter to return to menu...")

def main_menu():
    """Display main menu"""
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play Pig Dice")
        print("2. View Rules")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            play_pig()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1-3.")

# Start the game
if __name__ == "__main__":
    print("Welcome to Pig Dice!")
    main_menu()