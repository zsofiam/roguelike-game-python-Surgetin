import util
import engine
import ui
import random
import sys
import printing_name


PLAYER_ICON = '🧙‍'
PLAYER_START_X = 7
PLAYER_START_Y = 14

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = {
        "row": PLAYER_START_X,
        "column": PLAYER_START_Y,
        "icon": ' ' + PLAYER_ICON + '',
        "health": 1000
    }
    return player


def create_enemies(level):
    enemies = []
    for _ in range(8 * level):
        for _ in range(15):
            enemy_icons = random_enemies_generator()
        enemy = {
            "row": random.randint(1, BOARD_HEIGHT - 1),
            "column": random.randint(1, BOARD_WIDTH - 1),
            "icon": ' ' + enemy_icons + ''}
        enemies.append(enemy)
    return enemies


def create_items(level):
    items = []
    for _ in range(15 - level):
        for _ in range(15):
            item_icon = random_items_generator()
        item = {
            "row": random.randint(1, BOARD_HEIGHT - 1),
            "column": random.randint(1, BOARD_WIDTH - 1),
            "icon": ' ' + item_icon + ''}
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


def handle_exit(player, level, key):
    if player["row"] == BOARD_HEIGHT-1 and player["column"] == BOARD_WIDTH-1 and key == 'd':
        player["row"] = PLAYER_START_X
        player["column"] = PLAYER_START_Y
        level += 1           
        if level == 4:
            util.clear_screen()
            printing_name.won()
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
        elif enemy["column"] > player["column"]:
            enemy["column"] -= 1
        elif enemy["column"] < player["column"]:
            enemy["column"] += 1
        else:
            enemy["row"] -= 1
    handle_meets(enemies, player)


def process_game(level, player):
    enemies = create_enemies(level)
    items = create_items(level)

    is_running = True
    while is_running:
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        engine.put_player_on_board(board, player)
        engine.put_objects_on_board(board, items)
        engine.put_enemies_on_board(board, enemies)
        ui.display_board(board)
        ui.display_attributes(player, level)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's' or key == "w" or key == 'a' or key == 'd':
            handle_exit(player, level, key)
            move_if_valid(key, player, board)
            handle_meets(enemies, player)
            if not is_player_alive(player):
                print("Sorry, you died.")
                is_running = False
            handle_meets_with_items(items, player)
            move_enemies(enemies, player)
        elif key == 'c':
            player["health"] += 10000
        else:
            continue


def main():
    printing_name.main_screen()
    player = create_player()
    level = 1
    process_game(level, player)


def random_items_generator():
    list_of_items = []
    item = {
        "2": "🍖",
        "3": "🍺",
        "4": "🍩"
        }

    for _ in range(10):
        key = random.choice(list(item))
        list_of_items.append(item[key])

    items = random.choice(list_of_items)

    return items


def random_enemies_generator():
    list_of_enemies = []
    enemy = {
        "1": "💀",
        "2": "🦈",
        "3": "🦖",
        "4": "🦀"
        }

    for _ in range(10):
        key = random.choice(list(enemy))
        list_of_enemies.append(enemy[key])

    enemies = random.choice(list_of_enemies)

    return enemies


if __name__ == '__main__':
    main()