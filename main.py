import util
import engine
import ui
import random

PLAYER_ICON = '🧙‍'
ENEMY_ICON = '💀'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = {
        "row": PLAYER_START_X,
        "column": PLAYER_START_Y,
        "icon": ' ' + PLAYER_ICON + '',
        "health": 100
    }

    return player


def create_enemies():
    enemies = [{
        "row": random.randint(4, 17),
        "column": random.randint(4, 27),
        "icon": ' ' + ENEMY_ICON + '',
        "power": 60
        },{
        "row": random.randint(4, 17),
        "column": random.randint(4, 27),
        "icon": ' ' + ENEMY_ICON + '',
        "power": 60
        },{
        "row": random.randint(4, 17),
        "column": random.randint(4, 27),
        "icon": ' ' + ENEMY_ICON + '',
        "power": 60
        }]

    return enemies


def create_items():
    for _ in range(5):
        valami = random_items_generator()
    items = {
        "row": random.randint(4, 17),
        "column": random.randint(4, 27),
        "icon": ' ' + valami + ''}

    return items
    

def row_is_in_range(row):
    if row >= 0 and row < BOARD_HEIGHT:
        return True
    return False


def column_is_in_range(column):
    if column >= 0 and column < BOARD_WIDTH:
        return True
    return False


def handle_meets(enemies, player):
    index_to_delete = 0
    enemy_is_on_field = False
    for index, enemy in enumerate(enemies):
        if enemy["row"] == player["row"] and enemy["column"] == player["column"]:
            player["health"] -= 60
            enemy_is_on_field = True
            index_to_delete = index
            if enemy["power"] > player["health"]:
                print("Béna")
    if enemy_is_on_field:
        enemies.pop(index_to_delete)
    

def move_if_valid(key, player, board):
    row = player["row"]
    column = player["column"]
    if key == "s":
        new_row = player["row"] + 1
        if row_is_in_range(new_row):
            player["row"] += 1
            board[row][column] = "   "
    if key == "w":
        new_row = player["row"] - 1
        if row_is_in_range(new_row):
            player["row"] -= 1
            board[row][column] = "   "
    if key == "a":
        new_column = player["column"] - 1
        if column_is_in_range(new_column):
            player["column"] -= 1
            board[row][column] = "   "
    if key == "d":
        new_column = player["column"] + 1
        if column_is_in_range(new_column):
            player["column"] += 1
            board[row][column] = "   "


def is_player_alive(player):
    if player["health"] <= 0:
        return False
    return True


def main():
    player = create_player()
    enemies = create_enemies()
    items = create_items()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        engine.put_enemies_on_board(board, enemies)
        engine.put_objects_on_board(board, items)
        util.clear_screen()
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's' or key == "w" or key == 'a' or key == 'd':
            move_if_valid(key, player, board)
            handle_meets(enemies, player)
            if not is_player_alive(player):
                print("Sorry, you died.")
                is_running = False
        elif key == 'i':
            print_inventory()
        else:
            pass


def print_inventory():
    util.clear_screen()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    print("Inventory")
    print("___________________________________________________")
    print("NAME                AMOUNT                ATTRIBUTE")
    print()
    key = util.key_pressed()
    if key == "i":
        ui.display_board(board)
    else:
        pass
        util.clear_screen()


# def player_stat():
#     health = 100
#     damage = 30
#     money = 0
#     food = 0
#     while is_running:
#         pass


def random_items_generator():
    list_of_items = []
    item = {
        "money": "💵",
        "food": "🍖",
        "armor": "🛡️ "}

    for _ in range(10):
        key = random.choice(list(item))
        list_of_items.append(item[key])

    valami2 = random.choice(list_of_items)

    return valami2


def put_items_on_board():
    pass


def item_details():
    pass


if __name__ == '__main__':
    main()


# 🌳🌳
# 🧱🧱