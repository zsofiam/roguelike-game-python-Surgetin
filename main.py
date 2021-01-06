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


def main():
    player = create_player()
    enemies = create_enemies()
    level = 1
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level)
    
    #util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        #engine.put_enemies_on_board(board, enemies)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["row"] += 1
            engine.put_player_on_board(board, player)
            # engine.put_enemies_on_board(board, enemies)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'w':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["row"] -= 1
            engine.put_player_on_board(board, player)
            # engine.put_enemies_on_board(board, enemies)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'a':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["column"] -= 1
            engine.put_player_on_board(board, player)
            # engine.put_enemies_on_board(board, enemies)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'd':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["column"] += 1
            engine.put_player_on_board(board, player)
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
