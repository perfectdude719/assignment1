import math

#function for calculating the rculeadian distance

def manhattan(self):
    distance = 0
    for i in range(3):
        for j in range(3):
            if self.board[i][j] != 0: ##skip the zero
                x, y = divmod(self.board[i][j]-1, 3) ##lma na2st 1 it worked just fine 
                distance += abs(x - i) + abs(y - j) ##sum all the distances needed
    return distance

def generate_moves(board):
    """
    Generate all valid moves (Up, Down, Left, Right) based on the position of the empty space (0).
    """
    moves = []
    zero_index = board.index(0)  # Position of the empty space (0)
    x, y = divmod(zero_index, 3)

    if x > 0:  # Move Up
        moves.append("Up")
    if x < 2:  # Move Down
        moves.append("Down")
    if y > 0:  # Move Left
        moves.append("Left")
    if y < 2:  # Move Right
        moves.append("Right")

    return moves
