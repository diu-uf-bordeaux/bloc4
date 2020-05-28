from enum import Enum

class Color(Enum):
    BLACK = 1
    WHITE = 2

    def __repr__(self):
        return Color.STRINGS[self.value]

# One peculiarity of Enums, static variables must be defined outside
# the class
Color.STRINGS = { 1: "B", 2: "W" }

class Board():
    # One peculiarity of keyword args, that they are references
    # defined once and for all. You must not copy them for fear of
    # strange aliasing results.
    def __init__(self, moves = []):
        if (moves == []):
            self.moves = []
        else:
            self.moves = moves

    def __repr__(self):
        return "moves={}".format(self.moves)

    def get_move(self, color):
        old_moves = [ m[0] for m in self.moves ]
        if old_moves == []:
            return [1, color]
        else:
            return [max(old_moves) + 1, color]

print("--IMPERATIVE")
global_board = Board()  # global state

def play(board, color):
    m = board.get_move(color)
    # Modify board 'in place'
    board.moves.append(m)

print(Color.WHITE)
play(global_board, Color.WHITE)
play(global_board, Color.BLACK)
print(global_board)

print("--FUNCTIONAL")
def play(board, color):
    m = board.get_move(color)
    # Return new independent board
    return Board(moves = \
                    board.moves + [m])

board1 = Board()
board2 = play(board1, Color.WHITE)
board3 = play(board2, Color.BLACK)
print(board1)
print(board2)
print(board3)
