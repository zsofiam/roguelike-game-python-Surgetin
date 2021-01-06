def create_board(width, height):
    board = [[0 for x in range(width)] for y in range(height)]
    for i in range(height):
        for j in range(width):
            board[i][j] = "   "
    return board


# def put_objects_on_board(board, items):
#     for item in items:
#         board[item["row"] - 1][item["column"] - 1] = item["icon"]


def put_player_on_board(board, player):
    board[player["row"]][player["column"]] = player["icon"]


def put_enemies_on_board(board, enemy):
    board[enemy["row"]][enemy["column"]] = enemy["icon"]