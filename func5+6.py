'''
This is function five from the notebook
It chooses randomly which player goes first
'''
import random

def choose_first():
    player = random.randint(1,2)
    if player == 1:
        print('Player 1 goes first!')
    else:
        print('Player 2 goes first!')

'''
This is function six from the notebook
It checks if the selected space is available on the board
Returns True if available, False otherwise
'''
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False
