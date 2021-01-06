import util
import engine
import ui
import random
import sys


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
    enemies = []
    for _ in range(3):
        enemies.append({
        "row": random.randint(4, BOARD_HEIGHT - 3),
        "column": random.randint(4, BOARD_WIDTH - 3),
        "icon": ' ' + ENEMY_ICON + '',
        "power": 60
        })
    return enemies


def create_items():
    items = []
    for _ in range(5):
        for _ in range(5):
            valami = random_items_generator()
        item = {
            "row": random.randint(4, BOARD_HEIGHT - 3),
            "column": random.randint(4, BOARD_WIDTH - 3),
            "icon": ' ' + valami + ''}
        items.append(item)
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
    if enemy_is_on_field:
        enemies.pop(index_to_delete)


def handle_meets_with_items(items, player):
    index_to_delete = 0
    item_is_on_field = False
    for index, item in enumerate(items):
        if item["row"] == player["row"] and item["column"] == player["column"]:
            player["health"] += 60
            item_is_on_field = True
            index_to_delete = index
    if item_is_on_field:
        items.pop(index_to_delete)
    

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


def handle_exit(player, level):
    if player["row"] == BOARD_HEIGHT-1 and player["column"] == BOARD_WIDTH-1:
        player["row"] = PLAYER_START_X
        player["column"] = PLAYER_START_Y
        level += 1
        if level == 3:
            print("Hurray!")
            sys.exit()
        process_game(level, player)
        

def move_enemies(enemies, player):
    for enemy in enemies:
        if enemy["column"] == player["column"] and enemy["row"] < player["row"]:
            enemy["row"] += 1
        elif enemy["column"] == player["column"] and enemy["row"] > player["row"]:
            enemy["row"] -= 1
        elif enemy["row"] == player["row"] and enemy["column"] < player["column"]:
            enemy["column"] += 1
        elif enemy["row"] == player["row"] and enemy["column"] > player["column"]:
            enemy["column"] -= 1
        elif enemy["row"] < player["row"]:
            enemy["row"] += 1
        else:
            enemy["row"] -= 1
    handle_meets(enemies, player)


def process_game(level, player):
    enemies = create_enemies()
    items = create_items()
    
    is_running = True
    while is_running:
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        engine.put_player_on_board(board, player)
        engine.put_objects_on_board(board, items)
        engine.put_enemies_on_board(board, enemies)
        ui.display_board(board)
        ui.display_attributes(player)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's' or key == "w" or key == 'a' or key == 'd':
            handle_exit(player, level)
            move_if_valid(key, player, board)
            handle_meets(enemies, player)
            if not is_player_alive(player):
                print("Sorry, you died.")
                is_running = False
            handle_meets_with_items(items, player)
            move_enemies(enemies, player)
        elif key == 'i':
            print_inventory()
        else:
            continue


def main():
    player = create_player()
    level = 1
    process_game(level, player)


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


def item_details():
    pass


if __name__ == '__main__':
    main()


# 🌳🌳
# 🧱🧱