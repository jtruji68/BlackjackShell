import random


class Shoe:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        number = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        suits = ["♥", "♠", "♦", "♣"]
        sh = []
        for deck in range(6):
            for suit in suits:
                for x in range(len(values)):
                    sh.append({"card": values[x], "number": number[x], "suit": suit})
        random.shuffle(sh)
        self.shoe = sh

    def print_shoe(self):
        for card in self.shoe:
            print(card)

    def draw_card(self):
        return self.shoe.pop()

    def shuffle_shoe(self):
        random.shuffle(self.shoe)

    def remaining_cards(self):
        return len(self.shoe)