#!/usr/bin/env python
# coding: utf-8

# In[28]:


sample_board = [[7,8,0,4,0,0,1,2,0],
                [6,0,0,0,7,5,0,0,9],
                [0,0,0,6,0,1,0,7,8],
                [0,0,7,0,4,0,2,6,0],
                [0,0,1,0,5,0,9,3,0],
                [9,0,4,0,6,0,0,0,5],
                [0,7,0,3,0,0,0,1,2],
                [1,2,0,0,0,7,4,0,0],
                [0,4,9,2,0,6,0,0,7]]


# In[22]:


def empty_square(board):
    ## find position of empty square
    ## note that in this board, a zero represents an empty space
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                return (row, col)
            else: 
                pass
    return None


# In[23]:


def possible_sol(board, x, y, num):
    ## for rows and columns respectively
    ## note: here, num is a tuple
    for item in range(0,9):
        if board[item][y] == num or board[x][item] == num:
            return False
        
    ## check the subsquare
    x0 = (x // 3)*3
    y0 = (y // 3)*3
    
    for i in range(x0,x0+3):
        for j in range(y0,y0+3):
            if i != x and j != y and board[i][j] == num:
                return False
    return True


# In[29]:


def solve_board(board):
    ## base case
    emp_square = empty_square(board)
    if emp_square == None:
        return True
    ## recursive case 
    else:
        x = emp_square[0]
        y = emp_square[1]
    for num in range(1,10):
        if possible_sol(board, x, y, num):
            board[x][y] = num
            if solve_board(board):
                return True
            board[x][y] = 0
    return False


# In[30]:


solve_board(sample_board)


# In[33]:


def display_board(board):
    for x in range(0,9):
        end_box = ""
        if x == 3 or x == 6:
            print("......................")
        for y in range(len(board[x])):
            if y == 3 or y == 6:
                end_box += "| "
            end_box += str(board[x][y])+" "
        print(end_box)


# In[34]:


def final_board(board):
    if solve_board(board) == False:
        print("sudoku board is unsolvable")
    else:
        print(solve_board(board))
    display_board(board)


# In[36]:


final_board(sample_board)


# In[ ]:


## credits to computerphile: https://www.youtube.com/watch?v=G_UYXzGuqvM&t=219s
##  and tech with tim: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
## particularly for help of structure of the recursive case

