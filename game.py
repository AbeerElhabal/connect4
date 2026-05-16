# ============================================================
# game.py - Controls the overall flow of the game
# ============================================================

# Import the three main components of the game
from board import Board
from player import HumanPlayer, AIPlayer
from minimax import Minimax

# ============================================================
# Game Class: Manages turns, checks results, runs the loop
# ============================================================
class Game:

    # --------------------------------------------------------
    # __init__: Set up the board, players, and minimax engine
    # --------------------------------------------------------
    def __init__(self, human_name, mode):
        self.board   = Board()
        self.mode    = mode

        self.minimax = Minimax(
            ai_piece    = Board.AI_PIECE,
            human_piece = Board.HUMAN_PIECE
        )

        self.player1 = HumanPlayer(human_name, Board.HUMAN_PIECE)

        if self.mode == "hvai":
            self.player2 = AIPlayer("AI", Board.AI_PIECE, depth=5)
        else:
            self.player2 = HumanPlayer("Player 2", Board.AI_PIECE)

    # --------------------------------------------------------
    # display_welcome: Show welcome message at game start
    # --------------------------------------------------------
    def display_welcome(self):
        print("\n" + "=" * 35)
        print("       Welcome to Connect 4!")
        print("=" * 35)
        print(f"  {self.player1.name}  (X)  vs  {self.player2.name}  (O)")
        print("=" * 35)

    # --------------------------------------------------------
    # switch_turn: Alternate between player1 and player2
    # --------------------------------------------------------
    def switch_turn(self, current):
        return self.player2 if current == self.player1 else self.player1

    # --------------------------------------------------------
    # play_turn: Handle a single turn for the current player
    # --------------------------------------------------------
    def play_turn(self, current_player):
        self.board.print_board()

        if isinstance(current_player, AIPlayer):
            col = current_player.get_move(self.board, self.minimax)
        else:
            col = current_player.get_move(self.board)

        self.board.drop_piece(col, current_player.piece)

    # --------------------------------------------------------
    # check_result: Check if current player won or board full
    # --------------------------------------------------------
    def check_result(self, current_player):
        if self.board.check_winner(current_player.piece):
            self.board.print_board()
            print("\n" + "=" * 35)
            print(f"  🎉 {current_player.name} wins! Congratulations!")
            print("=" * 35 + "\n")
            return "win"

        if self.board.is_full():
            self.board.print_board()
            print("\n" + "=" * 35)
            print("        🤝 It's a Draw!")
            print("=" * 35 + "\n")
            return "draw"

        return "continue"

    # --------------------------------------------------------
    # run: Main game loop that keeps running until game ends
    # --------------------------------------------------------
    def run(self):
        self.display_welcome()
        current_player = self.player1

        while True:
            self.play_turn(current_player)
            result = self.check_result(current_player)
            if result in ("win", "draw"):
                break
            current_player = self.switch_turn(current_player)