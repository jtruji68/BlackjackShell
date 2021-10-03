import view


class Table:
    def __init__(self):
        self.dealer_hand = []
        self.player_hand = []
        self.pot = 0

    def get_card(self,card,player):
        if player:
            self.player_hand.append(card)
        else:
            self.dealer_hand.append(card)

    def print_table(self,hidden):
        print("=============Dealer's Hand=======================")
        if not hidden:
            view.print_cards(self.dealer_hand)
            c1, c2 = self.count_hand(False)
            print(f"Count: {self.show_count(c1, c2)}")
        else:
            hidden_card = {"card": "?", "number": "?", "suit": "?"}
            dealer_hidden = self.dealer_hand[:]
            dealer_hidden[1] = hidden_card
            view.print_cards(dealer_hidden)


        print("=============Your Hand===========================")
        view.print_cards(self.player_hand)
        co1,co2 = self.count_hand(True)
        print(f"Count: {self.show_count(co1,co2)}")
        print("=================================================")
        view.print_pot(self.pot)

    def count_hand(self,player):
        hand = self.player_hand[:] if player else self.dealer_hand[:]
        count1 = 0
        count2 = 0
        for c in hand:
            if c['card'] == "A":
                count1 += int(c['number'][0])
                count2 += int(c['number'][1])
            else:
                count1 += int(c['number'])
                count2 += int(c['number'])
        return count1, count2

    def validate_count(self,count1,count2):
        if count1 >= 22 and count2 >= 22:
            return "busted"

    def show_count(self,count1,count2):
        if count1 != count2:
            return f"{count1}/{count2}"
        else:
            return f"{count1}"

