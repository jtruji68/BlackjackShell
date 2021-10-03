import controller
import view

from model.shoe import Shoe
from model.table import Table
from model.player import Player
if __name__ == '__main__':
    view.print_welcome()
    shoe = Shoe()
    table = Table()
    player = Player()
    amount_bet = controller.bet_options()
    table.pot = amount_bet
    player.bet(amount_bet)

    controller.clear()

    card = shoe.draw_card()
    table.get_card(card,True)
    card = shoe.draw_card()
    table.get_card(card, False)
    card = shoe.draw_card()
    table.get_card(card,True)
    card = shoe.draw_card()
    table.get_card(card, False)
    view.print_chick()
    table.print_table(True)
    player.print_balance()
    print("=================================================")
    input()
    controller.clear()


    #table.print_table(False)




