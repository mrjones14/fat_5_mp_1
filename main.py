<<<<<<< HEAD
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
=======

from IPython.display import clear_output

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
>>>>>>> master
