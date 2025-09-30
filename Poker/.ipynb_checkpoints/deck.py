import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count=1):
        if count > len(self.cards):
            raise ValueError("Not enough cards to deal.")
        return [self.cards.pop() for _ in range(count)]
