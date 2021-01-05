import util
import engine
import ui


# selected_character = "@"
player_start_x = 3
player_start_y = 3

board_width = 30
board_height = 20


def chars():
    print('1: 🧝‍ Laeroth ')
    print('2: 🧙‍ Wanaxx')
    print('3: 👨 Vladimir')


def characters():
    # print('\033c')
    chars()
    choise = input("To check character details enter 1. To choose character enter 2. ")

    if choise == '1':
        print('\033c')
        character_details()
    elif choise == '2':
        print('\033c')
        chars()
        return choose_character()
    else:
        print('\033c')


def character_details():
    # print('\033c')
    chars()
    
    while True:
        choise = input("Choose a character.(1,2,3 or 0 to get back to the menu) ")
        if choise == '1':
            print('\033c')
            chars()
            print("🧝‍ Laeroth is an elf. He deals more damage with a bow but deals less with a sword.")
        elif choise == '2':
            print('\033c')
            chars()
            print("🧙‍ Wanaxx a wizard. He.... ")
        elif choise == '3':
            print('\033c')
            chars()
            print("👨 Vladimir is a humen. He is the master of the swords.... ")
        elif choise == '0':
            print('\033c')
            characters()
        else:
            print('\033c')
            continue

'''      
def choose_character():
    chars()
    choosen_character = input ("Select your character. (1,2,3 or 0 to get back to the menu) ")
    if choosen_character == '1':
        PLAYER_ICON = '🧝'
        print("You chose Laeroth ")
        return PLAYER_ICON
    elif choosen_character =='2':
        PLAYER_ICON = '🧙‍'
        print("You chose Wanaxx ")
        return PLAYER_ICON
    elif choosen_character == '3':
        PLAYER_ICON = '👨'
        print("You chose Vladimir ")
        return PLAYER_ICON
    elif choosen_character == '0':
        characters()'''


def choose_character():
    heros = ("🧝", "🧙", "👨")
    selected_character = ""
    choosen_character = input("Select your character. (1,2,3 or 0 to get back to the menu) ")
    if choosen_character == "1":
        player_icon = heros[0]
        selected_character.join(player_icon)
    elif choosen_character == "2":
        player_icon = heros[1]
        selected_character.join(player_icon)
    elif choosen_character == "3":
        player_icon = heros[2]
        selected_character.join(player_icon)
    elif choosen_character == "0":
        print('\033c')
        selected_character = characters()
    print(selected_character)
    
    return selected_character


def create_player():
    characters()
    
    player = {
        "row": player_start_x,
        "2colum"': player_start_y,
        "icon": ' ' + selected_character + ' '} #Nem jöttem rá a megoldásra!

    return player


def main():
    player = create_player()
    board = engine.create_board(board_width, board_height)

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
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["row"] += 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'w':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["row"] -= 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'a':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
            util.clear_screen()
            player["column"] -= 1
            engine.put_player_on_board(board, player)
            util.clear_screen()
            ui.display_board(board)
        elif key == 'd':
            row = player["row"]
            column = player["column"]
            board[row-1][column-1] = "   "
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
