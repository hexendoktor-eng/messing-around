import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def draw_cards(num_cards=5):
    deck = create_deck()
    if num_cards > len(deck):
        return "Not enough cards in deck"
    drawn_cards = random.sample(deck, num_cards)
    return drawn_cards

print("Drawing 5 cards for you:")
cards = draw_cards()
for i, card in enumerate(cards, 1):
    print(f"Card {i}: {card}")