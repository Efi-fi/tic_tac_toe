import random as rnd


def make_move(board, level):
    if level == 'AI':
        return ai_move(board)
    elif level == 'Random':
        return random_move(board)
    elif level == 'Hard':
        return hard_move(board)
    elif level == 'Low':
        return low_move(board)


def ai_move(board):
    pass


def random_move(board):
    """
    Chooses random empty cell.
    """
    return rnd.choice([i for i, char in enumerate(board) if char == ' '])


def hard_move(board):
    """
    Chooses empty cell, that win.
    """
    pass


def low_move(board):
    """
    Chooses empty cell, that another player win.
    """
    pass
