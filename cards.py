import random

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
number = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suits = ["♥", "♠", "♦", "♣"]
value = "A"
suit = "♣"
# print(f" ___\n|{value}  |\n| {suit} |\n|__{value}|")
hidden_print = f" ___\n|\\|/|\n|-?-|\n|/|\\|"
deck = []
for suit in suits:
    for x in range(len(values)):
        deck.append({"card": values[x], "number": number[x], "suit": suit})

#print(deck[0])
#print(len(deck))


def print_cards(cards):
    message = ""
    for card in cards:
        message += f" ___   "
    print(message)
    message = ""
    for card in cards:
        if len(card['card']) >=2:
            message += f"|{card['card']} |  "
        else:
            message += f"|{card['card']}  |  "
    print(message)
    message = ""
    for card in cards:
        message += f"| {card['suit']} |  "
    print(message)
    message = ""
    for card in cards:
        if len(card['card']) >= 2:
            message += f"|_{card['card']}|  "
        else:
            message += f"|__{card['card']}|  "
    print(message)
    message = ""
"""
for card in deck:
    if len(card['card']) < 2:
        print(f" ___\n|{card['card']}  |\n| {card['suit']} |\n|__{card['card']}|")
    else:
        print(f" ___\n|{card['card']}  |\n| {card['suit']}  |\n|__{card['card']}|")
"""

hidden = {'card': '?', 'number': "?", 'suit': '?'}
#test = [{'card': 'A', 'number': [1, 11], 'suit': '♣'},{'card': '2', 'number': 2, 'suit': '♦'},{'card': '10', 'number': 10, 'suit': '♥'}]
#test.append(hidden)

random.shuffle(deck)

my_cards = []
dealers_cards = []
def get_count(p_cards):
    count1 = 0
    count2 = 0
    for c in p_cards:
        if c['card'] == "A":
            count1 += int(c['number'][0])
            count2 += int(c['number'][1])
        else:
            count1 += int(c['number'])
            count2 += int(c['number'])
    return count1,count2

def evaluate_count(count1,count2):
    if count1 < 22:
        pass

def options_bj_print(double, split):
    d,s = "",""
    if double:
        d = f"Split 3 |"
    if split:
        s = f"Split 4 |"
    print(f"| Hit: 0  | Stay: 1 | {d} {s}")

def show_cards(dealers_cards,hidden_,player_cards):
    if hidden:
        dealers_cards[1] = hidden
    print("mano de dealer")
    print_cards(dealers_cards)
    print("--------------------\nmano de jugador1")
    print_cards(player_cards)
    count1, count2 = get_count(player_cards)
    if count1 != count2:
        print(f"cuenta: {count1} / {count2} ")
    else:
     print(f"cuenta: {count1}")
    print("--------------------\n")

print("se reparten las cartas")
my_cards.append(deck.pop())
dealers_cards.append(deck.pop())
my_cards.append(deck.pop())
dealers_cards.append(deck.pop())

show_cards(dealers_cards,True,my_cards)

options_bj_print(False,True)
print("jugador1 hit")
my_cards.append(deck.pop())
show_cards(dealers_cards,True,my_cards)