def create_board(width, height):
    board = [[0 for x in range(width)] for y in range(height)]
    for i in range(height):
        for j in range(width):
            board[i][j] = " - "
    return board


def put_player_on_board(board, player):
    board[player["row"] - 1][player["column"] - 1] = player["icon"]