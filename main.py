# ============================================================
# main.py - Entry point of the Connect 4 game
# ============================================================

# Import the Game class to start and control the game
from game import Game

# ============================================================
# get_player_name: Ask the user to enter their name
# ============================================================
def get_player_name():
    while True:
        name = input("\nEnter your name: ").strip()

        # Validate that name is not empty
        if name == "":
            print("  ⚠️  Name cannot be empty! Please enter your name.")
            continue

        return name

# ============================================================
# get_game_mode: Ask the user to choose game mode
# ============================================================
def get_game_mode():
    print("\n  Select Game Mode:")
    print("  [1] Human vs AI")
    print("  [2] Human vs Human")

    while True:
        choice = input("\n  Enter choice (1 or 2): ").strip()

        if choice == "1":
            return "hvai"
        elif choice == "2":
            return "hvh"
        else:
            print("  ⚠️  Invalid choice! Please enter 1 or 2.")

# ============================================================
# play_again: Ask the user if they want to play another round
# ============================================================
def play_again():
    while True:
        choice = input("\nDo you want to play again? (yes / no): ").strip().lower()

        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("  ⚠️  Please enter yes or no.")

# ============================================================
# main: Main function that runs the full game session
# ============================================================
def main():

    print("\n" + "=" * 35)
    print("         CONNECT 4 - AI Game")
    print("=" * 35)

    # Get player name and game mode before starting
    name = get_player_name()
    mode = get_game_mode()

    while True:
        # Create a new game and run it
        game = Game(name, mode)
        game.run()

        # Ask if player wants to play again
        if not play_again():
            print("\n Thanks for playing! Goodbye 👋\n")
            break

# ============================================================
# Run the program only if this file is executed directly
# ============================================================
if __name__ == "__main__":
    main()