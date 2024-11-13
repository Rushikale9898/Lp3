#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isSafe(board, row, col):
    # Check column for any queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def printBoard(board):
    for row in board:
        print(" ".join(row))
    print()

def placeQueens(board, row):
    # Base case: All queens are placed
    if row == len(board):
        printBoard(board)
        return True

    # Try placing queen in each column for current row
    for col in range(len(board)):
        if isSafe(board, row, col):
            # Place queen
            board[row][col] = 'Q'

            # Recur to place the rest of the queens
            if placeQueens(board, row + 1):
                return True  # Stop after finding the first solution

            # Backtrack if placing queen here doesn't lead to a solution
            board[row][col] = '.'

    return False

def solveNQueens(n):
    # Initialize board with '.' and place the first queen at top-left corner
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[0][0] = 'Q'  # Place the first queen in the top-left

    # Start placing the remaining queens
    if not placeQueens(board, 1):  # Start from the second row
        print("No solution found")

# Example usage for a 4x4 board
solveNQueens(8)


# In[ ]:




