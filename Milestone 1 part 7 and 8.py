
# coding: utf-8

# In[1]:


def full_board_check(board):
    if space_check == True:
        return False
    else:
        return True


# In[4]:


def player_choice(board):
    position = 0
    int(input("Please type a number from 1-9 to indicate where you would like to place your next marker "))
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        return player_choice()
    return position

