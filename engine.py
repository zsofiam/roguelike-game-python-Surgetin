def create_board(width, height):
    board = [[0 for x in range(width)] for y in range(height)]
    for i in range(height):
        for j in range(width):
            board[i][j] = "   "
    return board


def place_objects_on_board(board):
    pass


def put_player_on_board(board, player):
    board[player["row"]][player["column"]] = player["icon"]


# def put_enemies_on_board(board, enemies):
#     board[enemies["row"] - 1][enemies["column"] - 1] = enemies["icon"]
