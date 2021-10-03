import os
import random
from view import *
from model.shoe import Shoe

def create_shoe():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    number = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    suits = ["♥", "♠", "♦", "♣"]
    sh = []
    for deck in range(6):
        for suit in suits:
            for x in range(len(values)):
                sh.append({"card": values[x], "number": number[x], "suit": suit})
    random.shuffle(sh)
    return sh
shoe = create_shoe()

def set_balance():
    balance0 = 1000.00
    return balance0

balance = set_balance()


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
    return count1, count2


def initial_deal(dealer, player):
    player.append(shoe.pop())
    dealer.append(shoe.pop())
    player.append(shoe.pop())
    dealer.append(shoe.pop())
    return dealer, player

def new_draw(balance=balance):
    my_cards = []
    dealers_cards = []
    balance -= bet_options()
    show_newdraw()
    dealers_cards, my_cards = initial_deal(dealers_cards, my_cards)
    show_cards(dealers_cards,True,my_cards,balance)

def stay():
    print("Player stays")



def double():
    print("Player doubles")


def split():
    print("Player splits")


def menu_options(shoe, player, dealer, balance):
    choice = ""
    while choice != "5":
        options_bj_print(False, False)
        choice = str(input())
        if choice == "0":
            clear()
            result = ""
            if result == "busted":
                print("sneed")
                show_busted(balance=balance)
                new_draw()
        elif choice == "1":
            clear()
            stay()
            show_cards(dealer, True, player, balance)
        elif choice == "2":
            clear()
            double()
            show_cards(dealer, True, player, balance)
        elif choice == "3":
            clear()
            split()
            show_cards(dealer, True, player, balance)
        elif choice == "5":
            print("Adios")
            clear()
        else:
            print("Choice not valid")


def bet_options():
    choice = ""
    show_bets()
    while choice != "5":
        choice = str(input())
        if choice == "0":
            return 10
        elif choice == "1":
            return 20
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        elif choice == "4":
            return int(input("Ingrese el valor a apostar: "))
        elif choice == "5":
            return 0
        else:
            print("Choice not valid")

def round(balance=balance):
    my_cards = []
    dealers_cards = []
    dealers_cards, my_cards = initial_deal(dealers_cards, my_cards)
    balance -= bet_options()
    show_cards(dealers_cards, True, my_cards, balance)
    menu_options(shoe, my_cards, dealers_cards, balance)

def start():
    os.system('setterm -background green -foreground black -store')
    clear()
    #global sh
    #sh = Shoe()





