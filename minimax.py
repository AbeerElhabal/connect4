# ============================================================
# minimax.py - Contains the Minimax Algorithm logic
# ============================================================

# Import random to break ties between equal moves
import random

# ============================================================
# Minimax Class: Implements the Minimax decision algorithm
# ============================================================
class Minimax:

    # --------------------------------------------------------
    # Constants: Scores used to evaluate board positions
    # --------------------------------------------------------
    WIN_SCORE  = 100000   # Score for a winning position
    LOSE_SCORE = -100000  # Score for a losing position

    # --------------------------------------------------------
    # __init__: Store which piece belongs to AI and Human
    # --------------------------------------------------------
    def __init__(self, ai_piece, human_piece):
        self.ai_piece    = ai_piece
        self.human_piece = human_piece

    # --------------------------------------------------------
    # score_window: Score a group of 4 cells (a "window")
    # Gives points based on how many AI or Human pieces exist
    # --------------------------------------------------------
    def score_window(self, window, piece):
        opponent = self.human_piece if piece == self.ai_piece else self.ai_piece
        score = 0

        # Best case: all 4 are AI pieces
        if window.count(piece) == 4:
            score += 100

        # Good case: 3 AI pieces and 1 empty
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5

        # Okay case: 2 AI pieces and 2 empty
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        # Bad case: opponent has 3 pieces and 1 empty (block them)
        if window.count(opponent) == 3 and window.count(0) == 1:
            score -= 4

        return score

    # --------------------------------------------------------
    # score_board: Calculate total score for the whole board
    # Checks all directions: horizontal, vertical, diagonal
    # --------------------------------------------------------
    def score_board(self, board, piece):
        score = 0
        grid  = board.grid
        rows  = board.ROWS
        cols  = board.COLS

        # Prefer playing in the center column
        center_col   = [int(grid[r][cols // 2]) for r in range(rows)]
        center_count = center_col.count(piece)
        score += center_count * 3

        # Score all horizontal windows
        for r in range(rows):
            for c in range(cols - 3):
                window = list(grid[r][c:c + 4])
                score += self.score_window(window, piece)

        # Score all vertical windows
        for c in range(cols):
            for r in range(rows - 3):
                window = [grid[r + i][c] for i in range(4)]
                score += self.score_window(window, piece)

        # Score all diagonal windows (bottom-left to top-right)
        for r in range(rows - 3):
            for c in range(cols - 3):
                window = [grid[r + i][c + i] for i in range(4)]
                score += self.score_window(window, piece)

        # Score all diagonal windows (top-left to bottom-right)
        for r in range(3, rows):
            for c in range(cols - 3):
                window = [grid[r - i][c + i] for i in range(4)]
                score += self.score_window(window, piece)

        return score

    # --------------------------------------------------------
    # is_terminal: Check if the game has reached an end state
    # --------------------------------------------------------
    def is_terminal(self, board):
        return (
            board.check_winner(self.ai_piece) or
            board.check_winner(self.human_piece) or
            board.is_full()
        )

    # --------------------------------------------------------
    # minimax: Recursive function that simulates future moves
    # maximizing=True  → AI's turn  (wants highest score)
    # maximizing=False → Human's turn (wants lowest score)
    # --------------------------------------------------------
    def minimax(self, board, depth, maximizing):
        import copy

        # Base case: game over or max depth reached
        if depth == 0 or self.is_terminal(board):
            if board.check_winner(self.ai_piece):
                return self.WIN_SCORE
            elif board.check_winner(self.human_piece):
                return self.LOSE_SCORE
            else:
                return self.score_board(board, self.ai_piece)

        valid_cols = board.get_valid_cols()

        if maximizing:
            # AI tries to maximize its score
            best_score = float('-inf')
            for col in valid_cols:
                new_board = copy.deepcopy(board)
                new_board.drop_piece(col, self.ai_piece)
                score = self.minimax(new_board, depth - 1, False)
                best_score = max(best_score, score)
            return best_score

        else:
            # Human tries to minimize AI's score
            best_score = float('inf')
            for col in valid_cols:
                new_board = copy.deepcopy(board)
                new_board.drop_piece(col, self.human_piece)
                score = self.minimax(new_board, depth - 1, True)
                best_score = min(best_score, score)
            return best_score

    # --------------------------------------------------------
    # get_best_move: Find the column with the highest score
    # This is what the AI calls to decide its move
    # --------------------------------------------------------
    def get_best_move(self, board, depth, piece):
        import copy

        best_score = float('-inf')
        best_cols  = []

        for col in board.get_valid_cols():
            new_board = copy.deepcopy(board)
            new_board.drop_piece(col, self.ai_piece)
            score = self.minimax(new_board, depth - 1, False)

            if score > best_score:
                best_score = score
                best_cols  = [col]       # New best found
            elif score == best_score:
                best_cols.append(col)    # Tie → add to options

        # Pick randomly among equally good moves
        return random.choice(best_cols)