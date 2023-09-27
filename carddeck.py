import random
from card import Card

class CardDeck:
    # class data
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()
    
    def __init__(self, dealer_name):
        self._dealer_name = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def __str__(self):
        my_class = type(self)
        my_name = my_class.__name__
        return f"<{my_name} dealer={self.dealer}>"

    def __repr__(self):
        my_class = type(self)
        my_name = my_class.__name__
        return f"{my_name}('{self.dealer}')"

    @property
    def cards(self):
        return tuple(self._cards)


    @property
    def dealer(self):  # getter property
        return self._dealer_name 

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer_name = value
        else:
            raise TypeError("Dealer must be a str")

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)


