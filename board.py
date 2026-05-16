# ============================================================
# board.py - Handles the Connect 4 board structure
# ============================================================

# ============================================================
# Board Class: Represents the game board and its operations
# ============================================================
class Board:

    # --------------------------------------------------------
    # Constants: Define board dimensions and player pieces
    # --------------------------------------------------------
    ROWS = 6
    COLS = 7
    EMPTY = 0
    HUMAN_PIECE = 1
    AI_PIECE = 2

    # --------------------------------------------------------
    # __init__: Create an empty board using a 2D Python list
    # --------------------------------------------------------
    def __init__(self):
        self.grid = [[0] * self.COLS for _ in range(self.ROWS)]

    # --------------------------------------------------------
    # print_board: Display the board in the terminal
    # --------------------------------------------------------
    def print_board(self):
        print("\n  1   2   3   4   5   6   7")
        print("+" + "---+" * self.COLS)
        for row in self.grid:
            print("|", end="")
            for cell in row:
                if cell == self.HUMAN_PIECE:
                    print(" X |", end="")
                elif cell == self.AI_PIECE:
                    print(" O |", end="")
                else:
                    print("   |", end="")
            print()
            print("+" + "---+" * self.COLS)

    # --------------------------------------------------------
    # is_valid_col: Check if a column has space for a new piece
    # --------------------------------------------------------
    def is_valid_col(self, col):
        return self.grid[0][col] == self.EMPTY

    # --------------------------------------------------------
    # get_valid_cols: Return list of all columns that are valid
    # --------------------------------------------------------
    def get_valid_cols(self):
        return [c for c in range(self.COLS) if self.is_valid_col(c)]

    # --------------------------------------------------------
    # drop_piece: Place a piece in the lowest available row
    # --------------------------------------------------------
    def drop_piece(self, col, piece):
        for row in range(self.ROWS - 1, -1, -1):
            if self.grid[row][col] == self.EMPTY:
                self.grid[row][col] = piece
                return row

    # --------------------------------------------------------
    # is_full: Check if the board is completely full (draw)
    # --------------------------------------------------------
    def is_full(self):
        return len(self.get_valid_cols()) == 0

    # --------------------------------------------------------
    # check_winner: Check if a given piece has won the game
    # --------------------------------------------------------
    def check_winner(self, piece):

        # Check horizontal win
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.grid[r][c + i] == piece for i in range(4)):
                    return True

        # Check vertical win
        for r in range(self.ROWS - 3):
            for c in range(self.COLS):
                if all(self.grid[r + i][c] == piece for i in range(4)):
                    return True

        # Check diagonal win (bottom-left to top-right)
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if all(self.grid[r + i][c + i] == piece for i in range(4)):
                    return True

        # Check diagonal win (top-left to bottom-right)
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.grid[r - i][c + i] == piece for i in range(4)):
                    return True

        return False