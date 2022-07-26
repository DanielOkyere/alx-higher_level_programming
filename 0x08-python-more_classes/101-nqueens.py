#!/usr/bin/python3
"""
nqueens backtrack program to print the coordinates of nqueens
on an n x n grid
"""

from sys import argv

if __name__ == "__main__":
    global N
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    def printSolution(board):
        for i in range(N):
            for j in range(n):
                print(board[i][j], end="")
            print()

    def isSafe(board, row, col):
        #Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        #Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        #Check lower diagonal on left side
        for i, j in zip(range(row, N, 1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solveNQUtil(board, col):
        if col >= N:
            return True

        for i in range(n):
            if isSafe(board, i, col):
                board[i][col] = 1
                if solveNQUtil(board, col + 1) == True:
                    return True
                board[i][col] = 0

        return False

    def createBoard(rowCount, colCount, data):
        """creates a board of any size"""
        mat = []
        for i in range(rowCount):
            rowList = []
            for j in range(colCount):
                rowList.append(data[rowCount * i + j])
            mat.append(rowList)
        return mat

    def solveNQ():
        board = createBoard(N, N, [0])
        printSolution(board)
        return True

solveNQ()
