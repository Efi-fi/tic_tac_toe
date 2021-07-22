import random as rnd


def make_move(board, level):
    """
    Choosing algorithm for comp.
    """
    if level == 'AI':
        return ai_move(board)
    elif level == 'Random':
        return random_move(board)
    elif level == 'Hard':
        return hard_move(board)
    elif level == 'Low':
        return low_move(board)


def ai_move(board):
    """
    Chooses cell according AI-output.
    """
    return random_move(board)  # temporary


def random_move(board):
    """
    Chooses random empty cell.
    """
    return rnd.choice([i for i, char in enumerate(board) if char == ' '])


def hard_move(board):
    """
    Chooses empty cell, that win.
    """
    return random_move(board)  # temporary


def low_move(board):
    """
    Chooses empty cell, that another player win.
    """
    template = [3, 6, 7, 5, 1, 2, 0, 8, 4]  # Move sequence
    template.reverse()
    while board[template[-1]] != ' ':
        template.pop()
    return template.pop()
