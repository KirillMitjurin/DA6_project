import random
def cards():
    single_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
    random.shuffle(single_deck)
    return single_deck

def player_card(card):
    player_cards = [card[0], card[2]]
    return player_cards
print(player_card(cards())) 


def dealer_card(card):
    dealer_card = [card[1], card[3]]
    return dealer_card


print(dealer_card(cards())) 
