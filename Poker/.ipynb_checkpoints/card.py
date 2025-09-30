class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_values = {rank: index for index, rank in enumerate(ranks, start=2)}

    def __init__(self, rank, suit):
        if rank not in self.ranks or suit not in self.suits:
            raise ValueError("Invalid card rank or suit.")
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return self.rank_values[self.rank]
