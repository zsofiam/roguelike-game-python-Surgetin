import util
import engine
import ui
import random

PLAYER_ICON = '🧙‍'
ENEMIES_ICON = '@‍'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = {
        "row": PLAYER_START_X,
        "column": PLAYER_START_Y,
        "icon": ' ' + PLAYER_ICON + ''}

    return player


def create_enemies():
    enemies = []
    for i in range(5):
        enemy = {"row": random.randint(1, BOARD_HEIGHT-1),
        "column": random.randint(1, BOARD_WIDTH-1),
        "icon": ' ' + ENEMIES_ICON + ''}
        enemies.append(enemy)

    return enemies


def row_is_in_range(row):
    if row >= 0 and row < BOARD_HEIGHT:
        return True
    return False


def column_is_in_range(column):
    if column >= 0 and column < BOARD_WIDTH:
        return True
    return False


def handle_meets():
    pass


def move_if_valid(key, player, board):
    row = player["row"]
    column = player["column"]
    if key == "s":
        new_row = player["row"] + 1
        if row_is_in_range(new_row):
            player["row"] += 1
    if key == "w":
        new_row = player["row"] - 1
        if row_is_in_range(new_row):
            player["row"] -= 1
    if key == "a":
        new_column = player["column"] - 1
        if column_is_in_range(new_column):
            player["column"] -= 1
    if key == "d":
        new_column = player["column"] + 1
        if column_is_in_range(new_column):
            player["column"] += 1
    engine.put_player_on_board(board, player)
    board[row-1][column-1] = "   "


def main():
    player = create_player()
    #enemies = create_enemies()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    #util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        #engine.put_enemies_on_board(board, enemies)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's' or key == 'w' or key == 'a' or key == 'd':
            move_if_valid(key, player, board)
            #engine.put_player_on_board(board, player)
            # engine.put_enemies_on_board(board, enemies)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'i':
            print_inventory()
        else:
            pass
        util.clear_screen()


def print_inventory():
    util.clear_screen()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    print("Inventory")
    print("___________________________________________________")
    print("NAME              AMOUNT                ATTRIBUTE")
    print()
    key = util.key_pressed()
    if key == "i":
        ui.display_board(board)
    else:
        pass
        util.clear_screen()

def player_stat():
    pass
    

def items():
    money = "💵"
    food = "🍖"
    armor = "🛡️"
    pass


if __name__ == '__main__':
    main()
