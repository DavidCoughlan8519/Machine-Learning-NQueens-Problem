import copy
import random


def get_h_cost(board):
    h = 0
    for i in range(len(board)):
        # Check every column we haven't already checked
        for j in range(i + 1, len(board)):
            # Queens are in the same row
            if board[i] == board[j]:
                h += 1
                # Get the difference between the current column
                # and the check column
            offset = j - i
            # To be a diagonal, the check column value has to be
            # equal to the current column value +/- the offset
            if (board[i] == board[j] - offset or board[i] == board[j] + offset):
                h += 1
    return h


def make_move_steepest_hill(board):
    moves = {}
    for col in range(len(board)):
        best_move = board[col]
        for row in range(len(board)):
            if board[col] == row:
                # We don't need to evaluate the current
                # position, we already know the h-value
                continue
            board_copy = list(board)
            # Move the queen to the new row
            board_copy[col] = row
            moves[(col, row)] = get_h_cost(board_copy)

    best_moves = []
    h_to_beat = get_h_cost(board)
    for k, v in moves.iteritems():
        if v < h_to_beat:
            h_to_beat = v

    for k, v in moves.iteritems():
        if v == h_to_beat:
            best_moves.append(k)

    # Pick a random best move
    if (len(best_moves) > 0):
        pick = random.randint(0, len(best_moves) - 1)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board


def take_input():
    """Accepts the size of the chess board"""

    while True:
        try:
            size = int(input('What is the size of the chessboard? n = \n'))
            if (size == 1):
                print("Trivial solution, choose a board size of at least 4")
            if (size <= 3):
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")


def get_board(size):
    """Returns an n by n board"""
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def print_solutions(solutions, size):
    """Prints all the solutions in user friendly way"""
    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""

    # check row on left side
    for iy in range(col):
        if (board[row][iy] == 1):
            return False

    ix, iy = row, col
    while (ix >= 0 and iy >= 0):
        if (board[ix][iy] == 1):
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while (jx < size and jy >= 0):
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board, col, size):
    """Use backtracking to find all solutions"""
    # base case
    if (col >= size):
        return

    for i in range(size):
        if (is_safe(board, i, col, size)):
            board[i][col] = 1
            if (col == size - 1):
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            # backtrack
            board[i][col] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


size = take_input()

board = get_board(size)

# solutions = []

# solve(board, 0, size)

# print_solutions(solutions, size)

# print("Total solutions = {}".format(len(solutions)))

make_move_steepest_hill(board)

