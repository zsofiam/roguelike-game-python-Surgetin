import os


def display_board(board):
    os.system('clear')
    print("" + "🧱"  * (len(board[0]) + 17))
    for i in range(len(board)):
        if i == len(board) - 1 or i == len(board) - 2:
            print("🧱", end="")
            for j in range(len(board[0])):
                print(board[i][j], end="")
            print("")
        else:
            print("🧱", end="")
            for j in range(len(board[0])):
                print(board[i][j], end="")
            print("🧱")
    print("" + "🧱"  * (len(board[0]) + 17))


def display_attributes(player, level):
    print(f'LEVEL {level}')
    print("Health:", player["health"], "Damage:", 60, "Soak:", 10)