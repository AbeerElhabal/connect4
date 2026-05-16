# ============================================================
# player.py - Defines the Human and AI player types
# ============================================================

# ============================================================
# Player Class: Base class that holds player info
# ============================================================
class Player:

    # --------------------------------------------------------
    # __init__: Store the player's name and assigned piece
    # --------------------------------------------------------
    def __init__(self, name, piece):
        self.name = name    # Player's display name
        self.piece = piece  # 1 for Human, 2 for AI

# ============================================================
# HumanPlayer Class: Inherits from Player
# Handles input and validation from the human user
# ============================================================
class HumanPlayer(Player):

    # --------------------------------------------------------
    # __init__: Set up human player with name and piece
    # --------------------------------------------------------
    def __init__(self, name, piece):
        super().__init__(name, piece)

    # --------------------------------------------------------
    # get_move: Ask the human to enter a column (1-7)
    # Keeps asking until a valid column is entered
    # --------------------------------------------------------
    def get_move(self, board):

        while True:
            try:
                # Ask user for column input (1 to 7)
                col = int(input(f"\n{self.name}'s turn - Choose a column (1-7): ")) - 1

                # Check if column is within valid range
                if col < 0 or col >= board.COLS:
                    print("  ⚠️  Invalid input! Please enter a number between 1 and 7.")
                    continue

                # Check if chosen column still has space
                if not board.is_valid_col(col):
                    print("  ⚠️  Column is full! Please choose another column.")
                    continue

                return col

            except ValueError:
                # Handle non-numeric input
                print("  ⚠️  Invalid input! Please enter a number.")

# ============================================================
# AIPlayer Class: Inherits from Player
# Uses Minimax algorithm to choose the best move
# ============================================================
class AIPlayer(Player):

    # --------------------------------------------------------
    # __init__: Set up AI player with name, piece, and depth
    # depth controls how many moves ahead the AI thinks
    # --------------------------------------------------------
    def __init__(self, name, piece, depth=5):
        super().__init__(name, piece)
        self.depth = depth  # Search depth for Minimax

    # --------------------------------------------------------
    # get_move: Use Minimax to find the best column to play
    # --------------------------------------------------------
    def get_move(self, board, minimax):
        print(f"\n🤖 {self.name} is thinking...")
        col = minimax.get_best_move(board, self.depth, self.piece)
        print(f"🤖 {self.name} chose column {col + 1}")
        return col