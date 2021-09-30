import controller
from os import system, name


def print_cards(cards):
    message = ""
    for card in cards:
        message += f"  ___   "
    print(message)
    message = ""
    for card in cards:
        if len(card['card']) >= 2:
            message += f" |{card['card']} |  "
        else:
            message += f" |{card['card']}  |  "
    print(message)
    message = ""
    for card in cards:
        message += f" | {card['suit']} |  "
    print(message)
    message = ""
    for card in cards:
        if len(card['card']) >= 2:
            message += f" |_{card['card']}|  "
        else:
            message += f" |__{card['card']}|  "
    print(message + '\n')
    message = ""


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def show_cards(dealers_cards, hidden_, player_cards, balance):
    hidden = {'card': '?', 'number': "?", 'suit': '?'}

    if hidden_:
        dealers_cards[1] = hidden
    print("   Dealer's Hand")
    print_cards(dealers_cards)
    print("--------------------\n   Your Hand")
    print_cards(player_cards)
    count1, count2 = controller.get_count(player_cards)
    show_count(count1, count2)
    print_balance(balance)
    print("--------------------")


def show_count(count1, count2):
    if count1 != count2:
        print(f"Cuenta: {count1} / {count2} ")
    else:
        print(f"Cuenta: {count1}")


def options_bj_print(double, split):
    d, s = "", ""
    quit = "Quit: 5 |"
    if double:
        d = f"Split: 2 |"
    if split:
        s = f"Split: 3 |"
    print(f"| Hit: 0  | Stay: 1 | {d} {s} {quit}")


def print_balance(balance):
    print(f"Balance: ${balance}")


def print_welcome():
    print("""
♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ 
♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ 
  ___ _  _ ___ _    _                        
 / __| || | __| |  | |                       
 \__ \ __ | _|| |__| |__                     
 |___/_||_|___|____|____|__  _  _   ___ _  __
  | _ ) |    /_\ / __| |/ / | |/_\ / __| |/ /
  | _ \ |__ / _ \ (__| ' < || / _ \ (__| ' < 
  |___/____/_/ \_\___|_|\_\__/_/ \_\___|_|\_\  
  
♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ 
               ENTER TO START
♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥ ♦♦♦♦ ♣♣♣♣ ♠♠♠♠ ♥♥♥♥""")
    input()
    clear()
    deal_cards_print()


def deal_cards_print():
    print("=====================")
    print("     CARDS DEALED    ")
    print("=====================")


def show_bets():
    print("BET: ")
    print(f"| 🪙 10: 0  | 🪙 20: 1  | 🪙 50: 2 | 🪙 100: 3 ")
    print(f"Another value:  4")
