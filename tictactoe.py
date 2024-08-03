"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_moves = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X or board[row][col] == O:
                number_of_moves += 1

    if number_of_moves % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_moves.add((row,col))
    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board = copy.deepcopy(board)

    if action not in actions(board):
        raise Exception('Action Is Not Valid')

    row, col = action
    copy_board[row][col] = player(board)

    return copy_board

def check_row(board):
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
        if countX == 3:
            return X
        elif countO == 3:
            return O
        else:
            countX = 0
            countO = 0

def check_col(board):
    countX = 0
    countO = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
        if countX == 3:
            return X
        elif countO == 3:
            return O
        else:
            countX = 0
            countO = 0

def check_diag(board):
    countX = 0
    countO = 0

    for i in range(len(board)):
        if board[i][i] == X:
            countX += 1
        elif board[i][i] == O:
            countO += 1
    if countX == 3:
        return X
    elif countO == 3:
        return O

    countX = 0
    countO = 0
    for i in range(len(board)):
        if board[len(board) - 1 - i][i] == X:
            countX += 1
        elif board[len(board) - 1 - i][i] == O:
            countO += 1
    if countX == 3:
        return X
    elif countO == 3:
        return O


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board) == X:
        return X
    elif check_row(board) == O:
        return O
    elif check_col(board) == X:
        return X
    elif check_col(board) == O:
        return O
    elif check_diag(board) == X:
        return X
    elif check_diag(board) == O:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        moves = []
        for action in actions(board):
            moves.append([min_value(result(board, action)), action])
        return sorted(moves, key = lambda x: x[0], reverse = True)[0][1]

    elif player(board) == O:
        moves = []
        for action in actions(board):
            moves.append([max_value(result(board, action)), action])
        return sorted(moves, key = lambda x: x[0])[0][1]
