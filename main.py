
import random
from IPython.display import clear_output

def choose_first():
    '''
    This is function five from the notebook
    It chooses randomly which player goes first
    '''
    player = random.randint(1,2)
    print(f'{player} goes first!')

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



def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return(# ROWS:    
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or    
    # COLUMS:    
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    # DIAGONALS:
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

#step 7
# random function space_check defined for code to run. 
# This will be deleted when all parts of the project are together
def space_check():

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#step 8

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

