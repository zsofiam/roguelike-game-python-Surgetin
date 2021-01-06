def create_board(width, height, level):
    board = [[0 for x in range(width)] for y in range(height)]
    for i in range(height):
        for j in range(width):
            board[i][j] = "   "
    board = create_walls(board, width, height, level)
    return board


def create_walls(board, width, height, level):
    wall_1_row = height // 3 - 1
    wall_1_length = width // 2 + width // (6-level)
    wall_2_row = height * 2 // 3 + 1
    print(wall_2_row)
    wall_2_length = width // 2 + width // (6-level)
    for i in range(wall_1_length):
        board[wall_1_row][i] = " - "
    for i in range(wall_2_length):
        board[wall_2_row][width - 1 - i] = " - "
    return board


def place_objects_on_board(board):
    pass


def put_player_on_board(board, player):
    board[player["row"] - 1][player["column"] - 1] = player["icon"]


# def put_enemies_on_board(board, enemies):
#     board[enemies["row"] - 1][enemies["column"] - 1] = enemies["icon"]