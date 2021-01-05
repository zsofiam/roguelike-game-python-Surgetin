import os


def display_board(board):
    os.system('clear')
    print(" " + "_" * 3 * (len(board[0])))
    for i in range(len(board)):
        if i == len(board) - 1:
            print("|", end="")
            for j in range(len(board[0])):
                print(board[i][j], end="")
            print("")
        else:
            print("|", end="")
            for j in range(len(board[0])):
                print(board[i][j], end="")
            print("|")
    print(" " + "_" * 3 * (len(board[0])))

