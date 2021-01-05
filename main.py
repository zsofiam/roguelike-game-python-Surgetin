import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = {
    "row": PLAYER_START_X,
    "column": PLAYER_START_Y,
    "icon": ' ' + PLAYER_ICON + ' '}
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 's':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = " - "
            util.clear_screen()
            player["row"] += 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'w':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = " - "
            util.clear_screen()
            player["row"] -= 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'a':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = " - "
            util.clear_screen()
            player["column"] -= 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'd':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = " - "
            util.clear_screen()
            player["column"] += 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
