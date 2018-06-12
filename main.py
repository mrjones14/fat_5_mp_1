import random

def choose_first():
    '''
    This is function five from the notebook
    It chooses randomly which player goes first
    '''
    player = random.randint(1,2)
    if player == 1:
        print('Player 1 goes first!')
    else:
        print('Player 2 goes first!')


def space_check(board, position):
    '''
    This is function six from the notebook
    It checks if the selected space is available on the board
    Returns True if available, False otherwise
    '''
    if board[position] == ' ':
        return True
    else:
        return False
